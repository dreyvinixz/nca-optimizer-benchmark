/*
 * cnn_cuda.cu — Complete 1D-CNN Training on NVIDIA GPU
 *
 * Architecture: Input[N, T, 1] -> Conv1D(F, K) -> GlobalMaxPool1D -> Dense(D) -> Dropout -> Dense(1) -> Sigmoid
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <float.h>
#include <time.h>

#include <cuda_runtime.h>
#include <cublas_v2.h>
#include <curand.h>
#include <curand_kernel.h>

#include "cnn_cuda.h"

#define BLOCK 256
#define EPS   1e-7f

#define CK(call) do { \
    cudaError_t e = (call); \
    if (e != cudaSuccess) { \
        fprintf(stderr, "CUDA %s:%d %s\n", __FILE__, __LINE__, cudaGetErrorString(e)); \
        return -1; \
    } \
} while (0)

#define CMALLOC(ptr, bytes) CK(cudaMalloc((void **)(ptr), (bytes)))

#define CB(call) do { \
    cublasStatus_t s = (call); \
    if (s != CUBLAS_STATUS_SUCCESS) { \
        fprintf(stderr, "cuBLAS %s:%d status=%d\n", __FILE__, __LINE__, (int)s); \
        return -1; \
    } \
} while (0)

#define GRID(n) (((n) + BLOCK - 1) / BLOCK)

#define KC() do {                                           \
    cudaError_t e = cudaGetLastError();                     \
    if (e != cudaSuccess) {                                 \
        fprintf(stderr, "CUDA kernel %s:%d %s\n",           \
                __FILE__, __LINE__, cudaGetErrorString(e)); \
        return -1;                                          \
    }                                                       \
} while (0)

/* ================================================================
 *  Shared Kernels
 * ================================================================ */

__global__ void k_tanh_fwd(const float *z, float *a, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) a[i] = tanhf(z[i]);
}

__global__ void k_tanh_bwd(const float *da, const float *z, float *dz, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) { float t = tanhf(z[i]); dz[i] = da[i] * (1.0f - t * t); }
}

__global__ void k_relu_fwd(const float *z, float *a, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) a[i] = fmaxf(0.0f, z[i]);
}

__global__ void k_relu_bwd(const float *da, const float *z, float *dz, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) dz[i] = (z[i] > 0.0f) ? da[i] : 0.0f;
}

__global__ void k_sigmoid(const float *z, float *a, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        float v = fminf(fmaxf(z[i], -50.0f), 50.0f);
        a[i] = 1.0f / (1.0f + expf(-v));
    }
}

__global__ void k_add_bias(float *out, const float *bias, int rows, int cols) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < rows * cols) out[i] += bias[i % cols];
}

__global__ void k_bias_grad(const float *dz, float *db, int rows, int cols) {
    int c = blockIdx.x * BLOCK + threadIdx.x;
    if (c < cols) {
        float s = 0.0f;
        for (int r = 0; r < rows; r++) s += dz[r * cols + c];
        db[c] = s;
    }
}

__global__ void k_output_grad(const float *a, const float *y, float *dz, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) dz[i] = (a[i] - y[i]) / (float)n;
}

__global__ void k_add_l2(float *dw, const float *w, float alpha, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) dw[i] += 2.0f * alpha * w[i];
}

__global__ void k_dropout_fwd(float *a, float *mask, unsigned long long seed, unsigned long long offset, float rate, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        curandStatePhilox4_32_10_t st;
        curand_init(seed, (unsigned long long)i, offset, &st);
        float r = curand_uniform(&st);
        if (r < rate) {
            mask[i] = 0.0f; a[i] = 0.0f;
        } else {
            float scale = 1.0f / (1.0f - rate);
            mask[i] = scale; a[i] *= scale;
        }
    }
}

__global__ void k_dropout_bwd(float *da, const float *mask, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) da[i] *= mask[i];
}

__global__ void k_bce(const float *y, const float *a, float *loss, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        float p = fminf(fmaxf(a[i], EPS), 1.0f - EPS);
        loss[i] = -(y[i] * logf(p) + (1.0f - y[i]) * logf(1.0f - p));
    }
}

static int reduce_sum_host(float *d_buf, int n, float *sum_out) {
    if (n <= 0 || sum_out == NULL) {
        fprintf(stderr, "Invalid reduction size\n");
        return -1;
    }
    float *h = (float *)malloc(n * sizeof(float));
    if (h == NULL) {
        fprintf(stderr, "Host allocation failed in reduce_sum_host\n");
        return -1;
    }
    cudaError_t e = cudaMemcpy(h, d_buf, n * sizeof(float),
                               cudaMemcpyDeviceToHost);
    if (e != cudaSuccess) {
        fprintf(stderr, "CUDA memcpy reduce_sum_host: %s\n",
                cudaGetErrorString(e));
        free(h);
        return -1;
    }
    double s = 0.0;
    for (int i = 0; i < n; i++) s += (double)h[i];
    free(h);
    *sum_out = (float)s;
    return 0;
}

__global__ void k_rmsprop(float *p, const float *g, float *cache, float lr, float rho, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        cache[i] = rho * cache[i] + (1.0f - rho) * g[i] * g[i];
        p[i] -= lr * g[i] / (sqrtf(cache[i]) + EPS);
    }
}

__global__ void k_adam(float *p, const float *g, float *m, float *v, float lr, float b1, float b2, float b1t, float b2t, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        m[i] = b1 * m[i] + (1.0f - b1) * g[i];
        v[i] = b2 * v[i] + (1.0f - b2) * g[i] * g[i];
        float mh = m[i] / (1.0f - b1t);
        float vh = v[i] / (1.0f - b2t);
        p[i] -= lr * mh / (sqrtf(vh) + EPS);
    }
}

static inline cublasStatus_t matmul(cublasHandle_t h, const float *A, const float *B, float *C, int m, int k, int n, float alpha, float beta) {
    return cublasSgemm(h, CUBLAS_OP_N, CUBLAS_OP_N, n, m, k, &alpha, B, n, A, k, &beta, C, n);
}

static inline cublasStatus_t matmul_atb(cublasHandle_t h, const float *A, const float *B, float *C, int m, int k, int n, float alpha, float beta) {
    return cublasSgemm(h, CUBLAS_OP_N, CUBLAS_OP_T, n, k, m, &alpha, B, n, A, k, &beta, C, n);
}

static inline cublasStatus_t matmul_abt(cublasHandle_t h, const float *A, const float *B, float *C, int m, int k, int n, float alpha, float beta) {
    return cublasSgemm(h, CUBLAS_OP_T, CUBLAS_OP_N, n, m, k, &alpha, B, k, A, k, &beta, C, n);
}

static void xavier_init(float *buf, int fan_in, int fan_out, unsigned int seed) {
    float limit = sqrtf(6.0f / (float)(fan_in + fan_out));
    srand(seed);
    for (int i = 0; i < fan_in * fan_out; i++)
        buf[i] = ((float)rand() / (float)RAND_MAX) * 2.0f * limit - limit;
}

static void glorot_init_n(float *buf, int n_values, int fan_in, int fan_out,
                          unsigned int seed) {
    float limit = sqrtf(6.0f / (float)(fan_in + fan_out));
    srand(seed);
    for (int i = 0; i < n_values; i++)
        buf[i] = ((float)rand() / (float)RAND_MAX) * 2.0f * limit - limit;
}

/* ================================================================
 *  CNN Specific Kernels
 * ================================================================ */

/* Conv1D forward: X is [N, T], W is [K, F], Z is [N, T, F].
   Padding matches TensorFlow/Keras "same" for stride 1. */
__global__ void k_conv1d_fwd(const float *X, const float *W, const float *b, float *Z, int N, int T, int F, int K) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int total = N * T * F;
    if (idx < total) {
        int f = idx % F;
        int t = (idx / F) % T;
        int n = idx / (F * T);
        
        float sum = b[f];
        int P = (K - 1) / 2;
        for (int k = 0; k < K; k++) {
            int t_in = t + k - P;
            if (t_in >= 0 && t_in < T) {
                sum += X[n * T + t_in] * W[k * F + f];
            }
        }
        Z[idx] = sum;
    }
}

/* Conv1D Backward w.r.t W and b */
__global__ void k_conv1d_bwd_W_b(const float *dZ, const float *X, float *dW, float *db, int N, int T, int F, int K) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int total = K * F;
    if (idx < total) {
        int f = idx % F;
        int k = idx / F;
        
        float sum_W = 0.0f;
        int P = (K - 1) / 2;
        for (int n = 0; n < N; n++) {
            for (int t = 0; t < T; t++) {
                int t_in = t + k - P;
                if (t_in >= 0 && t_in < T) {
                    sum_W += dZ[(n * T + t) * F + f] * X[n * T + t_in];
                }
            }
        }
        dW[idx] = sum_W;
        
        if (k == 0) {
            float sum_b = 0.0f;
            for (int n = 0; n < N; n++) {
                for (int t = 0; t < T; t++) {
                    sum_b += dZ[(n * T + t) * F + f];
                }
            }
            db[f] = sum_b;
        }
    }
}

/* GlobalMaxPool1D Forward: A1 is [N, T, F]. Z2 is [N, F]. M is [N, F] */
__global__ void k_maxpool1d_fwd(const float *A1, float *Z2, int *M, int N, int T, int F) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int total = N * F;
    if (idx < total) {
        int f = idx % F;
        int n = idx / F;
        
        float max_val = -1e30f;
        int max_idx = 0;
        for (int t = 0; t < T; t++) {
            float val = A1[(n * T + t) * F + f];
            if (val > max_val) {
                max_val = val;
                max_idx = t;
            }
        }
        Z2[idx] = max_val;
        M[idx] = max_idx;
    }
}

/* GlobalMaxPool1D Backward: dZ2 is [N, F]. dA1 is [N, T, F] */
__global__ void k_maxpool1d_bwd(const float *dZ2, const int *M, float *dA1, int N, int T, int F) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    int total = N * F;
    if (idx < total) {
        int f = idx % F;
        int n = idx / F;
        
        int max_idx = M[idx];
        float grad = dZ2[idx];
        for (int t = 0; t < T; t++) {
            dA1[(n * T + t) * F + f] = (t == max_idx) ? grad : 0.0f;
        }
    }
}

/* ================================================================
 *  CNN Context
 * ================================================================ */

typedef struct {
    float *Wc, *bc, *W1, *b1, *W2, *b2;
    float *dWc, *dbc, *dW1, *db1, *dW2, *db2;
    float *cWc, *cbc, *cW1, *cb1, *cW2, *cb2;
    float *vWc, *vbc, *vW1, *vb1, *vW2, *vb2;
    float *Zc, *Ac, *Zp;
    int   *Mp;
    float *Zd, *Ad, *mask, *Zout, *Aout;
    float *dZout, *dAd, *dZd, *dZp, *dAc, *dZc;
    float *loss_buf;
    float *d_Xtrain, *d_ytrain, *d_Xval, *d_yval, *d_Xeval;
    int T, F, K, D, n_train_actual, n_val_internal, n_eval;
    int batch_size, max_epochs, patience;
    float lr, l2, dropout;
    int use_tanh, use_adam;
    unsigned int seed;
} CNNContext;

static int ctx_alloc(CNNContext *ctx, int max_batch) {
    int T = ctx->T, F = ctx->F, K = ctx->K, D = ctx->D;
    int max_samples = max_batch;
    if (ctx->n_val_internal > max_samples) max_samples = ctx->n_val_internal;
    if (ctx->n_eval > max_samples) max_samples = ctx->n_eval;

    CMALLOC(&ctx->Wc, K * F * sizeof(float));
    CMALLOC(&ctx->bc, F * sizeof(float));
    CMALLOC(&ctx->W1, F * D * sizeof(float));
    CMALLOC(&ctx->b1, D * sizeof(float));
    CMALLOC(&ctx->W2, D * sizeof(float));
    CMALLOC(&ctx->b2, sizeof(float));

    CMALLOC(&ctx->dWc, K * F * sizeof(float));
    CMALLOC(&ctx->dbc, F * sizeof(float));
    CMALLOC(&ctx->dW1, F * D * sizeof(float));
    CMALLOC(&ctx->db1, D * sizeof(float));
    CMALLOC(&ctx->dW2, D * sizeof(float));
    CMALLOC(&ctx->db2, sizeof(float));

    CMALLOC(&ctx->cWc, K * F * sizeof(float));
    CMALLOC(&ctx->cbc, F * sizeof(float));
    CMALLOC(&ctx->cW1, F * D * sizeof(float));
    CMALLOC(&ctx->cb1, D * sizeof(float));
    CMALLOC(&ctx->cW2, D * sizeof(float));
    CMALLOC(&ctx->cb2, sizeof(float));

    CK(cudaMemset(ctx->cWc, 0, K * F * sizeof(float)));
    CK(cudaMemset(ctx->cbc, 0, F * sizeof(float)));
    CK(cudaMemset(ctx->cW1, 0, F * D * sizeof(float)));
    CK(cudaMemset(ctx->cb1, 0, D * sizeof(float)));
    CK(cudaMemset(ctx->cW2, 0, D * sizeof(float)));
    CK(cudaMemset(ctx->cb2, 0, sizeof(float)));

    if (ctx->use_adam) {
        CMALLOC(&ctx->vWc, K * F * sizeof(float));
        CMALLOC(&ctx->vbc, F * sizeof(float));
        CMALLOC(&ctx->vW1, F * D * sizeof(float));
        CMALLOC(&ctx->vb1, D * sizeof(float));
        CMALLOC(&ctx->vW2, D * sizeof(float));
        CMALLOC(&ctx->vb2, sizeof(float));
        CK(cudaMemset(ctx->vWc, 0, K * F * sizeof(float)));
        CK(cudaMemset(ctx->vbc, 0, F * sizeof(float)));
        CK(cudaMemset(ctx->vW1, 0, F * D * sizeof(float)));
        CK(cudaMemset(ctx->vb1, 0, D * sizeof(float)));
        CK(cudaMemset(ctx->vW2, 0, D * sizeof(float)));
        CK(cudaMemset(ctx->vb2, 0, sizeof(float)));
    } else {
        ctx->vWc = ctx->vbc = ctx->vW1 = ctx->vb1 = ctx->vW2 = ctx->vb2 = NULL;
    }

    CMALLOC(&ctx->Zc, max_samples * T * F * sizeof(float));
    CMALLOC(&ctx->Ac, max_samples * T * F * sizeof(float));
    CMALLOC(&ctx->Zp, max_samples * F * sizeof(float));
    CMALLOC(&ctx->Mp, max_samples * F * sizeof(int));
    CMALLOC(&ctx->Zd, max_samples * D * sizeof(float));
    CMALLOC(&ctx->Ad, max_samples * D * sizeof(float));
    CMALLOC(&ctx->mask, max_samples * D * sizeof(float));
    CMALLOC(&ctx->Zout, max_samples * sizeof(float));
    CMALLOC(&ctx->Aout, max_samples * sizeof(float));

    CMALLOC(&ctx->dZout, max_samples * sizeof(float));
    CMALLOC(&ctx->dAd, max_samples * D * sizeof(float));
    CMALLOC(&ctx->dZd, max_samples * D * sizeof(float));
    CMALLOC(&ctx->dZp, max_samples * F * sizeof(float));
    CMALLOC(&ctx->dAc, max_samples * T * F * sizeof(float));
    CMALLOC(&ctx->dZc, max_samples * T * F * sizeof(float));
    CMALLOC(&ctx->loss_buf, max_samples * sizeof(float));

    return 0;
}

static void ctx_free(CNNContext *ctx) {
    cudaFree(ctx->Wc); cudaFree(ctx->bc);
    cudaFree(ctx->W1); cudaFree(ctx->b1);
    cudaFree(ctx->W2); cudaFree(ctx->b2);
    cudaFree(ctx->dWc); cudaFree(ctx->dbc);
    cudaFree(ctx->dW1); cudaFree(ctx->db1);
    cudaFree(ctx->dW2); cudaFree(ctx->db2);
    cudaFree(ctx->cWc); cudaFree(ctx->cbc);
    cudaFree(ctx->cW1); cudaFree(ctx->cb1);
    cudaFree(ctx->cW2); cudaFree(ctx->cb2);
    if (ctx->vWc) {
        cudaFree(ctx->vWc); cudaFree(ctx->vbc);
        cudaFree(ctx->vW1); cudaFree(ctx->vb1);
        cudaFree(ctx->vW2); cudaFree(ctx->vb2);
    }
    cudaFree(ctx->Zc); cudaFree(ctx->Ac); cudaFree(ctx->Zp); cudaFree(ctx->Mp);
    cudaFree(ctx->Zd); cudaFree(ctx->Ad); cudaFree(ctx->mask); cudaFree(ctx->Zout); cudaFree(ctx->Aout);
    cudaFree(ctx->dZout); cudaFree(ctx->dAd); cudaFree(ctx->dZd); cudaFree(ctx->dZp); cudaFree(ctx->dAc); cudaFree(ctx->dZc);
    cudaFree(ctx->loss_buf);
    cudaFree(ctx->d_Xtrain); cudaFree(ctx->d_ytrain);
    cudaFree(ctx->d_Xval); cudaFree(ctx->d_yval); cudaFree(ctx->d_Xeval);
}

static int forward(CNNContext *ctx, cublasHandle_t cublas, const float *d_X, int N, int training, unsigned long long dropout_offset) {
    int T = ctx->T, F = ctx->F, K = ctx->K, D = ctx->D;
    
    k_conv1d_fwd<<<GRID(N * T * F), BLOCK>>>(d_X, ctx->Wc, ctx->bc, ctx->Zc, N, T, F, K);
    KC();
    if (ctx->use_tanh) k_tanh_fwd<<<GRID(N * T * F), BLOCK>>>(ctx->Zc, ctx->Ac, N * T * F);
    else k_relu_fwd<<<GRID(N * T * F), BLOCK>>>(ctx->Zc, ctx->Ac, N * T * F);
    KC();

    k_maxpool1d_fwd<<<GRID(N * F), BLOCK>>>(ctx->Ac, ctx->Zp, ctx->Mp, N, T, F);
    KC();

    CB(matmul(cublas, ctx->Zp, ctx->W1, ctx->Zd, N, F, D, 1.0f, 0.0f));
    k_add_bias<<<GRID(N * D), BLOCK>>>(ctx->Zd, ctx->b1, N, D);
    KC();

    if (ctx->use_tanh) k_tanh_fwd<<<GRID(N * D), BLOCK>>>(ctx->Zd, ctx->Ad, N * D);
    else k_relu_fwd<<<GRID(N * D), BLOCK>>>(ctx->Zd, ctx->Ad, N * D);
    KC();

    if (training && ctx->dropout > 0.0f) {
        k_dropout_fwd<<<GRID(N * D), BLOCK>>>(ctx->Ad, ctx->mask, ctx->seed + 777ULL, dropout_offset, ctx->dropout, N * D);
        KC();
    }

    CB(matmul(cublas, ctx->Ad, ctx->W2, ctx->Zout, N, D, 1, 1.0f, 0.0f));
    k_add_bias<<<GRID(N), BLOCK>>>(ctx->Zout, ctx->b2, N, 1);
    KC();
    k_sigmoid<<<GRID(N), BLOCK>>>(ctx->Zout, ctx->Aout, N);
    KC();

    return 0;
}

static int backward(CNNContext *ctx, cublasHandle_t cublas, const float *d_X, const float *d_y, int N) {
    int T = ctx->T, F = ctx->F, K = ctx->K, D = ctx->D;

    k_output_grad<<<GRID(N), BLOCK>>>(ctx->Aout, d_y, ctx->dZout, N);
    KC();

    CB(matmul_atb(cublas, ctx->Ad, ctx->dZout, ctx->dW2, N, D, 1, 1.0f, 0.0f));
    k_bias_grad<<<GRID(1), BLOCK>>>(ctx->dZout, ctx->db2, N, 1);
    KC();
    CB(matmul_abt(cublas, ctx->dZout, ctx->W2, ctx->dAd, N, 1, D, 1.0f, 0.0f));

    if (ctx->dropout > 0.0f) {
        k_dropout_bwd<<<GRID(N * D), BLOCK>>>(ctx->dAd, ctx->mask, N * D);
        KC();
    }

    if (ctx->use_tanh) k_tanh_bwd<<<GRID(N * D), BLOCK>>>(ctx->dAd, ctx->Zd, ctx->dZd, N * D);
    else k_relu_bwd<<<GRID(N * D), BLOCK>>>(ctx->dAd, ctx->Zd, ctx->dZd, N * D);
    KC();

    CB(matmul_atb(cublas, ctx->Zp, ctx->dZd, ctx->dW1, N, F, D, 1.0f, 0.0f));
    k_bias_grad<<<GRID(D), BLOCK>>>(ctx->dZd, ctx->db1, N, D);
    KC();
    CB(matmul_abt(cublas, ctx->dZd, ctx->W1, ctx->dZp, N, D, F, 1.0f, 0.0f));

    k_maxpool1d_bwd<<<GRID(N * F), BLOCK>>>(ctx->dZp, ctx->Mp, ctx->dAc, N, T, F);
    KC();

    if (ctx->use_tanh) k_tanh_bwd<<<GRID(N * T * F), BLOCK>>>(ctx->dAc, ctx->Zc, ctx->dZc, N * T * F);
    else k_relu_bwd<<<GRID(N * T * F), BLOCK>>>(ctx->dAc, ctx->Zc, ctx->dZc, N * T * F);
    KC();

    k_conv1d_bwd_W_b<<<GRID(K * F), BLOCK>>>(ctx->dZc, d_X, ctx->dWc, ctx->dbc, N, T, F, K);
    KC();

    if (ctx->l2 > 0.0f) {
        k_add_l2<<<GRID(K * F), BLOCK>>>(ctx->dWc, ctx->Wc, ctx->l2, K * F);
        k_add_l2<<<GRID(F * D), BLOCK>>>(ctx->dW1, ctx->W1, ctx->l2, F * D);
        KC();
    }

    return 0;
}

static int update_params(CNNContext *ctx, int step) {
    int F = ctx->F, K = ctx->K, D = ctx->D;

    if (ctx->use_adam) {
        float b1 = 0.9f, b2 = 0.999f;
        float b1t = powf(b1, (float)step);
        float b2t = powf(b2, (float)step);
        k_adam<<<GRID(K*F), BLOCK>>>(ctx->Wc, ctx->dWc, ctx->cWc, ctx->vWc, ctx->lr, b1, b2, b1t, b2t, K*F);
        k_adam<<<GRID(F), BLOCK>>>(ctx->bc, ctx->dbc, ctx->cbc, ctx->vbc, ctx->lr, b1, b2, b1t, b2t, F);
        k_adam<<<GRID(F*D), BLOCK>>>(ctx->W1, ctx->dW1, ctx->cW1, ctx->vW1, ctx->lr, b1, b2, b1t, b2t, F*D);
        k_adam<<<GRID(D), BLOCK>>>(ctx->b1, ctx->db1, ctx->cb1, ctx->vb1, ctx->lr, b1, b2, b1t, b2t, D);
        k_adam<<<GRID(D), BLOCK>>>(ctx->W2, ctx->dW2, ctx->cW2, ctx->vW2, ctx->lr, b1, b2, b1t, b2t, D);
        k_adam<<<GRID(1), BLOCK>>>(ctx->b2, ctx->db2, ctx->cb2, ctx->vb2, ctx->lr, b1, b2, b1t, b2t, 1);
        KC();
    } else {
        float rho = 0.9f;
        k_rmsprop<<<GRID(K*F), BLOCK>>>(ctx->Wc, ctx->dWc, ctx->cWc, ctx->lr, rho, K*F);
        k_rmsprop<<<GRID(F), BLOCK>>>(ctx->bc, ctx->dbc, ctx->cbc, ctx->lr, rho, F);
        k_rmsprop<<<GRID(F*D), BLOCK>>>(ctx->W1, ctx->dW1, ctx->cW1, ctx->lr, rho, F*D);
        k_rmsprop<<<GRID(D), BLOCK>>>(ctx->b1, ctx->db1, ctx->cb1, ctx->lr, rho, D);
        k_rmsprop<<<GRID(D), BLOCK>>>(ctx->W2, ctx->dW2, ctx->cW2, ctx->lr, rho, D);
        k_rmsprop<<<GRID(1), BLOCK>>>(ctx->b2, ctx->db2, ctx->cb2, ctx->lr, rho, 1);
        KC();
    }
    return 0;
}

static int compute_loss(CNNContext *ctx, cublasHandle_t cublas,
                        const float *d_y, int N, float *loss_out) {
    if (loss_out == NULL) return -1;
    k_bce<<<GRID(N), BLOCK>>>(d_y, ctx->Aout, ctx->loss_buf, N);
    KC();
    CK(cudaDeviceSynchronize());

    float bce_sum = 0.0f;
    if (reduce_sum_host(ctx->loss_buf, N, &bce_sum) != 0)
        return -1;

    float reg = 0.0f;
    if (ctx->l2 > 0.0f) {
        float wc_sq = 0.0f;
        float w1_sq = 0.0f;
        CB(cublasSdot(cublas, ctx->K * ctx->F,
                      ctx->Wc, 1, ctx->Wc, 1, &wc_sq));
        CB(cublasSdot(cublas, ctx->F * ctx->D,
                      ctx->W1, 1, ctx->W1, 1, &w1_sq));
        reg = ctx->l2 * (wc_sq + w1_sq);
    }

    *loss_out = bce_sum / (float)N + reg;
    return 0;
}

typedef struct {
    float *Wc, *bc, *W1, *b1, *W2, *b2;
    int F, K, D;
} CNNSnapshot;

static int snapshot_alloc(CNNSnapshot *snap, int F, int K, int D) {
    snap->F = F; snap->K = K; snap->D = D;
    CMALLOC(&snap->Wc, K * F * sizeof(float));
    CMALLOC(&snap->bc, F * sizeof(float));
    CMALLOC(&snap->W1, F * D * sizeof(float));
    CMALLOC(&snap->b1, D * sizeof(float));
    CMALLOC(&snap->W2, D * sizeof(float));
    CMALLOC(&snap->b2, sizeof(float));
    return 0;
}

static void snapshot_save(CNNSnapshot *snap, CNNContext *ctx) {
    int F = snap->F, K = snap->K, D = snap->D;
    cudaMemcpy(snap->Wc, ctx->Wc, K*F*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->bc, ctx->bc, F*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->W1, ctx->W1, F*D*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->b1, ctx->b1, D*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->W2, ctx->W2, D*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->b2, ctx->b2, sizeof(float), cudaMemcpyDeviceToDevice);
}

static void snapshot_restore(CNNSnapshot *snap, CNNContext *ctx) {
    int F = snap->F, K = snap->K, D = snap->D;
    cudaMemcpy(ctx->Wc, snap->Wc, K*F*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->bc, snap->bc, F*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->W1, snap->W1, F*D*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->b1, snap->b1, D*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->W2, snap->W2, D*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->b2, snap->b2, sizeof(float), cudaMemcpyDeviceToDevice);
}

static void snapshot_free(CNNSnapshot *snap) {
    cudaFree(snap->Wc); cudaFree(snap->bc);
    cudaFree(snap->W1); cudaFree(snap->b1);
    cudaFree(snap->W2); cudaFree(snap->b2);
}

extern "C"
int cnn_train_predict(
    const float *X_train_h, const float *y_train_h, int n_train,
    const float *X_eval_h,  int n_eval,
    int input_dim, int n_filters, int kernel_size, int dense_neurons,
    float learning_rate, float l2_alpha, float dropout_rate,
    int batch_size, int max_epochs, int patience,
    int use_tanh, int use_adam, unsigned int seed,
    float *y_pred_out, float *y_proba_out,
    float *train_time_out, float *val_loss_out)
{
    if (X_train_h == NULL || y_train_h == NULL || X_eval_h == NULL ||
        y_pred_out == NULL || y_proba_out == NULL ||
        train_time_out == NULL || val_loss_out == NULL ||
        n_train < 2 || n_eval < 1 || input_dim < 1 ||
        n_filters < 1 || kernel_size < 1 || dense_neurons < 1 ||
        batch_size < 1 || max_epochs < 1 || patience < 0 ||
        learning_rate <= 0.0f || l2_alpha < 0.0f ||
        dropout_rate < 0.0f || dropout_rate >= 1.0f) {
        fprintf(stderr, "Invalid CNN CUDA training arguments\n");
        return -1;
    }

    int n_val_int = (int)(0.15f * (float)n_train);
    if (n_val_int < 1) n_val_int = 1;
    int n_train_act = n_train - n_val_int;

    cudaEvent_t t0, t1;
    CK(cudaEventCreate(&t0)); CK(cudaEventCreate(&t1));
    CK(cudaEventRecord(t0));

    cublasHandle_t cublas;
    CB(cublasCreate(&cublas));

    CNNContext ctx;
    memset(&ctx, 0, sizeof(ctx));
    ctx.T = input_dim; ctx.F = n_filters; ctx.K = kernel_size; ctx.D = dense_neurons;
    ctx.n_train_actual = n_train_act; ctx.n_val_internal = n_val_int; ctx.n_eval = n_eval;
    ctx.batch_size = batch_size; ctx.max_epochs = max_epochs; ctx.patience = patience;
    ctx.lr = learning_rate; ctx.l2 = l2_alpha; ctx.dropout = dropout_rate;
    ctx.use_tanh = use_tanh; ctx.use_adam = use_adam; ctx.seed = seed;

    int max_batch = batch_size;
    if (n_val_int > max_batch) max_batch = n_val_int;
    if (n_eval > max_batch) max_batch = n_eval;

    if (ctx_alloc(&ctx, max_batch) != 0) return -1;

    CMALLOC(&ctx.d_Xtrain, n_train_act * ctx.T * sizeof(float));
    CMALLOC(&ctx.d_ytrain, n_train_act * sizeof(float));
    CMALLOC(&ctx.d_Xval,   n_val_int * ctx.T * sizeof(float));
    CMALLOC(&ctx.d_yval,   n_val_int * sizeof(float));
    CMALLOC(&ctx.d_Xeval,  n_eval * ctx.T * sizeof(float));

    CK(cudaMemcpy(ctx.d_Xtrain, X_train_h, n_train_act * ctx.T * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_ytrain, y_train_h, n_train_act * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_Xval, X_train_h + n_train_act * ctx.T, n_val_int * ctx.T * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_yval, y_train_h + n_train_act, n_val_int * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_Xeval, X_eval_h, n_eval * ctx.T * sizeof(float), cudaMemcpyHostToDevice));

    float *h_Wc = (float *)malloc(ctx.K * ctx.F * sizeof(float));
    float *h_bc = (float *)calloc(ctx.F, sizeof(float));
    float *h_W1 = (float *)malloc(ctx.F * ctx.D * sizeof(float));
    float *h_b1 = (float *)calloc(ctx.D, sizeof(float));
    float *h_W2 = (float *)malloc(ctx.D * sizeof(float));
    float  h_b2 = 0.0f;
    if (h_Wc == NULL || h_bc == NULL || h_W1 == NULL ||
        h_b1 == NULL || h_W2 == NULL) {
        fprintf(stderr, "Host allocation failed during CNN initialization\n");
        free(h_Wc); free(h_bc); free(h_W1); free(h_b1); free(h_W2);
        return -1;
    }

    glorot_init_n(h_Wc, ctx.K * ctx.F, ctx.K, ctx.K * ctx.F, seed);
    xavier_init(h_W1, ctx.F, ctx.D, seed + 1);
    xavier_init(h_W2, ctx.D, 1, seed + 2);

    CK(cudaMemcpy(ctx.Wc, h_Wc, ctx.K * ctx.F * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.bc, h_bc, ctx.F * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.W1, h_W1, ctx.F * ctx.D * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.b1, h_b1, ctx.D * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.W2, h_W2, ctx.D * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.b2, &h_b2, sizeof(float), cudaMemcpyHostToDevice));
    free(h_Wc); free(h_bc); free(h_W1); free(h_b1); free(h_W2);

    CNNSnapshot best_snap;
    if (snapshot_alloc(&best_snap, ctx.F, ctx.K, ctx.D) != 0) return -1;
    snapshot_save(&best_snap, &ctx);

    float best_val_loss = FLT_MAX;
    int   wait_count = 0;
    int   global_step = 0;

    for (int epoch = 0; epoch < max_epochs; epoch++) {
        for (int start = 0; start < n_train_act; start += batch_size) {
            int end = start + batch_size;
            if (end > n_train_act) end = n_train_act;
            int bN = end - start;

            global_step++;
            unsigned long long drop_off = (unsigned long long)global_step * 1000ULL;

            const float *bX = ctx.d_Xtrain + start * ctx.T;
            const float *bY = ctx.d_ytrain + start;

            if (forward(&ctx, cublas, bX, bN, 1, drop_off) != 0) return -1;
            if (backward(&ctx, cublas, bX, bY, bN) != 0) return -1;
            if (update_params(&ctx, global_step) != 0) return -1;
        }

        if (forward(&ctx, cublas, ctx.d_Xval, n_val_int, 0, 0) != 0) return -1;
        float vl = 0.0f;
        if (compute_loss(&ctx, cublas, ctx.d_yval, n_val_int, &vl) != 0)
            return -1;

        if (vl < best_val_loss) {
            best_val_loss = vl;
            wait_count = 0;
            snapshot_save(&best_snap, &ctx);
        } else {
            wait_count++;
            if (wait_count >= patience) break;
        }
    }

    snapshot_restore(&best_snap, &ctx);

    if (forward(&ctx, cublas, ctx.d_Xeval, n_eval, 0, 0) != 0) return -1;

    CK(cudaMemcpy(y_proba_out, ctx.Aout, n_eval * sizeof(float), cudaMemcpyDeviceToHost));
    for (int i = 0; i < n_eval; i++) y_pred_out[i] = (y_proba_out[i] >= 0.5f) ? 1.0f : 0.0f;

    CK(cudaEventRecord(t1));
    CK(cudaEventSynchronize(t1));
    float ms = 0.0f;
    CK(cudaEventElapsedTime(&ms, t0, t1));
    *train_time_out = ms / 1000.0f;
    *val_loss_out = best_val_loss;

    snapshot_free(&best_snap);
    ctx_free(&ctx);
    cublasDestroy(cublas);
    cudaEventDestroy(t0); cudaEventDestroy(t1);

    return 0;
}

extern "C"
int cnn_train_predict_batch(
    const float        *X_train_h, const float *y_train_h, int n_train,
    const float        *X_eval_h,  int n_eval,
    int                 input_dim,
    int                 n_candidates,
    const int          *n_filters,
    const int          *kernel_sizes,
    const int          *dense_neurons,
    const float        *learning_rates,
    const float        *l2_alphas,
    const float        *dropout_rates,
    const int          *batch_sizes,
    const int          *use_tanhs,
    const int          *use_adams,
    const unsigned int *seeds,
    int                 max_epochs,
    int                 patience,
    float              *y_pred_out,
    float              *y_proba_out,
    float              *train_times_out,
    float              *val_losses_out)
{
    for (int c = 0; c < n_candidates; c++) {
        int rc = cnn_train_predict(
            X_train_h, y_train_h, n_train,
            X_eval_h, n_eval,
            input_dim,
            n_filters[c],
            kernel_sizes[c],
            dense_neurons[c],
            learning_rates[c],
            l2_alphas[c],
            dropout_rates[c],
            batch_sizes[c],
            max_epochs, patience,
            use_tanhs[c],
            use_adams[c],
            seeds[c],
            y_pred_out  + c * n_eval,
            y_proba_out + c * n_eval,
            train_times_out + c,
            val_losses_out  + c
        );
        if (rc != 0) return rc;
    }
    return 0;
}
