/*
 * mlp_cuda.h — CUDA MLP Training Library
 *
 * NCA Optimizer Benchmark — GPU-accelerated MLP training.
 * Supports single-model training and a batched convenience API.
 *
 * Architecture: Input → Dense(hidden, tanh|relu) → Dropout → Dense(1, sigmoid)
 * Optimizers:   RMSProp, Adam
 * Loss:         Binary Cross-Entropy + L2 on the hidden Dense kernel
 */

#ifndef MLP_CUDA_H
#define MLP_CUDA_H

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Train a single MLP and predict on evaluation data.
 *
 * The training data is internally split: the last 15% is used as
 * mini-validation for early stopping (matching TensorFlow's validation_split=0.15).
 *
 * Returns 0 on success, -1 on error.
 */
int mlp_train_predict(
    const float *X_train,       /* [n_train x input_dim] row-major          */
    const float *y_train,       /* [n_train]                                */
    int          n_train,
    const float *X_eval,        /* [n_eval x input_dim] row-major           */
    int          n_eval,
    int          input_dim,
    int          hidden_neurons,
    float        learning_rate,
    float        l2_alpha,
    float        dropout_rate,
    int          batch_size,
    int          max_epochs,
    int          patience,      /* early-stopping patience                  */
    int          use_tanh,      /* 1 = tanh, 0 = relu                       */
    int          use_adam,      /* 1 = Adam, 0 = RMSProp                    */
    unsigned int seed,
    float       *y_pred_out,    /* [n_eval] output: 0/1 predictions         */
    float       *y_proba_out,   /* [n_eval] output: sigmoid probabilities   */
    float       *train_time_out,/* scalar: wall-clock training time (sec)   */
    float       *val_loss_out   /* scalar: best validation loss achieved    */
);

/*
 * Train N models through the CUDA backend.
 *
 * All models share the same training/eval data but use different
 * hyper-parameters. The current implementation evaluates candidates
 * sequentially to fit 4 GB GPUs reliably.
 *
 * Returns 0 on success, -1 on error.
 */
int mlp_train_predict_batch(
    const float        *X_train,        /* [n_train x input_dim]            */
    const float        *y_train,        /* [n_train]                        */
    int                 n_train,
    const float        *X_eval,         /* [n_eval x input_dim]             */
    int                 n_eval,
    int                 input_dim,
    int                 n_candidates,
    const int          *hidden_neurons, /* [n_candidates]                   */
    const float        *learning_rates, /* [n_candidates]                   */
    const float        *l2_alphas,      /* [n_candidates]                   */
    const float        *dropout_rates,  /* [n_candidates]                   */
    const int          *batch_sizes,    /* [n_candidates]                   */
    const int          *use_tanhs,      /* [n_candidates]                   */
    const int          *use_adams,      /* [n_candidates]                   */
    const unsigned int *seeds,          /* [n_candidates]                   */
    int                 max_epochs,
    int                 patience,
    float              *y_pred_out,     /* [n_candidates x n_eval]          */
    float              *y_proba_out,    /* [n_candidates x n_eval]          */
    float              *train_times_out,/* [n_candidates]                   */
    float              *val_losses_out  /* [n_candidates]                   */
);

#ifdef __cplusplus
}
#endif

#endif /* MLP_CUDA_H */
