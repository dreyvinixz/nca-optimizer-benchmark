# Model selection: testes estatisticos e economicos

## Leitura curta

Os testes foram rodados para todos os modelos, otimizadores, seeds e os tres experimentos disponiveis. A conclusao continua sendo cautelosa: o MLP e o modelo mais promissor nas metricas preditivas, mas a decisao economica depende do criterio financeiro usado.

## Melhores combinacoes preditivas por experimento

| experiment_label            | model   | optimizer   |   reported_metric_mean |   accuracy_mean |   mcc_mean |   f1_mean |
|:----------------------------|:--------|:------------|-----------------------:|----------------:|-----------:|----------:|
| Exp. 1 - Holdout + MCC/F1   | mlp     | gwo         |               0.304668 |        0.652501 |   0.304668 |  0.6601   |
| Exp. 2 - Holdout + Accuracy | mlp     | pso         |               0.65228  |        0.65228  |   0.304326 |  0.658552 |
| Exp. 3 - CV + Accuracy      | mlp     | gwo         |               0.651505 |        0.651505 |   0.302763 |  0.657975 |

## Melhores combinacoes economicas por experimento

| experiment_label            | model   | optimizer   |   total_profit_mean |   win_rate_mean |   profit_factor_mean |   max_drawdown_mean |   sharpe_mean |
|:----------------------------|:--------|:------------|--------------------:|----------------:|---------------------:|--------------------:|--------------:|
| Exp. 1 - Holdout + MCC/F1   | svm     | gwo         |             38416.7 |        0.515162 |              1.84067 |            -2048.33 |       14.3125 |
| Exp. 2 - Holdout + Accuracy | cnn     | gwo         |             30003.3 |        0.494245 |              1.5601  |            -2461.67 |       10.3001 |
| Exp. 3 - CV + Accuracy      | mlp     | gwo         |             28406.7 |        0.488048 |              1.52143 |            -2060    |       13.505  |

## Resumo preditivo por modelo

| model   |   n |   accuracy_mean |   mcc_mean |   f1_mean |   auc_roc_mean |   reported_metric_mean |
|:--------|----:|----------------:|-----------:|----------:|---------------:|-----------------------:|
| cnn     |  45 |         0.62749 |   0.254139 |  0.627302 |       0.660734 |               0.497835 |
| mlp     |  45 |         0.64364 |   0.286969 |  0.651555 |       0.684586 |               0.520344 |
| rf      |  45 |         0.6186  |   0.236545 |  0.63849  |       0.656052 |               0.500102 |
| svm     |  45 |         0.59032 |   0.183424 |  0.610054 |       0.615823 |               0.460327 |

## Resumo economico por modelo

| model   |   n |   total_profit_mean |   win_rate_mean |   profit_factor_mean |   max_drawdown_mean |   sharpe_mean |
|:--------|----:|--------------------:|----------------:|---------------------:|--------------------:|--------------:|
| cnn     |  45 |             23836.2 |        0.480102 |              1.43279 |            -3682.67 |       8.88031 |
| mlp     |  45 |             25904   |        0.48399  |              1.48139 |            -3238.78 |      12.2839  |
| rf      |  45 |             23542.4 |        0.469706 |              1.41289 |            -1988.67 |      12.1927  |
| svm     |  45 |             11736.2 |        0.460034 |              1.2383  |            -7115.33 |       5.41266 |

## Testes Friedman preditivos

| scope                                 | metric        |   n_blocks |   friedman_statistic |   friedman_p_value |   mean_rank_cnn |   mean_rank_mlp |   mean_rank_rf |   mean_rank_svm |   mean_cnn |   mean_mlp |   mean_rf |   mean_svm |
|:--------------------------------------|:--------------|-----------:|---------------------:|-------------------:|----------------:|----------------:|---------------:|----------------:|-----------:|-----------:|----------:|-----------:|
| all_experiments_optimizer_seed_blocks | accuracy_test |         45 |              79.48   |           0        |         2.55556 |         1.15556 |        2.75556 |         3.53333 |   0.62749  |   0.64364  |  0.6186   |   0.59032  |
| all_experiments_optimizer_seed_blocks | mcc_test      |         45 |              72.8667 |           0        |         2.6     |         1.17778 |        2.8     |         3.42222 |   0.254139 |   0.286969 |  0.236545 |   0.183424 |
| all_experiments_optimizer_seed_blocks | f1_test       |         45 |              31.32   |           1e-06    |         2.6     |         1.6     |        2.8     |         3       |   0.627302 |   0.651555 |  0.63849  |   0.610054 |
| all_experiments_optimizer_seed_blocks | auc_roc_test  |         45 |              56.68   |           0        |         2.62222 |         1.28889 |        2.93333 |         3.15556 |   0.660734 |   0.684586 |  0.656052 |   0.615823 |
| exp1_holdout_mcc_f1                   | mcc_test      |         15 |              22.84   |           4.4e-05  |         3.66667 |         1.53333 |        2.06667 |         2.73333 |   0.224359 |   0.260522 |  0.289305 |   0.213584 |
| exp1_holdout_mcc_f1                   | accuracy_test |         15 |              25      |           1.5e-05  |         3.53333 |         1.46667 |        1.93333 |         3.06667 |   0.613324 |   0.630412 |  0.644799 |   0.603564 |
| exp1_holdout_mcc_f1                   | f1_test       |         15 |              17      |           0.000707 |         3.53333 |         2.46667 |        1.6     |         2.4     |   0.596927 |   0.638595 |  0.664499 |   0.60166  |
| exp2_holdout_accuracy                 | accuracy_test |         15 |              42.92   |           0        |         2       |         1       |        3.13333 |         3.86667 |   0.635259 |   0.65073  |  0.604471 |   0.578486 |
| exp2_holdout_accuracy                 | mcc_test      |         15 |              42.92   |           0        |         2       |         1       |        3.13333 |         3.86667 |   0.270721 |   0.301195 |  0.208095 |   0.159392 |
| exp2_holdout_accuracy                 | f1_test       |         15 |              32.84   |           0        |         2.2     |         1.06667 |        3.33333 |         3.4     |   0.639423 |   0.65786  |  0.624423 |   0.600269 |
| exp3_cv_accuracy                      | accuracy_test |         15 |              38.12   |           0        |         2.13333 |         1       |        3.2     |         3.66667 |   0.633887 |   0.649779 |  0.606529 |   0.588911 |
| exp3_cv_accuracy                      | mcc_test      |         15 |              38.12   |           0        |         2.13333 |         1       |        3.2     |         3.66667 |   0.267336 |   0.299191 |  0.212234 |   0.177296 |
| exp3_cv_accuracy                      | f1_test       |         15 |              28.2    |           3e-06    |         2.06667 |         1.26667 |        3.46667 |         3.2     |   0.645557 |   0.65821  |  0.626549 |   0.628233 |

## Pairwise preditivo do melhor modelo medio contra os demais

| scope                                 | metric        | best_model_by_mean   | comparison   |   n_blocks |   mean_difference |   median_difference |   wilcoxon_p_value |   holm_p_value | significant_0_05   |
|:--------------------------------------|:--------------|:---------------------|:-------------|-----------:|------------------:|--------------------:|-------------------:|---------------:|:-------------------|
| all_experiments_optimizer_seed_blocks | accuracy_test | mlp                  | mlp vs cnn   |         45 |          0.01615  |            0.01494  |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | accuracy_test | mlp                  | mlp vs rf    |         45 |          0.025041 |            0.041501 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | accuracy_test | mlp                  | mlp vs svm   |         45 |          0.05332  |            0.058765 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | mcc_test      | mlp                  | mlp vs cnn   |         45 |          0.032831 |            0.029822 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | mcc_test      | mlp                  | mlp vs rf    |         45 |          0.050424 |            0.083602 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | mcc_test      | mlp                  | mlp vs svm   |         45 |          0.103545 |            0.117551 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | f1_test       | mlp                  | mlp vs cnn   |         45 |          0.024253 |            0.015478 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | f1_test       | mlp                  | mlp vs rf    |         45 |          0.013065 |            0.029147 |           1e-05    |       1.9e-05  | True               |
| all_experiments_optimizer_seed_blocks | f1_test       | mlp                  | mlp vs svm   |         45 |          0.041501 |            0.033008 |           1e-05    |       1.9e-05  | True               |
| all_experiments_optimizer_seed_blocks | auc_roc_test  | mlp                  | mlp vs cnn   |         45 |          0.023851 |            0.020034 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | auc_roc_test  | mlp                  | mlp vs rf    |         45 |          0.028533 |            0.050343 |           0        |       0        | True               |
| all_experiments_optimizer_seed_blocks | auc_roc_test  | mlp                  | mlp vs svm   |         45 |          0.068763 |            0.071138 |           0        |       0        | True               |
| exp1_holdout_mcc_f1                   | mcc_test      | rf                   | rf vs cnn    |         15 |          0.064946 |            0.024445 |           6.1e-05  |       0.000183 | True               |
| exp1_holdout_mcc_f1                   | mcc_test      | rf                   | rf vs mlp    |         15 |          0.028783 |           -0.007065 |           0.055359 |       0.055359 | False              |
| exp1_holdout_mcc_f1                   | mcc_test      | rf                   | rf vs svm    |         15 |          0.075721 |            0.012293 |           0.015076 |       0.030151 | True               |
| exp1_holdout_mcc_f1                   | accuracy_test | rf                   | rf vs cnn    |         15 |          0.031474 |            0.012284 |           0.000643 |       0.00193  | True               |
| exp1_holdout_mcc_f1                   | accuracy_test | rf                   | rf vs mlp    |         15 |          0.014387 |           -0.00332  |           0.049919 |       0.049919 | True               |
| exp1_holdout_mcc_f1                   | accuracy_test | rf                   | rf vs svm    |         15 |          0.041235 |            0.015936 |           0.003431 |       0.006863 | True               |
| exp1_holdout_mcc_f1                   | f1_test       | rf                   | rf vs cnn    |         15 |          0.067573 |            0.025763 |           6.1e-05  |       0.000183 | True               |
| exp1_holdout_mcc_f1                   | f1_test       | rf                   | rf vs mlp    |         15 |          0.025904 |            0.00728  |           0.000305 |       0.00061  | True               |
| exp1_holdout_mcc_f1                   | f1_test       | rf                   | rf vs svm    |         15 |          0.062839 |            0.000416 |           0.207764 |       0.207764 | False              |
| exp2_holdout_accuracy                 | accuracy_test | mlp                  | mlp vs cnn   |         15 |          0.015471 |            0.015272 |           0.000645 |       0.001935 | True               |
| exp2_holdout_accuracy                 | accuracy_test | mlp                  | mlp vs rf    |         15 |          0.046259 |            0.046149 |           0.000652 |       0.001935 | True               |
| exp2_holdout_accuracy                 | accuracy_test | mlp                  | mlp vs svm   |         15 |          0.072244 |            0.079349 |           0.000653 |       0.001935 | True               |
| exp2_holdout_accuracy                 | mcc_test      | mlp                  | mlp vs cnn   |         15 |          0.030474 |            0.029899 |           6.1e-05  |       0.000183 | True               |
| exp2_holdout_accuracy                 | mcc_test      | mlp                  | mlp vs rf    |         15 |          0.0931   |            0.092802 |           6.1e-05  |       0.000183 | True               |
| exp2_holdout_accuracy                 | mcc_test      | mlp                  | mlp vs svm   |         15 |          0.141803 |            0.157291 |           6.1e-05  |       0.000183 | True               |
| exp2_holdout_accuracy                 | f1_test       | mlp                  | mlp vs cnn   |         15 |          0.018437 |            0.016938 |           6.1e-05  |       0.000183 | True               |
| exp2_holdout_accuracy                 | f1_test       | mlp                  | mlp vs rf    |         15 |          0.033437 |            0.034068 |           6.1e-05  |       0.000183 | True               |
| exp2_holdout_accuracy                 | f1_test       | mlp                  | mlp vs svm   |         15 |          0.057591 |            0.043404 |           0.000305 |       0.000305 | True               |
| exp3_cv_accuracy                      | accuracy_test | mlp                  | mlp vs cnn   |         15 |          0.015892 |            0.015272 |           0.00065  |       0.00195  | True               |
| exp3_cv_accuracy                      | accuracy_test | mlp                  | mlp vs rf    |         15 |          0.043249 |            0.042165 |           0.000652 |       0.00195  | True               |
| exp3_cv_accuracy                      | accuracy_test | mlp                  | mlp vs svm   |         15 |          0.060868 |            0.058101 |           0.000653 |       0.00195  | True               |
| exp3_cv_accuracy                      | mcc_test      | mlp                  | mlp vs cnn   |         15 |          0.031854 |            0.030708 |           6.1e-05  |       0.000183 | True               |
| exp3_cv_accuracy                      | mcc_test      | mlp                  | mlp vs rf    |         15 |          0.086956 |            0.084902 |           6.1e-05  |       0.000183 | True               |
| exp3_cv_accuracy                      | mcc_test      | mlp                  | mlp vs svm   |         15 |          0.121895 |            0.11572  |           6.1e-05  |       0.000183 | True               |
| exp3_cv_accuracy                      | f1_test       | mlp                  | mlp vs cnn   |         15 |          0.012653 |            0.013441 |           0.000122 |       0.000244 | True               |
| exp3_cv_accuracy                      | f1_test       | mlp                  | mlp vs rf    |         15 |          0.031661 |            0.031609 |           6.1e-05  |       0.000183 | True               |
| exp3_cv_accuracy                      | f1_test       | mlp                  | mlp vs svm   |         15 |          0.029977 |            0.031885 |           0.000854 |       0.000854 | True               |

## Testes Friedman economicos

| scope                                          | metric                  |   n_blocks |   friedman_statistic |   friedman_p_value |   mean_rank_cnn |   mean_rank_mlp |   mean_rank_rf |   mean_rank_svm |    mean_cnn |    mean_mlp |     mean_rf |    mean_svm | original_metric         |
|:-----------------------------------------------|:------------------------|-----------:|---------------------:|-------------------:|----------------:|----------------:|---------------:|----------------:|------------:|------------:|------------:|------------:|:------------------------|
| economic_all_experiments_optimizer_seed_blocks | total_profit_points     |         45 |              42.7867 |           0        |         2.4     |         1.53333 |        2.84444 |         3.22222 | 23836.2     | 25904       | 23542.4     | 11736.2     | total_profit_points     |
| economic_all_experiments_optimizer_seed_blocks | profit_factor           |         45 |              42.7867 |           0        |         2.4     |         1.53333 |        2.84444 |         3.22222 |     1.43279 |     1.48139 |     1.41289 |     1.2383  | profit_factor           |
| economic_all_experiments_optimizer_seed_blocks | sharpe_ratio_annualized |         45 |              77.1867 |           0        |         3.33333 |         1.4     |        1.95556 |         3.31111 |     8.88031 |    12.2839  |    12.1927  |     5.41266 | sharpe_ratio_annualized |
| economic_all_experiments_optimizer_seed_blocks | max_drawdown_points     |         45 |              91.3733 |           0        |         3.15556 |         1.71111 |        1.48889 |         3.64444 | -3682.67    | -3238.78    | -1988.67    | -7115.33    | max_drawdown_points     |
| economic_exp1_holdout_mcc_f1                   | total_profit_points     |         15 |               5.16   |           0.160449 |         3.13333 |         2.13333 |        2.33333 |         2.4     | 19969.3     | 22110       | 26465.3     | 17016.7     | total_profit_points     |
| economic_exp2_holdout_accuracy                 | total_profit_points     |         15 |              27.72   |           4e-06    |         1.8     |         1.46667 |        3.26667 |         3.46667 | 26860.7     | 27737.3     | 21972.7     | 11440       | total_profit_points     |
| economic_exp3_cv_accuracy                      | total_profit_points     |         15 |              37.64   |           0        |         2.26667 |         1       |        2.93333 |         3.8     | 24678.7     | 27864.7     | 22189.3     |  6752       | total_profit_points     |

## Pairwise economico do melhor modelo medio contra os demais

| scope                                          | metric                  | best_model_by_mean   | comparison   |   n_blocks |   mean_difference |   median_difference |   wilcoxon_p_value |   holm_p_value | significant_0_05   | original_metric         |
|:-----------------------------------------------|:------------------------|:---------------------|:-------------|-----------:|------------------:|--------------------:|-------------------:|---------------:|:-------------------|:------------------------|
| economic_all_experiments_optimizer_seed_blocks | total_profit_points     | mlp                  | mlp vs cnn   |         45 |       2067.78     |         2150        |           9e-06    |       1.1e-05  | True               | total_profit_points     |
| economic_all_experiments_optimizer_seed_blocks | total_profit_points     | mlp                  | mlp vs rf    |         45 |       2361.56     |         4260        |           0        |       0        | True               | total_profit_points     |
| economic_all_experiments_optimizer_seed_blocks | total_profit_points     | mlp                  | mlp vs svm   |         45 |      14167.8      |        14210        |           6e-06    |       1.1e-05  | True               | total_profit_points     |
| economic_all_experiments_optimizer_seed_blocks | profit_factor           | mlp                  | mlp vs cnn   |         45 |          0.048602 |            0.049758 |           9e-06    |       1.8e-05  | True               | profit_factor           |
| economic_all_experiments_optimizer_seed_blocks | profit_factor           | mlp                  | mlp vs rf    |         45 |          0.068495 |            0.096909 |           0        |       0        | True               | profit_factor           |
| economic_all_experiments_optimizer_seed_blocks | profit_factor           | mlp                  | mlp vs svm   |         45 |          0.243083 |            0.287172 |           1.6e-05  |       1.8e-05  | True               | profit_factor           |
| economic_all_experiments_optimizer_seed_blocks | sharpe_ratio_annualized | mlp                  | mlp vs cnn   |         45 |          3.40354  |            3.71301  |           0        |       0        | True               | sharpe_ratio_annualized |
| economic_all_experiments_optimizer_seed_blocks | sharpe_ratio_annualized | mlp                  | mlp vs rf    |         45 |          0.09117  |            0.997845 |           0.000685 |       0.000685 | True               | sharpe_ratio_annualized |
| economic_all_experiments_optimizer_seed_blocks | sharpe_ratio_annualized | mlp                  | mlp vs svm   |         45 |          6.87119  |            6.85803  |           0        |       0        | True               | sharpe_ratio_annualized |
| economic_all_experiments_optimizer_seed_blocks | max_drawdown_points     | rf                   | rf vs cnn    |         45 |       1694        |          560        |           0        |       0        | True               | max_drawdown_points     |
| economic_all_experiments_optimizer_seed_blocks | max_drawdown_points     | rf                   | rf vs mlp    |         45 |       1250.11     |          160        |           0.001399 |       0.001399 | True               | max_drawdown_points     |
| economic_all_experiments_optimizer_seed_blocks | max_drawdown_points     | rf                   | rf vs svm    |         45 |       5126.67     |         2525        |           0        |       0        | True               | max_drawdown_points     |
| economic_exp1_holdout_mcc_f1                   | total_profit_points     | rf                   | rf vs cnn    |         15 |       6496        |         1910        |           0.04126  |       0.123779 | False              | total_profit_points     |
| economic_exp1_holdout_mcc_f1                   | total_profit_points     | rf                   | rf vs mlp    |         15 |       4355.33     |          -10        |           0.359131 |       0.718262 | False              | total_profit_points     |
| economic_exp1_holdout_mcc_f1                   | total_profit_points     | rf                   | rf vs svm    |         15 |       9448.67     |         -150        |           0.638672 |       0.718262 | False              | total_profit_points     |
| economic_exp2_holdout_accuracy                 | total_profit_points     | mlp                  | mlp vs cnn   |         15 |        876.667    |         1710        |           0.168823 |       0.168823 | False              | total_profit_points     |
| economic_exp2_holdout_accuracy                 | total_profit_points     | mlp                  | mlp vs rf    |         15 |       5764.67     |         6150        |           6.1e-05  |       0.000183 | True               | total_profit_points     |
| economic_exp2_holdout_accuracy                 | total_profit_points     | mlp                  | mlp vs svm   |         15 |      16297.3      |        19000        |           0.001526 |       0.003052 | True               | total_profit_points     |
| economic_exp3_cv_accuracy                      | total_profit_points     | mlp                  | mlp vs cnn   |         15 |       3186        |         3010        |           6.1e-05  |       0.000183 | True               | total_profit_points     |
| economic_exp3_cv_accuracy                      | total_profit_points     | mlp                  | mlp vs rf    |         15 |       5675.33     |         5860        |           6.1e-05  |       0.000183 | True               | total_profit_points     |
| economic_exp3_cv_accuracy                      | total_profit_points     | mlp                  | mlp vs svm   |         15 |      21112.7      |        15720        |           6.1e-05  |       0.000183 | True               | total_profit_points     |

## Como interpretar

- Friedman testa se ha diferenca global entre os quatro modelos nos mesmos blocos comparaveis.
- Pairwise usa Wilcoxon pareado e correcao de Holm contra o melhor modelo medio daquele escopo.
- Com apenas tres seeds, nao e recomendavel afirmar superioridade definitiva. A melhor frase e: `modelo mais promissor nos experimentos atuais`.
- O resultado economico pode divergir do resultado preditivo porque lucro, drawdown e Sharpe dependem da distribuicao temporal dos erros, nao apenas da acuracia media.
