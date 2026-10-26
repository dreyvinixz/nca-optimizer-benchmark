# Plano de tarefas — estudo multi-escala B0

**Status geral:** Fases 0–6 concluídas; Fase 7 dispensada pelo critério condicional; Fase 8 concluída como rascunho interno e pacote reproduzível. O teste final foi aberto uma vez sob pré-registro. *Journal of Forecasting* foi avaliado como alvo de trabalho. Submissão externa não faz parte desta entrega.
**Branch:** `feat/one-minute-labels-clean`  
**Roadmap científico:** [ROADMAP_ONE_MINUTE_LABELS.md](ROADMAP_ONE_MINUTE_LABELS.md)

Este checklist transforma o roadmap em trabalho executável. Marque uma tarefa como concluída somente quando o artefato ou evidência indicado estiver disponível. Não avance para treinamento antes de aprovar as Fases 0–3.

## Regras de execução

- [x] Usar o checkout atual e o WSL2 existente; não criar outro clone/checkout nem copiar `.venv_wsl`.
- [x] Ler em modo somente leitura os SQLite locais `data/bovdb-labels-B4-v1.sqlite` e `data/bovdb-v3.1-internal.2.sqlite`; mantê-los ignorados pelo Git e não alterar/converter as origens.
- [x] Só criar cache derivado (Parquet) após medir o gargalo e congelar o contrato dos dados; registrar custo e tamanho.
- [x] Manter a auditoria inicial em leitura somente e registrar hash/proveniência dos insumos.
- [x] Não versionar dados, bases derivadas, predições completas, checkpoints ou caches pesados.
- [x] Registrar configurações, seeds, versões, orçamento, logs e resumos pequenos suficientes para reproduzir cada resultado.
- [x] Tratar os alvos B0 como referências relativas: sem referência independente, não declarar ground truth, direção real do mercado, incerteza epistêmica ou lucro executável.
- [x] Manter o manuscrito NCA anterior de 5 minutos separado deste estudo.

## Fase 0 — Ambiente e proveniência

**Objetivo:** confirmar a proveniência dos SQLite locais e a funcionalidade do ambiente, mantendo as bases de origem inalteradas.

- [x] Confirmar branch ativa, registrar commit base e descrever o estado do Git (inclusive arquivos de auditoria ainda não versionados).
- [x] Ativar o ambiente existente com `source scripts/wsl_cuda_env.sh`.
- [x] Registrar versões de Ubuntu/WSL, Python, TensorFlow, CUDA/cuDNN e bibliotecas relevantes.
- [x] Verificar `nvidia-smi` e listar GPUs reconhecidas por `tf.config.list_physical_devices("GPU")`.
- [x] Verificar memória e espaço livre nos diretórios de código, ambiente e temporários.
- [x] Confirmar acesso somente leitura aos dois SQLite e que `data/` continua ignorada pelo Git.
- [x] Registrar hashes dos dois arquivos e conferir se o hash da origem corresponde a `source_sha256` em `label_run` do B4.
- [x] Localizar e validar o manifesto correspondente; se não estiver disponível, registrar a lacuna e usar os metadados internos do B4 sem inventar proveniência.
- [x] Confirmar que o ambiente WSL e o venv existentes estão funcionais.

**Entregáveis:** [reports/environment.md](reports/environment.md) com comandos, versões, espaço livre, caminhos locais, hashes e limitações; bancos de origem inalterados.
**Saída da fase:** ambiente funcional, origem identificada e espaço de execução definido.

## Fase 1 — Auditoria dos rótulos (somente leitura)

**Objetivo:** descrever cobertura e comportamento dos rótulos antes de escolher amostra, cortes ou modelos.

- [x] Inspecionar esquema, tipos, chaves, timestamps e limites temporais da base/manifesto.
- [x] Contar candles, pregões, tickers, raízes futuras e contratos por período.
- [x] Auditar duplicatas, ordenação, lacunas temporais e minutos ausentes por raiz/pregão.
- [x] Medir nulos e cobertura de `trend_5m`, `trend_10m`, `trend_15m` e `trend_mean` por raiz e pregão.
- [x] Medir prevalência de classes e duração/comprimento de segmentos por alvo, raiz e pregão.
- [x] Medir mudanças de classe e concordância entre escalas por raiz e pregão.
- [x] Recalcular `trend_mean` como média/voto dos três alvos disponíveis e verificar a regra de maioria nas linhas elegíveis.
- [x] Registrar linhas excluídas e divergências entre manifesto, banco e rótulos; não corrigir a base nesta fase.
- [x] Gerar tabelas pequenas reproduzíveis e um resumo descritivo com contagens por pregão independente.

**Entregáveis:** [scripts/audit_labels.py](scripts/audit_labels.py), [reports/label_audit.md](reports/label_audit.md) e [reports/label_audit_by_root_session.csv](reports/label_audit_by_root_session.csv).
**Saída da fase:** inconsistências explicadas e cobertura suficiente para congelar a população do estudo.

## Fase 2 — Contrato dos dados e protocolo

**Objetivo:** congelar as decisões de amostragem antes de consultar resultados de teste.

- [x] Selecionar universo pela mediana diária de `amount_stock`, número de negócios e sessões observadas: WIN/IND no núcleo; demais raízes fora do estudo confirmatório atual.
- [x] Excluir WDO, WSP e ISP: não há candles `price1` nem rótulos B4 para essas raízes na fotografia local; CCMF/BGIG também ficam fora do universo confirmatório por liquidez menor.
- [x] Definir contratos como séries independentes por ticker, sem costura/ajuste contínuo; estados de feature reiniciam por contrato e pregão. Contratos do mesmo pregão ficam no mesmo split.
- [x] Definir chave `(ticker,date,time)`, decisão após o fechamento do candle de um minuto e pareamento do rótulo B0 no mesmo timestamp, sem shift.
- [x] Registrar que previsão da próxima sessão não faz parte da hipótese atual; se virar hipótese futura, exigirá contrato separado por próximo pregão/horário.
- [x] Registrar que B0 é retrospectivo; treino só pode usar rótulos depois de concluído o pregão, e o resultado é previsão de rótulo, não sinal causal de mercado.
- [x] Fixar política: sem minutos sintéticos ou forward-fill; lacunas reiniciam janelas; duplicatas falham; janelas limitadas a 09:00–18:00; rótulos nulos são mascarados por cabeça.
- [x] Reutilizar a auditoria B4 concluída na Fase 1 para os registros já presentes; não regenerar nem repetir a auditoria global ao selecionar raízes. Para novos símbolos incluídos, auditar apenas os rótulos novos.
- [x] Definir alvos individuais, máscara por alvo, interseção comum e regra do alvo de maioria.
- [x] Definir `mean_score` como alvo suave determinístico da fração de votos, sem interpretá-lo como probabilidade verdadeira.
- [x] Listar colunas/indicadores permitidos e proibidos; excluir SIDEWAYS, endpoints e qualquer coluna derivada de B4 das entradas.
- [x] Definir população confirmatória local: WIN/IND, 2026-01-02 a 2026-06-30, com exclusões/limites documentados nos relatórios.
- [x] Escrever e revisar `config/data_contract.yaml` e `config/experiment_protocol.yaml`.
- [x] Congelar os arquivos de protocolo em commit antes de abrir/usar métricas de teste; nenhum resultado de modelo ou métrica de teste foi consultado.

**Entregáveis:** [scripts/audit_futures_liquidity.py](scripts/audit_futures_liquidity.py), [relatório de liquidez](reports/futures_liquidity.md), contrato de dados e protocolo versionados, com proveniência e justificativas.
**Saída da fase:** decisões analíticas pré-registradas e revisadas.

## Fase 3 — Features causais e splits temporais

**Objetivo:** construir entradas sem vazamento e validação cronológica comparável.

- [x] Inspecionar o gerador B4: rótulos são atribuídos ex post até `segment_end_time`; B4 é limitado a uma sessão.
- [x] Especificar janelas retrospectivas de OHLCV/atividade disponíveis após o fechamento do candle da linha.
- [x] Definir retornos de 1/5/15 linhas consecutivas, corpo/amplitude, volatilidade populacional de 5/15/30 retornos e logs de volume/negócios/quantidade, com aquecimento completo.
- [x] Implementar e auditar indicadores sem usar rótulos, SIDEWAYS ou campos derivados de B4 como entradas.
- [x] Medir a extração após corrigir afinidade SQLite em `(id_ticker,date,time)`; cache Parquet seletivo de 12,6 MB criado para WIN/IND.
- [x] Implementar o pareamento B0 no mesmo `(ticker,date,time)`; nenhuma linha/dia seguinte é usada.
- [x] Confirmar por auditoria que os endpoints não atravessam o pregão, portanto nenhum segmento B4 cruza as datas de corte; janelas de features reiniciam em gaps/contratos/pregões.
- [x] Definir quatro folds expanding por pregão, somente no período de desenvolvimento e sem datas do teste.
- [x] Ajustar `StandardScaler` somente nos dados de treino de cada fold, dentro do pipeline; excluir janelas de feature incompletas, sem imputação.
- [x] Separar treino/validação/teste cronologicamente, por data comum a todos os instrumentos e sem shuffle.
- [x] Criar auditorias automáticas de colunas, chaves, fronteiras, endpoints, gaps e datas de folds.
- [x] Conferir as datas de corte/folds e a cobertura por ticker em `reports/leakage_audit.md`.

**Entregáveis:** código/configuração de features e splits, manifesto dos folds e `reports/leakage_audit.md`.  
**Saída da fase:** auditoria de vazamento aprovada e cortes congelados antes do treinamento.

## Fase 4 — Piloto de capacidade e baselines

**Objetivo:** medir custo local e estabelecer referências simples antes da comparação multitarefa.

- [x] Manter métricas compactas em `reports/` e o cache de dados em `data/derived/` ignorado pelo Git; não salvar checkpoints/predições volumosas.
- [x] Rodar piloto curto de CPU em quatro folds expanding e duas raízes, com features completas.
- [x] Registrar custo do MLP/GPU (tempo por época, throughput, RAM, pico de VRAM e estabilidade) em [mlp_pilot.md](reports/mlp_pilot.md) e no JSON do CV.
- [x] Revalidar a GTX 1650 Max-Q de 4 GB e dimensionar piloto em batch 256/MLP 11–32–16–1; o pico permaneceu bem abaixo da VRAM disponível.
- [x] Implementar classe majoritária e momentum causal; persistência do rótulo anterior foi excluída porque o B4 não registra o horário de confirmação/observabilidade.
- [x] Implementar baseline de regressão logística com padronização ajustada só no treino de cada fold.
- [x] Implementar baseline de árvore CPU com `HistGradientBoostingClassifier` do scikit-learn; LightGBM/XGBoost não estão instalados.
- [x] Implementar e avaliar um MLP compacto nos quatro folds; sem busca ampla de hiperparâmetros.
- [x] Avaliar separadamente os três alvos e o alvo de maioria nos mesmos quatro folds de validação.
- [x] Registrar MCC, balanced accuracy, macro-F1, prevalência, cobertura, matrizes de confusão e custo em [baseline_cv.md](reports/baseline_cv.md) e CSV.

**Entregáveis:** configuração do piloto, logs e tabela resumida de custo/desempenho por modelo e alvo.  
**Saída da fase:** orçamento de execução e baselines reproduzíveis aprovados.

## Fase 5 — Modelos multi-escala e discordância

**Objetivo:** comparar estratégias pareadas nas mesmas amostras e cortes.

- [x] Fixar seed 20261026, cinco épocas, batch 256, arquitetura 11–32–16–1 e sem busca; nenhuma métrica do teste foi consultada.
- [x] Treinar três modelos independentes, um por escala, nos quatro folds.
- [x] Treinar encoder compartilhado com três cabeças 5/10/15m e pesos/máscaras para rótulos nulos.
- [x] Treinar comparação com alvo duro de maioria.
- [x] Treinar regressão para `mean_score` e comparar com baseline da média do treino.
- [x] Registrar votos positivos, unanimidade e discordância entre escalas nas predições temporárias.
- [x] Medir aceitação seletiva por unanimidade das três saídas preditas, sempre junto com cobertura; tabelas de estratos pelo rótulo B0 ficam marcadas como descritivas, indisponíveis na inferência.
- [x] Comparar arquiteturas na interseção comum e reportar cobertura por cabeça quando há rótulos ausentes.
- [x] Usar os mesmos folds/datas/features/orçamento entre modelos pareados; seeds determinísticas registradas.
- [x] Manter predições em `tmp/` (ignorado pelo Git) e versionar somente tabelas/relatórios pequenos.

**Entregáveis:** configurações, logs, tabela comparativa pareada e resumo de cobertura/discordância.  
**Saída da fase:** comparação completa sem apresentar votos como probabilidades ou verdade independente.

## Fase 6 — Generalização e inferência

**Objetivo:** estimar estabilidade entre pregões, blocos temporais e raízes.

- [x] Repetir comparações nos blocos temporais e raízes definidos no protocolo; também manter resumos descritivos por contrato.
- [x] Calcular MCC, balanced accuracy e macro-F1 por cabeça/alvo, raiz e bloco em [final_test_metrics.csv](reports/final_test_metrics.csv).
- [x] Estimar intervalos pareados com bootstrap circular de blocos de cinco sessões e 10.000 replicações; candles não são tratados como replicações independentes.
- [x] Aplicar Wilcoxon por sessão e Holm aos três alvos no desenvolvimento; não reportar valores-p no teste, conforme pré-registro.
- [x] Reportar diferenças pareadas observadas e intervalos; os três intervalos independentes-vs-compartilhado incluem zero.
- [x] Avaliar Brier e log-loss em saídas probabilísticas; não aplicar ajuste de calibração.
- [x] Fazer análises por raiz, bloco, cobertura de cada alvo e contrato, conforme escopo; ver [final_test_contract_metrics.csv](reports/final_test_contract_metrics.csv).
- [x] Avaliar gap aparente treino–validação, estabilidade entre folds e sessões, e variação por bloco/raiz/contrato sem ajuste baseado no teste; ver [overfitting_assessment.md](reports/overfitting_assessment.md).
- [x] Registrar o resultado nulo da comparação principal, exclusões e limitações em [final_test.md](reports/final_test.md).

**Entregáveis:** tabelas de inferência e generalização, scripts de análise e relatório de limitações.  
**Saída da fase:** afirmações restritas ao período, universo e protocolo efetivamente avaliados.

## Fase 7 — Extensões opcionais (condicionais)

**Só iniciar se** a Fase 5 mostrar sinal útil, houver orçamento local e a extensão tiver hipótese própria e ablação planejada.

- [x] Registrar por escrito a decisão condicional: nenhuma extensão atende ao gate de sinal útil; ver [phase7_decision.md](reports/phase7_decision.md).
- [x] Formalizar a Fase 7 como não executada para esta versão do estudo; nenhuma hipótese adicional foi aberta depois do teste.
- [x] Manter pré-treino, encoder temporal e adaptação de regime fora do escopo atual.

**Entregáveis:** decisão documentada e, se executada, protocolo, ablação e relatório reproduzível.  
**Saída da fase:** extensão opcional concluída com evidência ou formalmente descartada.

## Fase 8 — Artigo e pacote reproduzível

**Objetivo:** escrever conclusões rastreáveis aos dados, código e resultados realmente produzidos.

- [x] Escrever novo rascunho em [manuscript/multiscale_b0_label_prediction_draft.md](manuscript/multiscale_b0_label_prediction_draft.md), mantendo o manuscrito NCA anterior separado.
- [x] Documentar método, proveniência, contrato, protocolo temporal e tratamento de rótulos ausentes.
- [x] Preparar tabelas reproduzíveis por modelo, raiz, bloco e contrato; os artefatos completos estão em `reports/`.
- [x] Ligar números do rascunho às configurações, scripts e saídas listados no mapa de artefatos do manuscrito.
- [x] Explicitar que B0 não é verdade-terreno independente e que discordância entre rótulos não é incerteza epistêmica.
- [x] Explicitar ausência de avaliação executável de lucro, escopo temporal jan–jun/2026, dados internos e cobertura insuficiente de B1/B2/Fuzzy.
- [x] Revisar alegações, vazamento, dependência por sessão, comparações múltiplas e limites de disponibilidade.
- [x] Reproduzir as tabelas a partir das predições finais salvas com `scripts/summarize_final_test.py`; o script suplementar não retreina nem reavalia modelos.
- [x] Escolher um alvo de trabalho provisório com base em escopo e requisitos oficiais; ver [journal_target_assessment.md](reports/journal_target_assessment.md).
- [x] Preparar [title_page_template.md](manuscript/title_page_template.md) com os campos exigidos sem inventar autores, vínculos, ORCID, financiamento ou declarações.
- [x] Revisar os requisitos editoriais do alvo de trabalho e registrar os campos que dependem dos autores/titular dos dados; manter submissão fora do escopo desta entrega interna.

**Entregáveis:** manuscrito e pacote mínimo de reprodução/documentação compatível com o status interno dos dados.  
**Saída da fase:** nenhuma afirmação numérica sem rastreabilidade e todas as limitações materiais declaradas.

## Critério de conclusão do projeto

- [x] Fases 0–6 concluídas com critérios de saída atendidos.
- [x] Fase 7 explicitamente descartada com justificativa.
- [x] Rascunho interno da Fase 8 preparado e reproduzido a partir dos artefatos documentados; avaliação do alvo editorial registrada.
- [x] Repositório contém código, configurações, documentação e resumos pequenos; dados e saídas pesadas permanecem externos/temporários.
- [x] `git status` revisado para confirmar que nenhum banco, predição completa, checkpoint ou cache foi incluído no commit; uma alteração alheia no CSV da auditoria foi preservada sem staging.

## Etapa posterior, se houver submissão externa

O estudo interno está concluído. Uma submissão futura exigirá confirmar autores e ordem, afiliações, ORCIDs, financiamento/conflitos e autorização do titular dos dados para divulgar resultados agregados/código. Esses dados não foram inferidos nem inventados.
