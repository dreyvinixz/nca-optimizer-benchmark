# Official Benchmark V1 Status

Este documento registra a configuração base (Baseline) validada do projeto para testes de meta-heurísticas aplicadas a classificação de tendências intradiárias. Este marco congela as configurações para análise estatística oficial antes de escalonamento massivo (1000 gerações) ou da inclusão de novos algoritmos.

## 1. Protocolo Experimental
- **Official Experiment**: Sim (Auditoria ativada no tracking).
- **Backend Oficial**: TensorFlow/Keras (`keras.Sequential` com backpropagation).
- **Modelo de Machine Learning**: Multilayer Perceptron (MLP).
- **Loss**: Binary Crossentropy.
- **Max Epochs**: 10 (com Early Stopping Patience = 3).
- **Paralelização**: Joblib com backend `loky` em multiprocessamento. O Keras é limitado via `os.environ` a 1 thread intra/interop para evitar contenção de CPU.
- **Cache**: Implementado cache pareado por semente/algoritmo/hiperparâmetros/split.

## 2. Dataset e Seleção de Atributos
- **Target**: `trend` (0: Downtrend, 1: Uptrend).
- **Features Selecionadas**: InfoGain_7 (índices `[30, 52, 31, 53, 42, 33, 41]`).
- **Split Temporal**: 60% Train, 20% Validation, 20% Test.
- **Regras do Split**: Estritamente cronológico, *sem shuffle*, com pré-escalonamento (`StandardScaler`) *fitado apenas no conjunto de treino* e transformado nos demais.

## 3. Otimizadores e Configurações (Budget Igualado)
Todos os otimizadores estão rodando com um **budget equivalente de 100 avaliações por seed**.
- **Sementes (Seeds) atuais**: `[42, 123, 2024, 2025, 777]`.

### Algoritmos Atuais:
- **Random Search**: Baseline cego (100 evaluations per seed).
- **Genetic Algorithm (GA)**: Population = 10, Generations = 10 (Total: 100 evaluations).
  - Crossover: 80%, Mutation: 20%, Tournament: 3.
- **Particle Swarm Optimization (PSO)**: Particles = 10, Iterations = 10 (Total: 100 evaluations).
  - Inertia: 0.70, Cognitive: 1.50, Social: 1.50.

## 4. Função Objetivo (Fitness)
Centralizada em `src/objective.py`.
- **Fórmula**: `0.60 * MCC + 0.40 * F1`.
- O cálculo usa limiar de classificação em `0.50`.
- É validada unicamente nos dados de *Validation*, guiando as meta-heurísticas para não superajustarem no *Test*.

## 5. Resultados Atuais Observados
Com os experimentos na base atual de 5 sementes, PSO e GA demonstraram (ganho observado):
- **achieved higher observed performance** em métricas rigorosas como MCC e AUC-PR no conjunto de teste em comparação ao Random Search.
- Nota Importante: Devido ao número restrito de observações/sementes e do orçamento fixo atual (100 avaliações), a superioridade estatisticamente significativa ainda necessita de confirmação via Análise Pareada ou testes de *Bootstrap*.

## 6. Limitações Desta Versão
1. **Budgets curtos**: 100 avaliações é um número muito baixo para observar convergência massiva de enxames ou genéticos.
2. **Número de Sementes**: 5 amostras independentes dificultam testes de Wilcoxon (n < 6). Métodos de reamostragem (Bootstrap) são necessários.
3. **Ausência de algoritmos avançados**: DE e GWO ainda não estão presentes nesta V1.

## 7. Próximos Passos
1. **Análise Estatística**: Rodar scripts para extrair intervalos de confiança (*Bootstrap CI*) e confirmar a robustez das diferenças.
2. **Expansão de Otimizadores**: Adicionar DE e GWO após validação estatística da arquitetura atual.
3. **Escalonamento Horizontal**: Aumentar budget (ex: 1.000 avaliações/gerações) e sementes (ex: 30) para dados publicáveis finais.
