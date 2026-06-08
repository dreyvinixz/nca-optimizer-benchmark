/*
 * cnn_cuda.h — CUDA CNN-1D Training Library
 *
 * NCA Optimizer Benchmark
 *
 * Architecture: Input[N, T] -> Conv1D(F, K) -> GlobalMaxPool1D -> Dense(D) -> Dropout -> Dense(1)
 */

#ifndef CNN_CUDA_H
#define CNN_CUDA_H

#ifdef __cplusplus
extern "C" {
#endif

int cnn_train_predict(
    const float *X_train,
    const float *y_train,
    int          n_train,
    const float *X_eval,
    int          n_eval,
    int          input_dim,
    int          n_filters,
    int          kernel_size,
    int          dense_neurons,
    float        learning_rate,
    float        l2_alpha,
    float        dropout_rate,
    int          batch_size,
    int          max_epochs,
    int          patience,
    int          use_tanh,
    int          use_adam,
    unsigned int seed,
    float       *y_pred_out,
    float       *y_proba_out,
    float       *train_time_out,
    float       *val_loss_out
);

int cnn_train_predict_batch(
    const float        *X_train,
    const float        *y_train,
    int                 n_train,
    const float        *X_eval,
    int                 n_eval,
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
    float              *val_losses_out
);

#ifdef __cplusplus
}
#endif

#endif /* CNN_CUDA_H */
