# Structural Optimizer/Activation Validation

Date: 2026-06-08

## Purpose

This validation run compares the internal neural training choices that will be fixed before the official optimizer benchmark:

- Optimizer: Adam vs RMSProp
- Hidden activation: ReLU vs Tanh
- Models: MLP CUDA and CNN CUDA

The goal is to choose a defensible default optimizer/activation pair without using the official test split.

## Dataset And Protocol

- Dataset: `data/raw/merged_output.csv`
- Feature set: `InfoGain_7`
- Feature indices: `[30, 52, 31, 53, 42, 33, 41]`
- Temporal split:
  - Train: 60%
  - Validation: 20%
  - Test: 20%
  - Shuffle: false
- Shapes after preprocessing:
  - Train: `(9034, 7)`
  - Validation: `(3011, 7)`
  - Test: `(3012, 7)`

Only the train and validation splits were used for this structural decision. The test split remains untouched for the official benchmark.

## Training Configuration

The run used the same neural training settings configured for the official benchmark:

- Backend: CUDA
- Loss: binary cross-entropy
- Output activation: sigmoid
- Max epochs: `10`
- Early stopping patience: `3`
- Validation metric: `val_loss`
- Objective fitness: `0.60 * MCC + 0.40 * F1`

The tested hyperparameter search spaces were the official spaces in `config/search_spaces.yaml`.

### MLP Space

- `hidden_neurons`: integer, 5 to 500
- `learning_rate`: float, `1e-8` to `1e-2`, log10 scale
- `l2_alpha`: float, `1e-8` to `1e-2`, log10 scale
- `dropout_rate`: float, 0.0 to 0.10
- `batch_size`: categorical, `[16, 32, 64, 80, 112, 128]`

### CNN Space

- `n_filters`: integer, 8 to 128
- `kernel_size`: integer, 2 to 5
- `dense_neurons`: integer, 16 to 256
- `learning_rate`: float, `1e-8` to `1e-2`, log10 scale
- `l2_alpha`: float, `1e-8` to `1e-2`, log10 scale
- `dropout_rate`: float, 0.0 to 0.10
- `batch_size`: categorical, `[16, 32, 64, 80, 112, 128]`

## Fairness Controls

The test is fair for selecting optimizer/activation because:

- Every structural combination was evaluated on the same dataset split.
- Every combination used the same official training budget per candidate.
- Every combination used the same official hyperparameter search space for its model.
- For each model and seed, candidate pools were generated once and reused across Adam/ReLU, Adam/Tanh, RMSProp/ReLU, and RMSProp/Tanh. This isolates the optimizer/activation effect from random hyperparameter sampling noise.
- The test used three random seeds: `1`, `2`, and `3`.
- Each combination received `300` evaluations: `3 seeds * 100 candidates`.
- The official test split was not touched.

## Results

| Model | Optimizer | Activation | OK | Fail | NaN/Inf | Seed Wins | Best Fitness | Mean Fitness | Top 10% Mean |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| MLP | RMSProp | Tanh | 300 | 0 | 0 | 3 | 0.428606 | 0.324621 | 0.421801 |
| MLP | Adam | Tanh | 300 | 0 | 0 | 0 | 0.426415 | 0.323514 | 0.418650 |
| MLP | RMSProp | ReLU | 300 | 0 | 0 | 0 | 0.422895 | 0.311166 | 0.415695 |
| MLP | Adam | ReLU | 300 | 0 | 0 | 0 | 0.415924 | 0.310579 | 0.411437 |
| CNN | RMSProp | Tanh | 300 | 0 | 0 | 2 | 0.409978 | 0.318803 | 0.400567 |
| CNN | Adam | Tanh | 300 | 0 | 0 | 0 | 0.403912 | 0.318849 | 0.400056 |
| CNN | RMSProp | ReLU | 300 | 0 | 0 | 1 | 0.405742 | 0.299246 | 0.400589 |
| CNN | Adam | ReLU | 300 | 0 | 0 | 0 | 0.403122 | 0.300509 | 0.399067 |

## Recommendation

Use `RMSProp + Tanh` as the fixed neural optimizer/activation configuration for the official benchmark.

Rationale:

- It was the strongest MLP configuration by best fitness, mean fitness, top-10% mean fitness, and seed wins.
- It was also the strongest CNN configuration by best fitness and seed wins, while being practically tied with Adam/Tanh on mean fitness.
- It produced no failures and no non-finite outputs in `2400` CUDA evaluations.
- It matches the original MLP-oriented configuration already present in `config/experiment_config.yaml`.

## Article Defensibility

This run is defensible as a pre-registered structural validation or pilot selection step, not as a replacement for the official benchmark.

A concise article-safe wording would be:

> Before running the official optimizer comparison, we fixed the neural optimizer and activation through a validation-only structural pilot. Adam and RMSProp were crossed with ReLU and Tanh for both CUDA MLP and CUDA CNN models. For each model and random seed, the same sampled hyperparameter candidates were reused across all four structural combinations, using the official hyperparameter ranges, temporal train/validation split, early stopping protocol, and validation fitness function. The test split was not used. RMSProp with Tanh achieved the strongest or tied-strongest validation performance across models and was therefore selected as the fixed neural training configuration for the official optimizer benchmark.

## Limitations

- This is a pilot structural selection, not the final official result.
- It uses validation performance only, intentionally avoiding the test set.
- It uses Random Search sampling to compare structural choices. That is appropriate for controlling candidate pools, but the final article should still report the official optimizer benchmark separately.
- Differences in CNN mean fitness between RMSProp/Tanh and Adam/Tanh are very small, so the CNN-specific claim should be phrased as a near-tie with RMSProp/Tanh selected for consistency and seed-win/best-fitness advantage.

## Saved Artifacts

- Full per-evaluation data: `outputs/structural_fast_official_space/structural_validation_runs.csv`
- Summary table: `outputs/structural_fast_official_space/structural_validation_summary.csv`
- This report: `outputs/structural_fast_official_space/structural_validation_report.md`
