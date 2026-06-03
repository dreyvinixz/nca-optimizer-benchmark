# 🧠 QuantBase Project Architecture

> Auto-generated architecture mapping  
> Last update: 2026-06-03 15:41:17 (Horário de Brasília)

---

## Critérios de leitura do mapa

- **[📄 Página]**: páginas React
- **[🧩 Seção]**: blocos grandes da interface
- **[🎨 Componente]**: componentes React reutilizáveis
- **[🧱 Layout]**: estruturas de composição/layout
- **[🪝 Hook]**: hooks customizados
- **[🗂️ Dados]**: mocks, constantes e estruturas estáticas
- **[🧾 Tipagem]**: tipos, interfaces e contratos
- **[🎨 Estilo]**: CSS/SCSS
- **[🛠️ Config]**: arquivos de configuração
- **[🧪 Teste]**: testes
- **[🤖 Script]**: scripts e automações
- **[⚙️ Utilitário]**: lógica auxiliar
- **[📦 Módulo]**: módulo genérico quando não houver sinal suficiente

---

## 📁 Árvore do Projeto

```text
nca-optimizer-benchmark/
├── article/
│   ├── cover_letter/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── figures/
│   │   ├── optimizer_convergence.png  # [📄 Arquivo] Arquivo do projeto (optimizer_convergence)
│   │   ├── optimizer_metrics_comparison.png  # [📄 Arquivo] Arquivo do projeto (optimizer_metrics_comparison)
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── manuscript/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── overleaf_zips/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── references/
│   │   ├── _ICCSA_2026___Andrey_____Combining_Technical_Indicators_and_Genetic_Algorithms_for_Short_Term_Machine_Learning_Prediction_of_Mini_Index_Futures (1).pdf  # [📄 Arquivo] Arquivo do projeto (_ICCSA_2026___Andrey_____Combining_Technical_Indicators_and_Genetic_Algorithms_for_Short_Term_Machine_Learning_Prediction_of_Mini_Index_Futures (1))
│   │   ├── _ICSSA_Document_2025___Andrey__Predictive_analysis_with_technical_indicators_and_features_selection_for_futures_contracts_trading (1).pdf  # [📄 Arquivo] Arquivo do projeto (_ICSSA_Document_2025___Andrey__Predictive_analysis_with_technical_indicators_and_features_selection_for_futures_contracts_trading (1))
│   │   └── s00521-025-11546-2.pdf  # [📄 Arquivo] Arquivo do projeto (s00521-025-11546-2)
│   ├── tables/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   └── templates/
│       └── README.md  # [📘 Documento] Documentação (README)
├── checkpoints/
│   ├── de/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── final_models/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── ga/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── gwo/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   └── pso/
│       └── README.md  # [📘 Documento] Documentação (README)
├── config/
│   ├── assets_universe.yaml  # [🛠️ Config] Arquivo de configuração (assets_universe)
│   ├── experiment_config.yaml  # [🛠️ Config] Arquivo de configuração (experiment_config)
│   ├── paths.yaml  # [🛠️ Config] Arquivo de configuração (paths)
│   └── search_spaces.yaml  # [🛠️ Config] Arquivo de configuração (search_spaces)
├── data/
│   ├── interim/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── processed/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   └── raw/
│       ├── merged_output.csv  # [📄 Arquivo] Arquivo do projeto (merged_output)
│       └── README.md  # [📘 Documento] Documentação (README)
├── docs/
│   ├── experiment_protocol.md  # [📘 Documento] Documentação (experiment_protocol)
│   ├── implementation_audit.md  # [📘 Documento] Documentação (implementation_audit)
│   ├── journal_requirements.md  # [📘 Documento] Documentação (journal_requirements)
│   ├── methodology.md  # [📘 Documento] Documentação (methodology)
│   └── reviewer_response_map.md  # [📘 Documento] Documentação (reviewer_response_map)
├── experiments/
│   └── train_model/
│       ├── ga_checkpoints/
│       │   └── open_arquive.py  # [📦 Módulo] Módulo Python (open_arquive)
│       ├── images/
│       │   ├── mlp/
│       │   │   ├── mlp_teste1/
│       │   │   │   ├── Captura de tela 2026-01-06 174153.png  # [📄 Arquivo] Arquivo do projeto (Captura de tela 2026-01-06 174153)
│       │   │   │   ├── ga.png  # [📄 Arquivo] Arquivo do projeto (ga)
│       │   │   │   ├── ga_zoom.png  # [📄 Arquivo] Arquivo do projeto (ga_zoom)
│       │   │   │   └── mlpestavel.png  # [📄 Arquivo] Arquivo do projeto (mlpestavel)
│       │   │   ├── mlp_teste2/
│       │   │   │   ├── Captura de tela 2026-01-07 233044.png  # [📄 Arquivo] Arquivo do projeto (Captura de tela 2026-01-07 233044)
│       │   │   │   ├── Figure_1.png  # [📄 Arquivo] Arquivo do projeto (Figure_1)
│       │   │   │   ├── mlp.png  # [📄 Arquivo] Arquivo do projeto (mlp)
│       │   │   │   ├── open_arquive.py  # [🧪 Teste] Teste automatizado (open_arquive)
│       │   │   │   ├── roc and pr curve.png  # [📄 Arquivo] Arquivo do projeto (roc and pr curve)
│       │   │   │   └── tradeoff.png  # [📄 Arquivo] Arquivo do projeto (tradeoff)
│       │   │   └── mlp_teste3/
│       │   │       ├── data.log  # [📄 Arquivo] Arquivo do projeto (data)
│       │   │       ├── Figure_1.png  # [📄 Arquivo] Arquivo do projeto (Figure_1)
│       │   │       └── open_arquive.py  # [🧪 Teste] Teste automatizado (open_arquive)
│       │   ├── random_forest/
│       │   │   ├── teste1/
│       │   │   │   ├── Figure_1.png  # [📄 Arquivo] Arquivo do projeto (Figure_1)
│       │   │   │   ├── garandomforest.png  # [📄 Arquivo] Arquivo do projeto (garandomforest)
│       │   │   │   ├── log.txt  # [📄 Arquivo] Arquivo do projeto (log)
│       │   │   │   └── roc.png  # [📄 Arquivo] Arquivo do projeto (roc)
│       │   │   └── teste2/
│       │   │       └── README.md  # [📘 Documento] Documentação (README)
│       │   └── svm/
│       │       └── README.md  # [📘 Documento] Documentação (README)
│       ├── logs/
│       │   ├── mlpreal_training.log  # [📄 Arquivo] Arquivo do projeto (mlpreal_training)
│       │   └── view_logs.py  # [📦 Módulo] Script para visualizar os logs de treinamento
│       ├── rf_ga_checkpoints/  [∅ Sem conteúdo]
│       ├── all_models.png  # [📄 Arquivo] Arquivo do projeto (all_models)
│       ├── best_mlp_checkpoint.h5  # [📄 Arquivo] Arquivo do projeto (best_mlp_checkpoint)
│       ├── best_mlp_checkpointy.h5  # [📄 Arquivo] Arquivo do projeto (best_mlp_checkpointy)
│       ├── explicacao_tecnica.md  # [📘 Documento] Documentação (explicacao_tecnica)
│       ├── Figure_2.png  # [📄 Arquivo] Arquivo do projeto (Figure_2)
│       ├── grafic.py  # [📦 Módulo] Módulo Python (grafic)
│       ├── inspect_model.py  # [📦 Módulo] Módulo Python (inspect_model)
│       ├── merged_output.csv  # [📄 Arquivo] Arquivo do projeto (merged_output)
│       ├── mlp_ga.py  # [📦 Módulo] graficos: | ⚡ GA_optimize_MLP, bits_to_int, create_mlp_model, decode_individual
│       ├── mlp_test.py  # [🧪 Teste] ===================================================== | ⚡ create_mlp_model, get_feature_names, train_and_evaluate_mlp
│       ├── mlpreal.py  # [📦 Módulo] ===================================================== | ⚡ build_ga_mlp, create_mlp_model, get_feature_names, train_and_evaluate_mlp
│       ├── random_forest.py  # [📦 Módulo] Módulo Python (random_forest) | ⚡ GA_optimize_RandomForest, bits_to_int, decode_individual, decode_linear
│       └── requirements.txt  # [📄 Arquivo] Arquivo do projeto (requirements)
├── logs/
│   ├── de/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── experiments/
│   │   ├── compare_optimizers.log  # [📄 Arquivo] Arquivo do projeto (compare_optimizers)
│   │   ├── de.log  # [📄 Arquivo] Arquivo do projeto (de)
│   │   ├── ga.log  # [📄 Arquivo] Arquivo do projeto (ga)
│   │   ├── gwo.log  # [📄 Arquivo] Arquivo do projeto (gwo)
│   │   ├── paper_figures.log  # [📄 Arquivo] Arquivo do projeto (paper_figures)
│   │   ├── pso.log  # [📄 Arquivo] Arquivo do projeto (pso)
│   │   ├── random_search.log  # [📄 Arquivo] Arquivo do projeto (random_search)
│   │   ├── reproduce_iccsa.log  # [📄 Arquivo] Arquivo do projeto (reproduce_iccsa)
│   │   ├── reproduce_ijcnn.log  # [📄 Arquivo] Arquivo do projeto (reproduce_ijcnn)
│   │   └── statistical_tests.log  # [📄 Arquivo] Arquivo do projeto (statistical_tests)
│   ├── ga/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   └── pso/
│       └── README.md  # [📘 Documento] Documentação (README)
├── notebooks/
│   ├── 01_data_audit.ipynb  # [📄 Arquivo] Arquivo do projeto (01_data_audit)
│   ├── 02_feature_analysis.ipynb  # [📄 Arquivo] Arquivo do projeto (02_feature_analysis)
│   ├── 03_result_exploration.ipynb  # [📄 Arquivo] Arquivo do projeto (03_result_exploration)
│   └── 04_figures_preview.ipynb  # [📄 Arquivo] Arquivo do projeto (04_figures_preview)
├── outputs/
│   ├── backtests/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── figures/
│   │   ├── optimizer_convergence.png  # [📄 Arquivo] Arquivo do projeto (optimizer_convergence)
│   │   └── optimizer_metrics_comparison.png  # [📄 Arquivo] Arquivo do projeto (optimizer_metrics_comparison)
│   ├── metrics/
│   │   ├── convergence/
│   │   │   ├── ga_convergence.csv  # [📄 Arquivo] Arquivo do projeto (ga_convergence)
│   │   │   ├── pso_convergence.csv  # [📄 Arquivo] Arquivo do projeto (pso_convergence)
│   │   │   └── random_search_convergence.csv  # [📄 Arquivo] Arquivo do projeto (random_search_convergence)
│   │   ├── ga_best_by_seed.csv  # [📄 Arquivo] Arquivo do projeto (ga_best_by_seed)
│   │   ├── ga_runs.csv  # [📄 Arquivo] Arquivo do projeto (ga_runs)
│   │   ├── iccsa_baseline_temporal.csv  # [📄 Arquivo] Arquivo do projeto (iccsa_baseline_temporal)
│   │   ├── ijcnn_historical_baseline.csv  # [📄 Arquivo] Arquivo do projeto (ijcnn_historical_baseline)
│   │   ├── pso_best_by_seed.csv  # [📄 Arquivo] Arquivo do projeto (pso_best_by_seed)
│   │   ├── pso_runs.csv  # [📄 Arquivo] Arquivo do projeto (pso_runs)
│   │   ├── random_search_best_by_seed.csv  # [📄 Arquivo] Arquivo do projeto (random_search_best_by_seed)
│   │   └── random_search_runs.csv  # [📄 Arquivo] Arquivo do projeto (random_search_runs)
│   ├── networks/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── pdf/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── predictions/
│   │   ├── ga_predictions.csv  # [📄 Arquivo] Arquivo do projeto (ga_predictions)
│   │   ├── pso_predictions.csv  # [📄 Arquivo] Arquivo do projeto (pso_predictions)
│   │   └── random_search_predictions.csv  # [📄 Arquivo] Arquivo do projeto (random_search_predictions)
│   ├── previews/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   ├── reports/
│   │   ├── de_placeholder.md  # [📘 Documento] Documentação (de_placeholder)
│   │   ├── gwo_placeholder.md  # [📘 Documento] Documentação (gwo_placeholder)
│   │   ├── iccsa_baseline_temporal.md  # [📘 Documento] Documentação (iccsa_baseline_temporal)
│   │   ├── ijcnn_historical_baseline.md  # [📘 Documento] Documentação (ijcnn_historical_baseline)
│   │   ├── optimizer_benchmark_summary.md  # [📘 Documento] Documentação (optimizer_benchmark_summary)
│   │   └── statistical_tests_first_stage.md  # [📘 Documento] Documentação (statistical_tests_first_stage)
│   ├── statistical_tests/
│   │   └── wilcoxon_first_stage.csv  # [📄 Arquivo] Arquivo do projeto (wilcoxon_first_stage)
│   ├── svg/
│   │   └── README.md  # [📘 Documento] Documentação (README)
│   └── tables/
│       └── optimizer_comparison.csv  # [📄 Arquivo] Arquivo do projeto (optimizer_comparison)
├── scripts/
│   ├── 00_reproduce_iccsa_baseline.py  # [🤖 Script] Script executável (00_reproduce_iccsa_baseline) | ⚡ main
│   ├── 01_reproduce_ijcnn_baseline.py  # [🤖 Script] Script executável (01_reproduce_ijcnn_baseline) | ⚡ main
│   ├── 02_run_random_search.py  # [🤖 Script] Script executável (02_run_random_search) | ⚡ main
│   ├── 03_run_ga.py  # [🤖 Script] Script executável (03_run_ga) | ⚡ main
│   ├── 04_run_pso.py  # [🤖 Script] Script executável (04_run_pso) | ⚡ main
│   ├── 05_run_de.py  # [🤖 Script] Script executável (05_run_de) | ⚡ main
│   ├── 06_run_gwo.py  # [🤖 Script] Script executável (06_run_gwo) | ⚡ main
│   ├── 07_compare_optimizers.py  # [🤖 Script] Script executável (07_compare_optimizers) | ⚡ main
│   ├── 08_run_statistical_tests.py  # [🧪 Teste] Teste automatizado (08_run_statistical_tests) | ⚡ main
│   └── 09_generate_paper_figures.py  # [🤖 Script] Script executável (09_generate_paper_figures) | ⚡ main
├── src/
│   ├── evaluation/
│   │   ├── backtest.py  # [🧪 Teste] Placeholder for financial backtesting.
│   │   ├── metrics.py  # [🤖 Script] Classification metrics for optimizer benchmark outputs. | ⚡ compute_classification_metrics
│   │   └── statistical_tests.py  # [🧪 Teste] Placeholder for statistical tests.
│   ├── models/
│   │   └── mlp.py  # [🤖 Script] MLP model training with TensorFlow preference and sklearn fallback. | ⚡ fit_predict_mlp
│   ├── optimizers/
│   │   ├── de.py  # [⚙️ Utilitário] Placeholder for Differential Evolution. | ⚡ run_de
│   │   ├── ga.py  # [🤖 Script] Simple real-coded Genetic Algorithm using the shared objective function. | ⚡ run_ga
│   │   ├── gwo.py  # [⚙️ Utilitário] Placeholder for Grey Wolf Optimizer. | ⚡ run_gwo
│   │   ├── pso.py  # [🤖 Script] Particle Swarm Optimization using the shared objective function. | ⚡ run_pso
│   │   └── random_search.py  # [🤖 Script] Random Search optimizer baseline. | ⚡ run_random_search, sample_candidate
│   ├── utils/
│   │   ├── io.py  # [⚙️ Utilitário] I/O helpers for configuration and machine-readable experiment outputs. | ⚡ ensure_directory, ensure_output_directories, load_project_configs, load_yaml
│   │   ├── logger.py  # [⚙️ Utilitário] Logging setup for benchmark scripts. | ⚡ get_logger
│   │   └── seeds.py  # [⚙️ Utilitário] Utilities for reproducible experiment execution. | ⚡ set_global_seed
│   ├── benchmark.py  # [⚙️ Utilitário] Shared setup and persistence for benchmark scripts. | ⚡ prepare_benchmark, save_optimizer_outputs
│   ├── data_loader.py  # [🧠 Lógica] Dataset loading for the NCA optimizer benchmark. | ⚡ LoadedDataset, load_legacy_dataset
│   ├── feature_engineering.py  # [⚙️ Utilitário] Feature engineering helpers for future benchmark extensions. | ⚡ add_exponential_moving_average_spreads, add_moving_average_spreads, validate_required_price_columns
│   ├── feature_selection.py  # [⚙️ Utilitário] Feature selection helpers for historical Information Gain features. | ⚡ indices_to_feature_names, select_features
│   ├── objective.py  # [🤖 Script] Central candidate evaluation shared by all optimizers. | ⚡ candidate_to_log, evaluate_best_on_test, evaluate_candidate, normalize_candidate
│   ├── preprocessing.py  # [⚙️ Utilitário] Preprocessing helpers for the benchmark pipeline. | ⚡ drop_missing_rows, keep_numeric_features
│   └── temporal_split.py  # [🧠 Lógica] Chronological train/validation/test splitting. | ⚡ TemporalSplit, make_temporal_split
├── generate_project_map.py  # [🤖 Script] Script de automação (generate_project_map) | ⚡ analyze_python_ast, analyze_ts_js, build_tree, classify_css
├── PROJECT_CONTEXT.md  # [📘 Documento] Documentação (PROJECT_CONTEXT)
├── README.md  # [📘 Documento] Documentação (README)
├── requirements.txt  # [📄 Arquivo] Arquivo do projeto (requirements)
├── ROADMAP.md  # [📘 Documento] Documentação (ROADMAP)
├── RUNBOOK.md  # [📘 Documento] Documentação (RUNBOOK)
├── SKILLS.md  # [📘 Documento] Documentação (SKILLS)
└── TASKS.md  # [📘 Documento] Documentação (TASKS)
```

---
## Observações

Este README é inferido automaticamente. A classificação melhorou bastante,
mas ainda depende da qualidade estrutural do código e dos nomes de arquivos.

Quanto mais consistentes forem:
- nomes de arquivos
- comentários de topo
- exports
- separação por responsabilidade

mais preciso o mapa fica.
