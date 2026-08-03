# Estudo de Estilo, Estrutura e Linguagem da Introdução — Padrão NCA

Este documento consolida o **estudo minucioso de linguagem, retórica e progressão textual** realizado sobre as introduções dos artigos do *Neural Computing and Applications (NCA)* e dos artigos precursores do nosso grupo.

---

## 1. O Modelo Retórico CARS (Creating A Research Space) no NCA

Os artigos de alto impacto do NCA (como Dhingra et al., 2025) seguem a estrutura de 5 movimentos retóricos (*rhetorical moves*):

```
[Move 1: Território] → [Move 2: Soluções de ML] → [Move 3: Isolamento do Otimizador] → [Move 4: Gap & Open Issues] → [Move 5: 6 Contribuições]
```

### Move 1: Estabelecendo o Território (Parágrafo 1)
- **Objetivo**: Conectar a relevância prática imediata do domínio (mercados futuros intraday de alta frequência) com a complexidade computacional do problema.
- **Estrutura de Frases Padrão NCA**:
  - *"Financial asset price forecasting in high-frequency intraday environments represents one of the most challenging applications of computational intelligence [Ref]."*
  - *"In modern futures markets, such as the Brazilian Mini-Index (WIN), market participants face rapid regime transitions, low signal-to-noise ratios, and severe non-stationarity."*
- **Técnica Textual**: Usar conectivos de necessidade: *"Achieving reliable predictive signals under sub-hourly resolutions is crucial for..."*

### Move 2: Apresentando o Papel das Redes Neurais (Parágrafo 2)
- **Objetivo**: Apresentar os modelos neurais (MLP, feedforward) e a complexidade do espaço de busca.
- **Estrutura de Frases Padrão NCA**:
  - *"Multilayer Perceptrons (MLPs) possess strong universal function approximation capabilities... However, predictive performance depends critically on hyperparameter configuration..."*
  - *"While gradient-descent algorithms update internal weight parameters, hyperparameter tuning requires navigating complex, discrete-continuous, multimodal landscapes where gradient information is unavailable."*

### Move 3: Isolando o Otimizador como Objeto de Estudo (Parágrafo 3)
- **Objetivo**: Transitar da rede neural para a **meta-heurística de otimização**.
- **Estrutura de Frases Padrão NCA**:
  - *"To overcome manual trial-and-error or brute-force grid search, metaheuristic algorithms have gained widespread adoption..."*
  - *"In particular, evolutionary algorithms (GA, DE) and swarm intelligence algorithms (PSO, GWO) offer distinct exploration-exploitation mechanics..."*

### Move 4: Articulando a Lacuna (The Research Gap & Open Issues) (Parágrafos 4 & 5)
- **Objetivo**: Mostrar por que a literatura atual é insuficiente e listar as lacunas abertas.
- **Estrutura de Frases Padrão NCA**:
  - *"However, prior research overwhelmingly focuses on tuning neural networks using a single, arbitrarily selected optimizer (most commonly a standard GA or Grid Search)..."*
  - *"Consequently, the comparative effectiveness, convergence behavior, and stability of different optimizer families under real-world financial constraints remain significantly underexplored."*
  - *"A synthesis of the studies in Table 1 reveals four primary open issues: 1... 2... 3... 4..."*

### Move 5: Apresentando o Benchmark e as 6 Contribuições (Lista Numerada)
- **Objetivo**: Anunciar a solução do artigo com autoridade e clareza.
- **Estrutura de Frases Padrão NCA**:
  - *"Addressing these gaps, this paper reframes the problem into a controlled benchmark study of five distinct optimizer algorithms..."*
  - *"The main contributions of this work are summarized as follows: 1. Controlled Equal-Budget... 2. Leakage-Free Temporal Validation... 3. Robust Classification Optimization... 4. Multi-Seed Statistical Analysis... 5. Convergence Dynamics... 6. Economic Value & Cost Sensitivity."*

---

## 2. Comparativo de Linguagem: IJCNN vs. NCA

| Aspeto Textual | Linguagem no Artigo IJCNN (Rejeitado) | Linguagem Padrão NCA (Novo Manuscrito) |
|---|---|---|
| **Foco Inicial** | Genérico sobre mercado financeiro (*"The financial market is the arena for investing..."*) | Direto e técnico (*"Financial asset price forecasting in high-frequency intraday environments represents..."*) |
| **Justificativa do Otimizador** | Trata o GA apenas como uma ferramenta acessória (*"GA has been used in this context..."*) | Trata o otimizador como **objeto central do estudo científico** (*"Optimizers are critical components that control weight updates, stability, and generalization..."*) |
| **Apresentação de Trabalhos Anteriores** | Resumo narrativo corrido | **Tabela de Literatura (Table 1)** contrastando modelo, otimizador, dados e **limitações reportadas**. |
| **Declaração de Contribuição** | Texto corrido único ao final da introdução | Lista numerada formal com **6 contribuições claras e destacadas em negrito**. |
| **Articulação do Problema Metodológico** | Silencioso sobre data leakage e orçamento computacional | Denúncia explícita dos vícios da literatura: data leakage temporal, acurácia isolada e falta de orçamento idêntico. |

---

## 3. Checklist de Rigor Acadêmico para a Escrita

- [x] Toda afirmação de limitação da literatura é ancorada em citação ou demonstrada na Tabela 1.
- [x] O termo *"controlled benchmark under equal budget"* é reforçado ao longo do texto.
- [x] A validação temporal 60/20/20 sem *data leakage* é explicitada na introdução como contribuição fundamental.
- [x] A métrica de fitness (MCC + F1) é apresentada como a alternativa robusta à acurácia simples.
- [x] O encadeamento das seções (*paper outline*) encerra a introdução de forma padronizada.
