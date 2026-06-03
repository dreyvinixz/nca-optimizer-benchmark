# Implementation Audit

## 1. Data flow
The data flow is robustly handled and decoupled. Data is loaded from `merged_output.csv`, mapped (e.g., `downtrend: 0`, `uptrend: 1`), and filtered for the predefined `InfoGain_7` features. It is then passed to `make_temporal_split`, which creates `TemporalSplit` data structures for train, validation, and test sets. The optimizers receive this structure and iteratively call the central `evaluate_candidate` function, which trains the model on `train` and scores it on `validation`. Once the best candidate is found, `evaluate_best_on_test` retrains the model on `train + validation` and scores on the `test` set.

## 2. Temporal split
The `temporal_split.py` module strictly enforces a chronological split. The dataset is explicitly sorted by the `datetime_column` and sliced linearly. The split proportions defined in `experiment_config.yaml` are:
- Train: 60%
- Validation: 20%
- Test: 20%
There is **no shuffle** applied to the data, ensuring that the time series integrity is preserved and future data does not leak into the training past.

## 3. Feature selection
The `InfoGain_7` feature selection is implemented via hardcoded predefined indices (`[30, 52, 31, 53, 42, 33, 41]`) specified in `experiment_config.yaml`. Since the indices are provided a priori from the historical study, no feature selection algorithm is executed during the pipeline. This perfectly eliminates any risk of test-set leakage regarding the feature selection process.

## 4. Preprocessing
In `src/models/mlp.py` (`fit_predict_mlp`), preprocessing is correctly isolated. A `StandardScaler` is initialized and `fit_transform` is called **only on the training data (`X_train`)**. The evaluation data (`X_eval`, which represents validation or test depending on the phase) is purely transformed using `scaler.transform(X_eval)`. This guarantees zero data leakage from the scaler.

## 5. Objective function
The objective function is universally shared by all optimizers through `src/objective.py`. The fitness score is computed exactly as required:
```python
fitness = weights["mcc_weight"] * metrics["mcc"] + weights["f1_weight"] * metrics["f1"]
```
Given the `experiment_config.yaml` weights, this evaluates exactly to `0.60 * MCC + 0.40 * F1`.

## 6. Optimizer budget
The computational budget is strictly equalized to 100 candidate evaluations per seed for every optimizer:
- **Random Search:** 100 evaluations (explicitly `evaluations_per_seed: 100`).
- **Genetic Algorithm (GA):** Population of 10 × 10 Generations = 100 evaluations.
- **Particle Swarm Optimization (PSO):** 10 Particles × 10 Iterations = 100 evaluations.

## 7. Reproducibility
Randomness is tightly controlled. `experiment_config.yaml` defines 5 fixed seeds: `[42, 123, 2024, 2025, 777]`.
- Each optimizer initializes its own `numpy.random.default_rng(seed)`.
- The `evaluate_candidate` function shifts the seed per evaluation (`seed + evaluation_id`) and passes it to the MLP.
- Inside `src/models/mlp.py`, `set_global_seed(seed)` is called to freeze Python's `random`, `numpy`, and `tensorflow` states.
All results, candidates, and convergence history per seed are saved to disk.

## 8. Backend
The model fallback in `src/models/mlp.py` attempts to load **TensorFlow** first. If it is unavailable, it gracefully falls back to a **NumPy** implementation (`numpy_mlp`). 
**Critical Warning:** The NumPy fallback behaves essentially as an Extreme Learning Machine (ELM). It assigns random fixed weights to the hidden layer and solves the output layer weights analytically via Ridge Regression. While this is fast and prevents the pipeline from crashing, **it does not backpropagate errors to hidden layers**. 

## 9. Outputs
The pipeline generates comprehensive CSV logs:
- `outputs/metrics/{optimizer}_runs.csv`: Logs every candidate evaluation, showing hyperparameters, validation metrics, and runtime.
- `outputs/metrics/{optimizer}_best_by_seed.csv`: Logs the best model per seed, showing test-set metrics and runtime.
- `outputs/predictions/{optimizer}_predictions.csv`: Logs raw test-set predictions (true label, predicted label, and probability).
- `outputs/metrics/convergence/{optimizer}_convergence.csv`: Logs convergence trajectories (`best_fitness_so_far` and `mean_fitness_so_far`) across evaluations.
- `outputs/tables/optimizer_comparison.csv`: Summary of metrics for comparison scripts.

## 10. Known limitations
1. **NumPy MLP Fallback:** The `numpy_mlp` is not a true Multi-Layer Perceptron since it doesn't optimize hidden weights via backpropagation. For a rigorous NCA benchmark on neural network optimization, **TensorFlow must be installed**. Relying on the NumPy fallback alters the scientific interpretation of the experiment.
2. **Hardcoded InfoGain:** While avoiding leakage, the feature mask is not dynamically selected during the fold. Expanding the benchmark to new datasets will require dynamic feature selection to be implemented correctly within the training loop.
3. **Hyperparameter Ranges:** Some optimizer boundaries, like batch size being treated as a continuous variable mapped to categorical indices in GA/PSO, may cause rounding artifacts and could be better modeled with customized discrete handlers in the future.
