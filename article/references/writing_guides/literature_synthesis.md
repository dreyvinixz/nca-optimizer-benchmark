# Síntese da Literatura de Referência — Manuscrito NCA

Este documento mapeia os artigos fundamentais trazidos de `D:\tese` e os conecta diretamente com as seções do nosso artigo para o journal **Neural Computing and Applications (NCA)**.

---

## 1. Mapeamento de Papéis Chave

### Paper 1: PSO Systematic Review (2022)
- **Arquivo**: `2022_particle_swarm_optimization_algorithm_and_its_applications_a_systematic_review.pdf`
- **Autores / Veículo**: Ahmed G. Gad (2022) — *Archives of Computational Methods in Engineering*
- **DOI**: `10.1007/s11831-021-09694-4`
- **Tópicos Chave**:
  - Classificação e taxonomia de variantes do PSO (Standard PSO, Adaptive PSO, Hybrid PSO).
  - Aplicações de PSO no treinamento e ajuste de pesos/hiperparâmetros de Redes Neurais (MLP, RBF, CNN).
  - Parâmetros críticos: Inércia ($w$), coeficientes cognitivo ($c_1$) e social ($c_2$).
- **Uso no Manuscrito**:
  - `sections/related_work.tex` (Subseção 2.1 — Metaheuristic Optimization for Neural Networks).
  - `sections/methodology.tex` (Subseção 4.3.3 — PSO formulation and boundary handling).

---

### Paper 2: PSO Comprehensive Survey (2022/2018)
- **Arquivo**: `2022_particle_swarm_optimization_a_comprehensive_survey.pdf`
- **Autores / Veículo**: Wang et al. / Gad
- **Tópicos Chave**:
  - Análise de convergência e estagnação em ótimos locais.
  - Comparação de desempenho entre PSO, Algoritmos Genéticos (GA) e Busca Aleatória (RS).
  - Trade-off entre exploração global e explotação local.
- **Uso no Manuscrito**:
  - `sections/introduction.tex` (Justificativa do gap de comparação controlada).
  - `sections/discussion.tex` (Análise de convergência vs estabilidade).

---

### Paper 3: Exhaustive Metaheuristics Review (2023)
- **Arquivo**: `2023_an_exhaustive_review_of_the_metaheuristic_algorithms_for_search_and_optimization_taxonomy_applicatio.pdf`
- **Autores / Veículo**: Kamal Rajwar, Kusum Deep, Swagatam Das (2023) — *Artificial Intelligence Review*
- **DOI**: `10.1007/s10462-023-10470-y`
- **Tópicos Chave**:
  - Taxonomia completa de meta-heurísticas (Evolution-based, Swarm-based, Physics-based, Human-based).
  - Enquadramento do GA e DE na família evolutiva, e do PSO e GWO na família swarm.
  - Protocolos de benchmark rigorosos: necessidade de orçamento computacional idêntico (number of function evaluations).
- **Uso no Manuscrito**:
  - `sections/related_work.tex` (Subseção 2.3 — Benchmark Studies and Fair Protocol).
  - `sections/methodology.tex` (Subseção 4.4 — Equal Evaluation Budget Protocol).

---

### Paper 4: Grey Wolf Optimizer Review (2023/2018)
- **Arquivo**: `2023_recent_advances_in_grey_wolf_optimizer_its_versions_and_applications_review.pdf`
- **Autores / Veículo**: Faris et al. / Advances in GWO
- **Tópicos Chave**:
  - Mecanismo de liderança hierárquica ($\alpha, \beta, \delta$).
  - Desempenho do GWO em tarefas de seleção de atributos e otimização de hyperparameters de redes neurais.
  - Eficiência de convergência inicial vs risco de perda de diversidade da população.
- **Uso no Manuscrito**:
  - `sections/methodology.tex` (Subseção 4.3.5 — GWO formulation).
  - `sections/discussion.tex` (Comparação Swarm vs Evolutionary).

---

### Paper 5: Evolutionary Neural Architecture Search Survey (2023)
- **Arquivo**: `2023_a_survey_on_evolutionary_neural_architecture_search.pdf`
- **Autores / Veículo**: Survey on ENAS
- **Tópicos Chave**:
  - Algoritmos evolutivos na busca de topologias e hiperparâmetros de redes neurais.
  - Operadores de mutação e crossover aplicados a vetores de hiperparâmetros discretos e contínuos.
  - Prevenção de overfitting em validações temporais/financeiras.
- **Uso no Manuscrito**:
  - `sections/related_work.tex` (Subseção 2.1 e 2.2).
  - `sections/limitations.tex` (Limitações de busca de arquitetura vs hiperparâmetros fixos de topo).

---

## 2. Linha do Tempo e Enquadramento Científico do Manuscrito

```
[ICCSA 2025] Seleção de Atributos com RF (InfoGain) 
     │
     ▼
[IJCNN 2026] Otimização de Hiperparâmetros com GA (RF, SVM, MLP)
     │
     ▼
[NCA Journal 2026] Controlled Benchmark of Evolutionary & Swarm Optimizers for Neural Trend Classification
     ├─ Orçamento computacional idêntico (Equal Budget)
     ├─ Validação Temporal sem Data Leakage (60/20/20)
     ├─ 5 Otimizadores: RS, GA, PSO, DE, GWO
     ├─ Métricas de Classificação Robustas (MCC, F1, AUC-PR) + Testes Estatísticos (Friedman / Wilcoxon-Holm)
     └─ Avaliação de Impacto Financeiro (Sharpe, MDD, Cost Sensitivity)
```
