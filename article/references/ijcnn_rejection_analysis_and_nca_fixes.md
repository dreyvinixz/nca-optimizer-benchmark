# Análise do Artigo Precursor IJCNN 2026 e Correções Aplicadas no Manuscrito NCA

Este documento analisa as limitações metodológicas do artigo precursor submetido ao IJCNN (*Combining Technical Indicators and Genetic Algorithms for Short-Term Machine Learning Prediction of Mini-Index Futures*) e detalha como cada ponto fraco foi superado no novo manuscrito para o **Neural Computing and Applications (NCA)**.

---

## 1. Mapeamento de Limitações vs. Soluções no NCA

| Componente | Abordagem no IJCNN 2026 | Solução Implementada no Novo Artigo (NCA) |
|---|---|---|
| **Divisão de Dados** | Amostragem aleatória (3.000 instâncias sorteadas para treino e 12.057 para teste) + 5-fold Cross-Validation. | **Validação Temporal Estrita (60/20/20)** em ordem cronológica contínua. Eliminação total de *data leakage* e quebra de autocorrelação. |
| **Otimizadores Avaliados** | Apenas Algoritmo Genético (GA) testado em 3 classificadores (RF, SVM, MLP). | **Benchmark Controlado com 5 Otimizadores**: Random Search (RS), Genetic Algorithm (GA), Particle Swarm Optimization (PSO), Differential Evolution (DE) e Grey Wolf Optimizer (GWO). |
| **Orçamento Computacional** | Orçamento desigual (10 indivíduos $\times$ 1.000 gerações em 5-folds = 50.000 avaliações potenciais, resultando em 18h de execução para o MLP). | **Orçamento Computacional Idêntico e Controlado** ($N_{eval} = 1.500$ avaliações fixas por seed para todos os otimizadores). |
| **Métrica de Fitness** | Acurácia simples do 5-fold cross-validation. | **Fitness Composto baseada no MCC**: $f(\boldsymbol{\theta}) = 0.60 \times \text{MCC} + 0.40 \times F_1$. O MCC corrige distorções de desbalanceamento de classes e falsos positivos. |
| **Análise Estatística** | Nenhuma análise estatística formal de significância (apenas médias diretas). | **Testes Não-Paramétricos de Hipóteses**: Teste de Friedman + Testes Pareados de Wilcoxon com correção de Holm-Bonferroni e tamanho de efeito $d$ de Cohen. |
| **Avaliação Econômica / Financeira** | Ausente (avaliação restrita a métricas preditivas sem simulador de trading). | **Backtest Financeiro Completo**: Modelo de trading intraday em WIN futuros medindo Retorno Líquido, Índice Sharpe, Drawdown Máximo (MDD), Profit Factor e sensibilidade aos custos de transação. |

---

## 2. Enquadramento e Narrativa Científica no Manuscrito NCA

Na seção de **Trabalhos Relacionados** e **Introdução** do artigo NCA, a linhagem de pesquisa é apresentada com o devido rigor acadêmico:

> *"Preliminary conference precursors investigated feature selection via Information Gain for Random Forest models on Brazilian mini-index futures [Souza et al., ICCSA 2025] and explored GA-based hyperparameter tuning for Random Forest, SVM, and MLP classifiers [Souza et al., 2026]. However, these initial studies evaluated a single optimizer under randomized cross-validation without temporal constraints. The present work substantially advances this research lineage by establishing a leakage-free temporal validation protocol, enforcing equal evaluation budgets across five distinct evolutionary and swarm optimizer families, conducting non-parametric statistical hypothesis testing, and evaluating out-of-sample economic utility under realistic transaction costs."*

---

## 3. Síntese dos Autores e Afiliações Integrados ao Proyecto

- **Primeiros Autores**: Andrey V. S. Souza (Co-primeiro autor), Bruno L. Dalmazo (Autor Correspondente e Co-primeiro autor)
- **Equipe de Pesquisa**: Viviane L. D. de Mattos, Richard F. Pinto, Diego R. Bruno, Eduardo N. Borges, Giancarlo Lucca, Fabian C. Cardoso, Rafael A. Berri
- **Instituições**: Universidade Federal do Rio Grande (FURG), Universidade Estadual Paulista (UNESP), Universidade de Rio Verde (UniRV)
- **Financiamentos Registrados**: FAPERGS (Grants 24/2551-0001396-2 e 23/2551-0000773-8), CNPq (Grant 307416/2025-9), FAPERGS/CNPq (Grant 23/2551-0000126-8) e Fesurv/UniRV.
