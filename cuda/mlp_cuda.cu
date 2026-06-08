/*
 * mlp_cuda.cu — Complete MLP Training on NVIDIA GPU
 *
 * NCA Optimizer Benchmark project.
 * Full backpropagation, mini-batch SGD, RMSProp/Adam, dropout,
 * L2 regularization, early stopping.
 *
 * Supports single-model training and a sequential batched convenience API
 * for population-based optimizers (GA, PSO, DE, GWO).
 *
 * Compile:  nvcc -O3 -arch=sm_75 -Xcompiler -fPIC -shared
 *                -lcublas -lcurand -o libmlp_cuda.so mlp_cuda.cu
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

#include "mlp_cuda.h"

/* ================================================================
 *  Constants
 * ================================================================ */

#define BLOCK 256
#define EPS   1e-7f

/* ================================================================
 *  Error-checking macros
 * ================================================================ */

#define CK(call) do {                                          \
    cudaError_t e = (call);                                    \
    if (e != cudaSuccess) {                                    \
        fprintf(stderr, "CUDA  %s:%d  %s\n",                  \
                __FILE__, __LINE__, cudaGetErrorString(e));    \
        return -1;                                             \
    }                                                          \
} while (0)

#define CMALLOC(ptr, bytes) CK(cudaMalloc((void **)(ptr), (bytes)))

#define CB(call) do {                                          \
    cublasStatus_t s = (call);                                 \
    if (s != CUBLAS_STATUS_SUCCESS) {                          \
        fprintf(stderr, "cuBLAS %s:%d  status=%d\n",           \
                __FILE__, __LINE__, (int)s);                   \
        return -1;                                             \
    }                                                          \
} while (0)

#define GRID(n) (((n) + BLOCK - 1) / BLOCK)

#define KC() do {                                           \
    cudaError_t e = cudaGetLastError();                     \
    if (e != cudaSuccess) {                                 \
        fprintf(stderr, "CUDA kernel %s:%d  %s\n",          \
                __FILE__, __LINE__, cudaGetErrorString(e)); \
        return -1;                                          \
    }                                                       \
} while (0)

/* ================================================================
 *  Activation kernels
 * ================================================================ */

__global__ void k_tanh_fwd(const float *z, float *a, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) a[i] = tanhf(z[i]);
}

__global__ void k_tanh_bwd(const float *da, const float *z,
                           float *dz, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) { float t = tanhf(z[i]); dz[i] = da[i] * (1.0f - t * t); }
}

__global__ void k_relu_fwd(const float *z, float *a, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) a[i] = fmaxf(0.0f, z[i]);
}

__global__ void k_relu_bwd(const float *da, const float *z,
                           float *dz, int n) {
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

/* ================================================================
 *  Element-wise helpers
 * ================================================================ */

__global__ void k_add_bias(float *out, const float *bias,
                           int rows, int cols) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < rows * cols) out[i] += bias[i % cols];
}

__global__ void k_bias_grad(const float *dz, float *db,
                            int rows, int cols) {
    int c = blockIdx.x * BLOCK + threadIdx.x;
    if (c < cols) {
        float s = 0.0f;
        for (int r = 0; r < rows; r++) s += dz[r * cols + c];
        db[c] = s;
    }
}

__global__ void k_output_grad(const float *a, const float *y,
                              float *dz, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) dz[i] = (a[i] - y[i]) / (float)n;
}

__global__ void k_add_l2(float *dw, const float *w,
                         float alpha, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) dw[i] += 2.0f * alpha * w[i];
}

__global__ void k_threshold(const float *proba, float *pred, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) pred[i] = (proba[i] >= 0.5f) ? 1.0f : 0.0f;
}

__global__ void k_zero(float *d, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) d[i] = 0.0f;
}

/* ================================================================
 *  Dropout
 * ================================================================ */

__global__ void k_dropout_fwd(float *a, float *mask,
                              unsigned long long seed,
                              unsigned long long offset,
                              float rate, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        curandStatePhilox4_32_10_t st;
        curand_init(seed, (unsigned long long)i, offset, &st);
        float r = curand_uniform(&st);
        if (r < rate) {
            mask[i] = 0.0f;
            a[i]    = 0.0f;
        } else {
            float scale = 1.0f / (1.0f - rate);
            mask[i] = scale;
            a[i]   *= scale;
        }
    }
}

__global__ void k_dropout_bwd(float *da, const float *mask, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) da[i] *= mask[i];
}

/* ================================================================
 *  Loss (binary cross-entropy)
 * ================================================================ */

__global__ void k_bce(const float *y, const float *a,
                      float *loss, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        float p = fminf(fmaxf(a[i], EPS), 1.0f - EPS);
        loss[i] = -(y[i] * logf(p) + (1.0f - y[i]) * logf(1.0f - p));
    }
}

/* Simple sum-reduce on host after small kernel writes. */
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

/* ================================================================
 *  Optimizer kernels
 * ================================================================ */

__global__ void k_rmsprop(float *p, const float *g, float *cache,
                          float lr, float rho, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        cache[i] = rho * cache[i] + (1.0f - rho) * g[i] * g[i];
        p[i] -= lr * g[i] / (sqrtf(cache[i]) + EPS);
    }
}

__global__ void k_adam(float *p, const float *g, float *m, float *v,
                       float lr, float b1, float b2,
                       float b1t, float b2t, int n) {
    int i = blockIdx.x * BLOCK + threadIdx.x;
    if (i < n) {
        m[i] = b1 * m[i] + (1.0f - b1) * g[i];
        v[i] = b2 * v[i] + (1.0f - b2) * g[i] * g[i];
        float mh = m[i] / (1.0f - b1t);
        float vh = v[i] / (1.0f - b2t);
        p[i] -= lr * mh / (sqrtf(vh) + EPS);
    }
}

/* ================================================================
 *  cuBLAS row-major matmul helpers
 *
 *  For row-major C = A[m,k] @ B[k,n]:
 *    cublasSgemm(h, N, N, n, m, k, &a, B, n, A, k, &b, C, n)
 *
 *  For row-major C = A^T[k,m] @ B[k,n]  (i.e. A is [m,k], we want A^T @ B):
 *    cublasSgemm(h, N, T, n, m, k, &a, B, n, A, k, &b, C, n)
 *    but really m and k swap roles... let me be more careful.
 *
 * ================================================================ */

/* C[m,n] = A[m,k] @ B[k,n]   all row-major */
static inline cublasStatus_t matmul(cublasHandle_t h,
    const float *A, const float *B, float *C,
    int m, int k, int n, float alpha, float beta)
{
    return cublasSgemm(h, CUBLAS_OP_N, CUBLAS_OP_N,
                       n, m, k, &alpha, B, n, A, k, &beta, C, n);
}

/* C[k,n] = A[m,k]^T @ B[m,n]   all row-major */
static inline cublasStatus_t matmul_atb(cublasHandle_t h,
    const float *A, const float *B, float *C,
    int m, int k, int n, float alpha, float beta)
{
    /* A^T @ B  in row-major:
       In col-major view: C_col[n,k] = B_col[n,m] @ A_col[m,k]
       cublasSgemm(h, N, N, k, n, m, &alpha, A, k, B, n, &beta, C, k)
       Wait, let me think again...
       
       Row-major A[m,k] is col-major A'[k,m].
       Row-major B[m,n] is col-major B'[n,m].
       We want C = A^T @ B = [k,m] @ [m,n] = [k,n] row-major.
       Col-major C'[n,k].
       
       C' = B' @ A (where A is the col-major storage of row-major A)
       cublasSgemm(h, N, N, k, n, m, alpha, A_ptr, k, B_ptr, n, beta, C_ptr, k)
       
       Nope. Let me use the transposed approach:
       cublasSgemm computes: C_cm = alpha * op(A_cm) * op(B_cm) + beta * C_cm
       with ldA, ldB, ldC.
       
       We have row-major A[m,k] stored as A_rm. In column-major, this is A^T[k,m].
       We have row-major B[m,n] stored as B_rm. In column-major, this is B^T[n,m].
       
       We want: C_rm[k,n] = A_rm^T @ B_rm (row-major multiply)
       Equivalently: C_cm[n,k] = B_cm @ A_cm^T  ... hmm
       
       Actually, the simplest approach:
       C[k,n] = A^T[k,m] @ B[m,n]  all row-major
       = (B^T[n,m] @ A[m,k])^T ... no, that doesn't help.
       
       Let me just use: cublasSgemm(h, N, T, n, k, m, alpha, B_ptr, n, A_ptr, k, beta, C_ptr, n)
       This computes C_cm[n,k] = B_cm[n,m] * A_cm^T[m,k]
       B_cm is B_rm viewed as col-major = B^T, but B_rm[m,n] col-major is [n,m].
       A_cm^T: A_rm[m,k] is col-major [k,m], transposing gives [m,k].
       
       C_cm[n,k] = [n,m] * [m,k] = [n,k]. But col-major [n,k] = row-major [k,n]. ✓
    */
    return cublasSgemm(h, CUBLAS_OP_N, CUBLAS_OP_T,
                       n, k, m, &alpha, B, n, A, k, &beta, C, n);
}

/* C[m,n] = A[m,k] @ B^T[n,k]   all row-major */
static inline cublasStatus_t matmul_abt(cublasHandle_t h,
    const float *A, const float *B, float *C,
    int m, int k, int n, float alpha, float beta)
{
    /* We want C[m,n] = A[m,k] @ B^T[k,n] where B is [n,k].
       Col-major view:
       A_rm[m,k] → col [k,m]
       B_rm[n,k] → col [k,n]
       C_rm[m,n] → col [n,m]
       
       C_col[n,m] = B_col[k,n]^T * A_col[k,m]
       = B^T_col[n,k] * A_col[k,m] → need CUBLAS_OP_T on first, CUBLAS_OP_N on second
       
       cublasSgemm(h, T, N, ??? )
       cublasSgemm: C = alpha * op(A) * op(B) + beta * C
       with C[M,N], op(A)[M,K], op(B)[K,N] in col-major.
       
       We need: C_col[n,m] = B_col^T[n,k] * A_col[k,m]
       M=n, N=m, K=k
       op(A_blas) = B_col^T → A_blas = B_col with CUBLAS_OP_T, ldA = k
       op(B_blas) = A_col   → B_blas = A_col with CUBLAS_OP_N, ldB = k
       
       cublasSgemm(h, CUBLAS_OP_T, CUBLAS_OP_N, n, m, k, &alpha, B, k, A, k, &beta, C, n)
    */
    return cublasSgemm(h, CUBLAS_OP_T, CUBLAS_OP_N,
                       n, m, k, &alpha, B, k, A, k, &beta, C, n);
}

/* ================================================================
 *  Xavier weight initialization (host)
 * ================================================================ */

static void xavier_init(float *buf, int fan_in, int fan_out,
                        unsigned int seed) {
    float limit = sqrtf(6.0f / (float)(fan_in + fan_out));
    srand(seed);
    for (int i = 0; i < fan_in * fan_out; i++)
        buf[i] = ((float)rand() / (float)RAND_MAX) * 2.0f * limit - limit;
}

/* ================================================================
 *  Internal: train one MLP
 * ================================================================ */

typedef struct {
    /* Weights on device */
    float *W1, *b1, *W2, *b2;
    /* Optimizer state */
    float *cW1, *cb1, *cW2, *cb2;   /* RMSProp cache or Adam m */
    float *vW1, *vb1, *vW2, *vb2;   /* Adam v (unused for RMSProp) */
    /* Gradients */
    float *dW1, *db1, *dW2, *db2;
    /* Activations & intermediates */
    float *Z1, *A1, *mask, *Z2, *A2;
    /* Backward temps */
    float *dZ2, *dA1, *dZ1;
    /* Loss scratch */
    float *loss_buf;
    /* Data pointers on device */
    float *d_Xtrain, *d_ytrain, *d_Xval, *d_yval, *d_Xeval;
    /* Dimensions */
    int input_dim, hidden, n_train_actual, n_val_internal, n_eval;
    int batch_size, max_epochs, patience;
    float lr, l2, dropout;
    int use_tanh, use_adam;
    unsigned int seed;
} MLPContext;

static int ctx_alloc(MLPContext *ctx, int max_batch) {
    int H = ctx->hidden;
    int D = ctx->input_dim;
    int B = max_batch;  /* largest buffer needed */
    int NV = ctx->n_val_internal;
    int NE = ctx->n_eval;
    int max_samples = B;
    if (NV > max_samples) max_samples = NV;
    if (NE > max_samples) max_samples = NE;
    /* Use max_samples for activation buffers */
    int abuf = max_samples;

    /* Weights */
    CMALLOC(&ctx->W1, D * H * sizeof(float));
    CMALLOC(&ctx->b1, H * sizeof(float));
    CMALLOC(&ctx->W2, H * sizeof(float));   /* H x 1 */
    CMALLOC(&ctx->b2, sizeof(float));

    /* Gradients */
    CMALLOC(&ctx->dW1, D * H * sizeof(float));
    CMALLOC(&ctx->db1, H * sizeof(float));
    CMALLOC(&ctx->dW2, H * sizeof(float));
    CMALLOC(&ctx->db2, sizeof(float));

    /* Optimizer state */
    CMALLOC(&ctx->cW1, D * H * sizeof(float));
    CMALLOC(&ctx->cb1, H * sizeof(float));
    CMALLOC(&ctx->cW2, H * sizeof(float));
    CMALLOC(&ctx->cb2, sizeof(float));
    CK(cudaMemset(ctx->cW1, 0, D * H * sizeof(float)));
    CK(cudaMemset(ctx->cb1, 0, H * sizeof(float)));
    CK(cudaMemset(ctx->cW2, 0, H * sizeof(float)));
    CK(cudaMemset(ctx->cb2, 0, sizeof(float)));

    if (ctx->use_adam) {
        CMALLOC(&ctx->vW1, D * H * sizeof(float));
        CMALLOC(&ctx->vb1, H * sizeof(float));
        CMALLOC(&ctx->vW2, H * sizeof(float));
        CMALLOC(&ctx->vb2, sizeof(float));
        CK(cudaMemset(ctx->vW1, 0, D * H * sizeof(float)));
        CK(cudaMemset(ctx->vb1, 0, H * sizeof(float)));
        CK(cudaMemset(ctx->vW2, 0, H * sizeof(float)));
        CK(cudaMemset(ctx->vb2, 0, sizeof(float)));
    } else {
        ctx->vW1 = ctx->vb1 = ctx->vW2 = ctx->vb2 = NULL;
    }

    /* Activation buffers (sized for largest pass) */
    CMALLOC(&ctx->Z1,   abuf * H * sizeof(float));
    CMALLOC(&ctx->A1,   abuf * H * sizeof(float));
    CMALLOC(&ctx->mask, abuf * H * sizeof(float));
    CMALLOC(&ctx->Z2,   abuf * sizeof(float));
    CMALLOC(&ctx->A2,   abuf * sizeof(float));
    CMALLOC(&ctx->dZ2,  abuf * sizeof(float));
    CMALLOC(&ctx->dA1,  abuf * H * sizeof(float));
    CMALLOC(&ctx->dZ1,  abuf * H * sizeof(float));
    CMALLOC(&ctx->loss_buf, abuf * sizeof(float));

    return 0;
}

static void ctx_free(MLPContext *ctx) {
    cudaFree(ctx->W1);  cudaFree(ctx->b1);
    cudaFree(ctx->W2);  cudaFree(ctx->b2);
    cudaFree(ctx->dW1); cudaFree(ctx->db1);
    cudaFree(ctx->dW2); cudaFree(ctx->db2);
    cudaFree(ctx->cW1); cudaFree(ctx->cb1);
    cudaFree(ctx->cW2); cudaFree(ctx->cb2);
    if (ctx->vW1) { cudaFree(ctx->vW1); cudaFree(ctx->vb1);
                     cudaFree(ctx->vW2); cudaFree(ctx->vb2); }
    cudaFree(ctx->Z1);  cudaFree(ctx->A1);  cudaFree(ctx->mask);
    cudaFree(ctx->Z2);  cudaFree(ctx->A2);
    cudaFree(ctx->dZ2); cudaFree(ctx->dA1); cudaFree(ctx->dZ1);
    cudaFree(ctx->loss_buf);
    cudaFree(ctx->d_Xtrain); cudaFree(ctx->d_ytrain);
    cudaFree(ctx->d_Xval);   cudaFree(ctx->d_yval);
    cudaFree(ctx->d_Xeval);
}

/* Forward pass on a batch of N samples.
   X is already on device at d_X[N, D].  */
static int forward(MLPContext *ctx, cublasHandle_t cublas,
                   const float *d_X, int N, int training,
                   unsigned long long dropout_offset) {
    int D = ctx->input_dim, H = ctx->hidden;

    /* Z1[N,H] = X[N,D] @ W1[D,H] */
    CB(matmul(cublas, d_X, ctx->W1, ctx->Z1, N, D, H, 1.0f, 0.0f));
    /* Z1 += b1 */
    k_add_bias<<<GRID(N * H), BLOCK>>>(ctx->Z1, ctx->b1, N, H);
    KC();

    /* A1 = activation(Z1) */
    int nH = N * H;
    if (ctx->use_tanh)
        k_tanh_fwd<<<GRID(nH), BLOCK>>>(ctx->Z1, ctx->A1, nH);
    else
        k_relu_fwd<<<GRID(nH), BLOCK>>>(ctx->Z1, ctx->A1, nH);
    KC();

    /* Dropout (training only) */
    if (training && ctx->dropout > 0.0f) {
        k_dropout_fwd<<<GRID(nH), BLOCK>>>(
            ctx->A1, ctx->mask, ctx->seed + 777ULL,
            dropout_offset, ctx->dropout, nH);
        KC();
    }

    /* Z2[N,1] = A1[N,H] @ W2[H,1] */
    CB(matmul(cublas, ctx->A1, ctx->W2, ctx->Z2, N, H, 1, 1.0f, 0.0f));
    /* Z2 += b2 */
    k_add_bias<<<GRID(N), BLOCK>>>(ctx->Z2, ctx->b2, N, 1);
    KC();

    /* A2 = sigmoid(Z2) */
    k_sigmoid<<<GRID(N), BLOCK>>>(ctx->Z2, ctx->A2, N);
    KC();

    return 0;
}

/* Backward pass on a mini-batch.  Must call forward() first. */
static int backward(MLPContext *ctx, cublasHandle_t cublas,
                    const float *d_X, const float *d_y, int N) {
    int D = ctx->input_dim, H = ctx->hidden;
    int nH = N * H;

    /* dZ2 = (A2 - y) / N */
    k_output_grad<<<GRID(N), BLOCK>>>(ctx->A2, d_y, ctx->dZ2, N);
    KC();

    /* dW2[H,1] = A1^T[H,N] @ dZ2[N,1] */
    CB(matmul_atb(cublas, ctx->A1, ctx->dZ2, ctx->dW2,
                  N, H, 1, 1.0f, 0.0f));
    /* db2 = sum(dZ2); dZ2 is already scaled by 1/N */
    k_bias_grad<<<GRID(1), BLOCK>>>(ctx->dZ2, ctx->db2, N, 1);
    KC();

    /* dA1[N,H] = dZ2[N,1] @ W2^T[1,H] */
    CB(matmul_abt(cublas, ctx->dZ2, ctx->W2, ctx->dA1,
                  N, 1, H, 1.0f, 0.0f));

    /* Dropout backward */
    if (ctx->dropout > 0.0f) {
        k_dropout_bwd<<<GRID(nH), BLOCK>>>(ctx->dA1, ctx->mask, nH);
        KC();
    }

    /* dZ1 = dA1 * activation'(Z1) */
    if (ctx->use_tanh)
        k_tanh_bwd<<<GRID(nH), BLOCK>>>(ctx->dA1, ctx->Z1, ctx->dZ1, nH);
    else
        k_relu_bwd<<<GRID(nH), BLOCK>>>(ctx->dA1, ctx->Z1, ctx->dZ1, nH);
    KC();

    /* dW1[D,H] = X^T[D,N] @ dZ1[N,H] */
    CB(matmul_atb(cublas, d_X, ctx->dZ1, ctx->dW1,
                  N, D, H, 1.0f, 0.0f));
    /* db1 = sum(dZ1); dZ1 is already scaled by 1/N */
    k_bias_grad<<<GRID(H), BLOCK>>>(ctx->dZ1, ctx->db1, N, H);
    KC();

    /* Keras model applies L2 only to the hidden Dense kernel. */
    if (ctx->l2 > 0.0f) {
        k_add_l2<<<GRID(D * H), BLOCK>>>(ctx->dW1, ctx->W1, ctx->l2, D * H);
        KC();
    }

    return 0;
}

/* Apply optimizer update to all parameters. */
static int update_params(MLPContext *ctx, int step) {
    int D = ctx->input_dim, H = ctx->hidden;

    if (ctx->use_adam) {
        float b1 = 0.9f, b2 = 0.999f;
        float b1t = powf(b1, (float)step);
        float b2t = powf(b2, (float)step);
        k_adam<<<GRID(D*H), BLOCK>>>(ctx->W1, ctx->dW1, ctx->cW1, ctx->vW1,
                                      ctx->lr, b1, b2, b1t, b2t, D*H);
        k_adam<<<GRID(H), BLOCK>>>(ctx->b1, ctx->db1, ctx->cb1, ctx->vb1,
                                    ctx->lr, b1, b2, b1t, b2t, H);
        k_adam<<<GRID(H), BLOCK>>>(ctx->W2, ctx->dW2, ctx->cW2, ctx->vW2,
                                    ctx->lr, b1, b2, b1t, b2t, H);
        k_adam<<<GRID(1), BLOCK>>>(ctx->b2, ctx->db2, ctx->cb2, ctx->vb2,
                                    ctx->lr, b1, b2, b1t, b2t, 1);
        KC();
    } else {
        float rho = 0.9f;
        k_rmsprop<<<GRID(D*H), BLOCK>>>(ctx->W1, ctx->dW1, ctx->cW1,
                                          ctx->lr, rho, D*H);
        k_rmsprop<<<GRID(H), BLOCK>>>(ctx->b1, ctx->db1, ctx->cb1,
                                        ctx->lr, rho, H);
        k_rmsprop<<<GRID(H), BLOCK>>>(ctx->W2, ctx->dW2, ctx->cW2,
                                        ctx->lr, rho, H);
        k_rmsprop<<<GRID(1), BLOCK>>>(ctx->b2, ctx->db2, ctx->cb2,
                                        ctx->lr, rho, 1);
        KC();
    }
    return 0;
}

/* Compute validation loss on device data d_y[N]. Must call forward() first. */
static int compute_loss(MLPContext *ctx, cublasHandle_t cublas,
                        const float *d_y, int N, float *loss_out) {
    if (loss_out == NULL) return -1;
    k_bce<<<GRID(N), BLOCK>>>(d_y, ctx->A2, ctx->loss_buf, N);
    KC();
    CK(cudaDeviceSynchronize());

    float bce_sum = 0.0f;
    if (reduce_sum_host(ctx->loss_buf, N, &bce_sum) != 0)
        return -1;

    float reg = 0.0f;
    if (ctx->l2 > 0.0f) {
        float w1_sq = 0.0f;
        CB(cublasSdot(cublas, ctx->input_dim * ctx->hidden,
                      ctx->W1, 1, ctx->W1, 1, &w1_sq));
        reg = ctx->l2 * w1_sq;
    }

    *loss_out = bce_sum / (float)N + reg;
    return 0;
}

/* ================================================================
 *  Copy best weights (for early stopping restore)
 * ================================================================ */

typedef struct {
    float *W1, *b1, *W2, *b2;
    int D, H;
} WeightSnapshot;

static int snapshot_alloc(WeightSnapshot *snap, int D, int H) {
    snap->D = D; snap->H = H;
    CMALLOC(&snap->W1, D * H * sizeof(float));
    CMALLOC(&snap->b1, H * sizeof(float));
    CMALLOC(&snap->W2, H * sizeof(float));
    CMALLOC(&snap->b2, sizeof(float));
    return 0;
}

static void snapshot_save(WeightSnapshot *snap, MLPContext *ctx) {
    int D = snap->D, H = snap->H;
    cudaMemcpy(snap->W1, ctx->W1, D*H*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->b1, ctx->b1, H*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->W2, ctx->W2, H*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(snap->b2, ctx->b2, sizeof(float), cudaMemcpyDeviceToDevice);
}

static void snapshot_restore(WeightSnapshot *snap, MLPContext *ctx) {
    int D = snap->D, H = snap->H;
    cudaMemcpy(ctx->W1, snap->W1, D*H*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->b1, snap->b1, H*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->W2, snap->W2, H*sizeof(float), cudaMemcpyDeviceToDevice);
    cudaMemcpy(ctx->b2, snap->b2, sizeof(float), cudaMemcpyDeviceToDevice);
}

static void snapshot_free(WeightSnapshot *snap) {
    cudaFree(snap->W1); cudaFree(snap->b1);
    cudaFree(snap->W2); cudaFree(snap->b2);
}

/* ================================================================
 *  PUBLIC: Train single MLP
 * ================================================================ */

extern "C"
int mlp_train_predict(
    const float *X_train_h, const float *y_train_h, int n_train,
    const float *X_eval_h,  int n_eval,
    int input_dim, int hidden_neurons,
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
        hidden_neurons < 1 || batch_size < 1 || max_epochs < 1 ||
        patience < 0 || learning_rate <= 0.0f || l2_alpha < 0.0f ||
        dropout_rate < 0.0f || dropout_rate >= 1.0f) {
        fprintf(stderr, "Invalid MLP CUDA training arguments\n");
        return -1;
    }

    /* ---- Internal train/val split (last 15% for early stopping) ---- */
    int n_val_int = (int)(0.15f * (float)n_train);
    if (n_val_int < 1) n_val_int = 1;
    int n_train_act = n_train - n_val_int;

    /* ---- Timing ---- */
    cudaEvent_t t0, t1;
    CK(cudaEventCreate(&t0));
    CK(cudaEventCreate(&t1));
    CK(cudaEventRecord(t0));

    /* ---- cuBLAS handle ---- */
    cublasHandle_t cublas;
    CB(cublasCreate(&cublas));

    /* ---- Build context ---- */
    MLPContext ctx;
    memset(&ctx, 0, sizeof(ctx));
    ctx.input_dim = input_dim;
    ctx.hidden = hidden_neurons;
    ctx.n_train_actual = n_train_act;
    ctx.n_val_internal = n_val_int;
    ctx.n_eval = n_eval;
    ctx.batch_size = batch_size;
    ctx.max_epochs = max_epochs;
    ctx.patience = patience;
    ctx.lr = learning_rate;
    ctx.l2 = l2_alpha;
    ctx.dropout = dropout_rate;
    ctx.use_tanh = use_tanh;
    ctx.use_adam = use_adam;
    ctx.seed = seed;

    int max_batch = batch_size;
    if (n_val_int > max_batch) max_batch = n_val_int;
    if (n_eval > max_batch) max_batch = n_eval;

    if (ctx_alloc(&ctx, max_batch) != 0) return -1;

    /* ---- Copy data to device ---- */
    int D = input_dim;
    CMALLOC(&ctx.d_Xtrain, n_train_act * D * sizeof(float));
    CMALLOC(&ctx.d_ytrain, n_train_act * sizeof(float));
    CMALLOC(&ctx.d_Xval,   n_val_int * D * sizeof(float));
    CMALLOC(&ctx.d_yval,   n_val_int * sizeof(float));
    CMALLOC(&ctx.d_Xeval,  n_eval * D * sizeof(float));

    CK(cudaMemcpy(ctx.d_Xtrain, X_train_h,
                   n_train_act * D * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_ytrain, y_train_h,
                   n_train_act * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_Xval, X_train_h + n_train_act * D,
                   n_val_int * D * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_yval, y_train_h + n_train_act,
                   n_val_int * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.d_Xeval, X_eval_h,
                   n_eval * D * sizeof(float), cudaMemcpyHostToDevice));

    /* ---- Init weights ---- */
    int H = hidden_neurons;
    float *h_W1 = (float *)malloc(D * H * sizeof(float));
    float *h_b1 = (float *)calloc(H, sizeof(float));
    float *h_W2 = (float *)malloc(H * sizeof(float));
    float  h_b2 = 0.0f;
    if (h_W1 == NULL || h_b1 == NULL || h_W2 == NULL) {
        fprintf(stderr, "Host allocation failed during MLP initialization\n");
        free(h_W1); free(h_b1); free(h_W2);
        return -1;
    }

    xavier_init(h_W1, D, H, seed);
    xavier_init(h_W2, H, 1, seed + 1);

    CK(cudaMemcpy(ctx.W1, h_W1, D * H * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.b1, h_b1, H * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.W2, h_W2, H * sizeof(float), cudaMemcpyHostToDevice));
    CK(cudaMemcpy(ctx.b2, &h_b2, sizeof(float), cudaMemcpyHostToDevice));
    free(h_W1); free(h_b1); free(h_W2);

    /* ---- Early stopping setup ---- */
    WeightSnapshot best_snap;
    if (snapshot_alloc(&best_snap, D, H) != 0) return -1;
    snapshot_save(&best_snap, &ctx);

    float best_val_loss = FLT_MAX;
    int   wait_count = 0;
    int   global_step = 0;

    /* ---- Training loop ---- */
    for (int epoch = 0; epoch < max_epochs; epoch++) {
        /* Mini-batch iteration (no shuffle, matching TF shuffle=False) */
        for (int start = 0; start < n_train_act; start += batch_size) {
            int end = start + batch_size;
            if (end > n_train_act) end = n_train_act;
            int bN = end - start;

            global_step++;
            unsigned long long drop_off = (unsigned long long)global_step * 1000ULL;

            const float *bX = ctx.d_Xtrain + start * D;
            const float *bY = ctx.d_ytrain + start;

            if (forward(&ctx, cublas, bX, bN, 1, drop_off) != 0) return -1;
            if (backward(&ctx, cublas, bX, bY, bN) != 0) return -1;
            if (update_params(&ctx, global_step) != 0) return -1;
        }

        /* Validation loss for early stopping */
        if (forward(&ctx, cublas, ctx.d_Xval, n_val_int, 0, 0) != 0)
            return -1;
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

    /* Restore best weights */
    snapshot_restore(&best_snap, &ctx);

    /* ---- Predict on eval data ---- */
    if (forward(&ctx, cublas, ctx.d_Xeval, n_eval, 0, 0) != 0) return -1;

    /* Copy probabilities to host */
    CK(cudaMemcpy(y_proba_out, ctx.A2, n_eval * sizeof(float),
                   cudaMemcpyDeviceToHost));

    /* Threshold on host */
    for (int i = 0; i < n_eval; i++)
        y_pred_out[i] = (y_proba_out[i] >= 0.5f) ? 1.0f : 0.0f;

    /* ---- Timing ---- */
    CK(cudaEventRecord(t1));
    CK(cudaEventSynchronize(t1));
    float ms = 0.0f;
    CK(cudaEventElapsedTime(&ms, t0, t1));
    *train_time_out = ms / 1000.0f;
    *val_loss_out = best_val_loss;

    /* ---- Cleanup ---- */
    snapshot_free(&best_snap);
    ctx_free(&ctx);
    cublasDestroy(cublas);
    cudaEventDestroy(t0);
    cudaEventDestroy(t1);

    return 0;
}

/* ================================================================
 *  PUBLIC: Batch-train N models sequentially through the CUDA backend
 * ================================================================ */

extern "C"
int mlp_train_predict_batch(
    const float        *X_train_h, const float *y_train_h, int n_train,
    const float        *X_eval_h,  int n_eval,
    int                 input_dim,
    int                 n_candidates,
    const int          *hidden_neurons,
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
    /*
     * For simplicity and reliability on the GTX 1650 (4 GB),
     * candidates are evaluated sequentially. A future version can
     * factor out data uploads and use separate streams for overlap.
     */
    for (int c = 0; c < n_candidates; c++) {
        int rc = mlp_train_predict(
            X_train_h, y_train_h, n_train,
            X_eval_h, n_eval,
            input_dim,
            hidden_neurons[c],
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
            &train_times_out[c],
            &val_losses_out[c]
        );
        if (rc != 0) {
            fprintf(stderr, "Candidate %d/%d failed\n", c+1, n_candidates);
            return -1;
        }
    }
    return 0;
}
