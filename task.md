# Plano de tarefas — estudo multi-escala B0

**Status geral:** planejamento; nenhum treinamento deste estudo foi iniciado.  
**Branch:** `feat/one-minute-labels-clean`  
**Roadmap científico:** [ROADMAP_ONE_MINUTE_LABELS.md](ROADMAP_ONE_MINUTE_LABELS.md)

Este checklist transforma o roadmap em trabalho executável. Marque uma tarefa como concluída somente quando o artefato ou evidência indicado estiver disponível. Não avance para treinamento antes de aprovar as Fases 0–3.

## Regras de execução

- [ ] Usar o checkout atual e o WSL2 existente; não criar outro clone/checkout nem copiar `.venv_wsl`.
- [ ] Ler em modo somente leitura os SQLite locais `data/bovdb-labels-B4-v1.sqlite` e `data/bovdb-v3.1-internal.2.sqlite`; mantê-los ignorados pelo Git e não alterar/converter as origens.
- [ ] Só criar cache derivado (Parquet, memmap ou TFRecord) após medir o gargalo e congelar o contrato dos dados; registrar custo e tamanho.
- [ ] Manter a auditoria inicial em leitura somente e registrar hash/proveniência dos insumos.
- [ ] Não versionar dados, bases derivadas, predições completas, checkpoints ou caches pesados.
- [ ] Registrar configurações, seeds, versões, orçamento, logs e resumos pequenos suficientes para reproduzir cada resultado.
- [ ] Tratar os alvos B0 como referências relativas: sem referência independente, não declarar ground truth, direção real do mercado, incerteza epistêmica ou lucro executável.
- [ ] Manter o manuscrito NCA anterior de 5 minutos separado deste estudo.

## Fase 0 — Ambiente e proveniência

**Objetivo:** confirmar a proveniência dos SQLite locais e a funcionalidade do ambiente, mantendo as bases de origem inalteradas.

- [ ] Confirmar branch ativa e estado limpo do Git; registrar commit base.
- [ ] Ativar o ambiente existente com `source scripts/wsl_cuda_env.sh`.
- [ ] Registrar versões de Ubuntu/WSL, Python, TensorFlow, CUDA/cuDNN e bibliotecas relevantes.
- [ ] Verificar `nvidia-smi` e listar GPUs reconhecidas por `tf.config.list_physical_devices("GPU")`.
- [ ] Verificar memória e espaço livre nos diretórios de código, ambiente e temporários.
- [ ] Confirmar acesso somente leitura aos dois SQLite e que `data/` continua ignorada pelo Git.
- [ ] Registrar hashes dos dois arquivos e conferir se o hash da origem corresponde a `source_sha256` em `label_run` do B4.
- [ ] Localizar e validar o manifesto correspondente; se não estiver disponível, registrar a lacuna e usar os metadados internos do B4 sem inventar proveniência.
- [ ] Confirmar que o ambiente WSL e o venv existentes estão funcionais.

**Entregáveis:** `reports/environment.md` com comandos, versões, espaço livre, caminhos locais, hashes e limitações; bancos de origem inalterados.  
**Saída da fase:** ambiente funcional, origem identificada e espaço de execução definido.

## Fase 1 — Auditoria dos rótulos (somente leitura)

**Objetivo:** descrever cobertura e comportamento dos rótulos antes de escolher amostra, cortes ou modelos.

- [ ] Inspecionar esquema, tipos, chaves, timestamps e limites temporais da base/manifesto.
- [ ] Contar candles, pregões, tickers, raízes futuras e contratos por período.
- [ ] Auditar duplicatas, ordenação, lacunas temporais e minutos ausentes por raiz/pregão.
- [ ] Medir nulos e cobertura de `trend_5m`, `trend_10m`, `trend_15m` e `trend_mean` por raiz e pregão.
- [ ] Medir prevalência de classes e duração/comprimento de segmentos por alvo, raiz e pregão.
- [ ] Medir mudanças de classe e concordância entre escalas por raiz e pregão.
- [ ] Recalcular `trend_mean` como média/voto dos três alvos disponíveis e verificar a regra de maioria nas linhas elegíveis.
- [ ] Registrar linhas excluídas e divergências entre manifesto, banco e rótulos; não corrigir a base nesta fase.
- [ ] Gerar tabelas pequenas reproduzíveis e um resumo descritivo com contagens por pregão independente.

**Entregáveis:** script/notebook de auditoria reproduzível, configuração de consulta, tabelas resumidas e `reports/label_audit.md`.  
**Saída da fase:** inconsistências explicadas e cobertura suficiente para congelar a população do estudo.

## Fase 2 — Contrato dos dados e protocolo

**Objetivo:** congelar as decisões de amostragem antes de consultar resultados de teste.

- [ ] Aprovar universo principal de futuros e lista de raízes BovDB incluídas/excluídas com justificativa.
- [ ] Definir tratamento de contratos, vencimentos, rolagens e eventuais sobreposições de contratos.
- [ ] Definir chave única da amostra e instante em que a previsão seria tomada.
- [ ] Fixar política para minutos ausentes, candles incompletos, duplicatas e pregões parciais.
- [ ] Definir alvos individuais, máscara por alvo, interseção comum e regra do alvo de maioria.
- [ ] Definir uso de `mean_score` como alvo suave/resumo determinístico; não interpretá-lo como probabilidade verdadeira.
- [ ] Listar colunas permitidas e proibidas; excluir SIDEWAYS centrado, campos derivados de B4 e qualquer informação posterior à decisão.
- [ ] Definir população, período, exclusões e política de dados faltantes.
- [ ] Escrever e revisar `config/data_contract.yaml` e `config/experiment_protocol.yaml`.
- [ ] Congelar os arquivos de protocolo em commit antes de abrir/usar métricas de teste.

**Entregáveis:** contrato de dados e protocolo versionados, com proveniência e justificativas.  
**Saída da fase:** decisões analíticas pré-registradas e revisadas.

## Fase 3 — Features causais e splits temporais

**Objetivo:** construir entradas sem vazamento e validação cronológica comparável.

- [ ] Inspecionar o gerador B4 e a semântica das colunas para determinar fronteiras/segmentos dos alvos.
- [ ] Especificar janelas retrospectivas de OHLCV/atividade disponíveis até o instante da decisão.
- [ ] Definir um conjunto inicial enxuto de indicadores causais (por exemplo, retornos, corpo/amplitude do candle, volatilidade móvel e atividade/volume), suas fórmulas, lookbacks e aquecimento.
- [ ] Implementar e auditar indicadores sem usar rótulos, SIDEWAYS ou campos derivados de B4 como entrada.
- [ ] Medir consultas SQLite representativas; só então decidir se um cache derivado Parquet é útil para extração repetida.
- [ ] Determinar purge/embargo com base na janela de features e na fronteira/segmento do alvo.
- [ ] Definir folds walk-forward/expanding por pregão, com datas idênticas entre alvos e modelos.
- [ ] Implementar escalonamento e imputação ajustados somente no conjunto de treino de cada fold.
- [ ] Separar explicitamente treino, validação e teste; impedir shuffle e sobreposição temporal indevida.
- [ ] Criar auditorias automáticas de colunas, timestamps, chaves, fronteiras, purge e uso de dados futuros.
- [ ] Verificar por amostragem manual as datas e instrumentos de cada corte.

**Entregáveis:** código/configuração de features e splits, manifesto dos folds e `reports/leakage_audit.md`.  
**Saída da fase:** auditoria de vazamento aprovada e cortes congelados antes do treinamento.

## Fase 4 — Piloto de capacidade e baselines

**Objetivo:** medir custo local e estabelecer referências simples antes da comparação multitarefa.

- [ ] Configurar diretório temporário de execução e limite de disco; garantir que artefatos grandes não sejam versionados.
- [ ] Rodar piloto curto com uma raiz, janela limitada, batch pequeno e orçamento fixo.
- [ ] Registrar tempo por época, throughput, RAM, pico de VRAM e estabilidade da GPU.
- [ ] Ajustar o tamanho do modelo/batch ao limite da GTX 1650 Max-Q de 4 GB.
- [ ] Implementar baseline de persistência e baseline de classe majoritária calculados sem informação futura.
- [ ] Implementar regressão logística/Elastic Net.
- [ ] Implementar baseline de árvore (LightGBM ou XGBoost) no CPU, se viável no ambiente disponível.
- [ ] Implementar um MLP ou TCN compacto; não iniciar busca ampla de hiperparâmetros.
- [ ] Avaliar separadamente os três alvos e o alvo de maioria nos mesmos folds.
- [ ] Registrar MCC, balanced accuracy, macro-F1, prevalência, cobertura, matriz de confusão e custos de execução.

**Entregáveis:** configuração do piloto, logs e tabela resumida de custo/desempenho por modelo e alvo.  
**Saída da fase:** orçamento de execução e baselines reproduzíveis aprovados.

## Fase 5 — Modelos multi-escala e discordância

**Objetivo:** comparar estratégias pareadas nas mesmas amostras e cortes.

- [ ] Fixar seeds, orçamento de busca/treino e critérios de seleção sem olhar o teste.
- [ ] Treinar três modelos independentes, um por escala.
- [ ] Treinar encoder compartilhado com cabeças 5/10/15m e perda mascarada para alvos nulos.
- [ ] Treinar comparação com alvo duro de maioria.
- [ ] Treinar comparação com alvo suave derivado da fração de votos/`mean_score`.
- [ ] Calcular número de votos, concordância e discordância entre escalas nas linhas elegíveis.
- [ ] Avaliar abstention seletiva por nível de discordância, sempre reportando cobertura junto com desempenho.
- [ ] Comparar modelos na interseção comum de linhas e também reportar cobertura por cabeça quando alvos forem ausentes.
- [ ] Preservar igualdade de datas, entradas, seeds e orçamento entre comparações pareadas.
- [ ] Registrar predições e checkpoints somente no diretório temporário definido; guardar no repositório apenas resumos pequenos necessários.

**Entregáveis:** configurações, logs, tabela comparativa pareada e resumo de cobertura/discordância.  
**Saída da fase:** comparação completa sem apresentar votos como probabilidades ou verdade independente.

## Fase 6 — Generalização e inferência

**Objetivo:** estimar estabilidade entre pregões, blocos temporais e raízes.

- [ ] Repetir comparações nos blocos temporais e raízes definidos no protocolo.
- [ ] Calcular MCC, balanced accuracy e macro-F1 por cabeça/alvo, raiz e bloco.
- [ ] Estimar intervalos de incerteza por sessão/bloco temporal, não tratando candles como observações independentes.
- [ ] Aplicar correção de comparações múltiplas conforme protocolo (incluindo Friedman/Wilcoxon quando aplicável).
- [ ] Reportar tamanhos de efeito e diferenças pareadas, além de valores-p.
- [ ] Avaliar Brier, log-loss e calibração somente para saídas probabilísticas apropriadas.
- [ ] Fazer análises de sensibilidade para cobertura, universo, cortes e políticas de contrato já previstas.
- [ ] Registrar resultados negativos, falhas, exclusões e limitações sem selecionar somente resultados favoráveis.

**Entregáveis:** tabelas de inferência e generalização, scripts de análise e relatório de limitações.  
**Saída da fase:** afirmações restritas ao período, universo e protocolo efetivamente avaliados.

## Fase 7 — Extensões opcionais (condicionais)

**Só iniciar se** a Fase 5 mostrar sinal útil, houver orçamento local e a extensão tiver hipótese própria e ablação planejada.

- [ ] Decidir por escrito se alguma extensão atende aos critérios; caso contrário, registrar “não executada” e seguir para artigo.
- [ ] Se aprovada, escolher uma extensão por vez: pré-treino autossupervisionado compacto, encoder temporal congelado ou adaptação de regime com dados passados.
- [ ] Definir hipótese, conjunto de dados permitido, orçamento, folds e ablação antes do experimento.
- [ ] Medir footprint e tempo antes de qualquer execução extensa; não fazer fine-tuning de modelo grande.
- [ ] Comparar com o baseline correspondente em protocolo pareado.
- [ ] Registrar resultados e custo, inclusive resultado nulo, e não misturar a extensão ao núcleo sem justificativa.

**Entregáveis:** decisão documentada e, se executada, protocolo, ablação e relatório reproduzível.  
**Saída da fase:** extensão opcional concluída com evidência ou formalmente descartada.

## Fase 8 — Artigo e pacote reproduzível

**Objetivo:** escrever conclusões rastreáveis aos dados, código e resultados realmente produzidos.

- [ ] Definir a estrutura do novo manuscrito sem alterar o manuscrito NCA anterior de 5 minutos.
- [ ] Preparar método, proveniência, contrato, protocolo temporal e tratamento de rótulos ausentes.
- [ ] Preparar tabelas/figuras diretamente dos artefatos versionados ou reproduzíveis.
- [ ] Ligar cada número e afirmação a configuração, código, log e saída correspondentes.
- [ ] Explicitar que B0 não é ground truth sem validação independente e que discordância não é incerteza epistêmica.
- [ ] Explicitar limites: ausência de avaliação executável de lucro, escopo temporal jan–jun/2026, dados internos e cobertura B1/B2/Fuzzy insuficiente.
- [ ] Revisar alegações, vazamento, dependência entre observações, múltiplas comparações e disponibilidade de dados/código.
- [ ] Reproduzir as tabelas/figuras a partir das configurações arquivadas e conferir consistência com o manuscrito.
- [ ] Fazer revisão final de anonimização e requisitos editoriais do periódico escolhido.

**Entregáveis:** manuscrito e pacote mínimo de reprodução/documentação compatível com o status interno dos dados.  
**Saída da fase:** nenhuma afirmação numérica sem rastreabilidade e todas as limitações materiais declaradas.

## Critério de conclusão do projeto

- [ ] Fases 0–6 concluídas com critérios de saída atendidos.
- [ ] Fase 7 concluída ou explicitamente descartada com justificativa.
- [ ] Fase 8 concluída e reproduzida a partir dos artefatos documentados.
- [ ] Repositório contém código, configurações, documentação e resumos pequenos; dados e saídas pesadas permanecem externos/temporários.
- [ ] `git status` revisado para confirmar que nenhum banco, predição completa, checkpoint ou cache foi incluído.
