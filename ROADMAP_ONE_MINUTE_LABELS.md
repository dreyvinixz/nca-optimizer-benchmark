# Roadmap — multi-escala e incerteza dos rótulos intradiários

**Status:** planejamento; treinamento deste estudo ainda não iniciado  
**Branch:** `feat/one-minute-labels-clean`
**Atualizado:** 2026-10-26

## Objetivo científico

Investigar se aprender conjuntamente os rótulos B0 de 5, 10 e 15 minutos
melhora a classificação de tendências em candles de 1 minuto, e se o desacordo
entre essas escalas identifica exemplos ambíguos. Comparar essa abordagem com
classificadores separados por escala e com o rótulo derivado por maioria.

O estudo avalia **robustez e utilidade preditiva relativas aos rótulos B0**. Sem
uma referência independente, não afirmará que uma escala é ground truth ou que
um modelo aprendeu a direção real do mercado. O manuscrito NCA existente para
5 minutos permanece separado e não será reescrito por este plano.

## Dados conhecidos e limites

- O manifesto `bovdb-labels-B4-v1.manifest.json` descreve 1.255.202 candles,
  41 tickers e 119 pregões, de 2026-01-02 a 2026-06-30.
- O artefato oferece `trend_5m`, `trend_10m`, `trend_15m` e `trend_mean`.
  `trend_mean` é derivado dos outros três e só existe quando todos estão
  definidos; com três alvos binários válidos, corresponde à maioria.
- O universo inclui ações/ETFs e futuros. A análise principal usará os futuros,
  identificados pelas raízes aprovadas do BovDB; a inclusão de cada raiz e as
  datas/contratos cobertos será conferida antes do split.
- Os campos SIDEWAYS usam janelas centradas e são retrospectivos. Não serão
  preditores nem parte da alegação causal.
- O banco de rótulos B4-v1 é um artefato interno, não uma publicação pública.
  Seu metadado `label_run` registra o gerador `B4-unsuppressed-B0+SIDEWAYS-features-v1`
  e a origem `bovdb-v3.1-internal.2.sqlite`. B1/B2/Fuzzy não cobrem atualmente
  o painel inteiro e não entram na análise principal até que sejam regenerados
  e auditados em todo o período.
- O B4 processa cada ticker/pregão separadamente e grava cada rótulo na mesma
  chave `ticker/date/time` do candle. A regra de pivôs é retrospectiva: a posição
  dos pivôs e o fim dos segmentos dependem de candles posteriores da sessão;
  após o último pivô, o rótulo fica nulo.
- A contagem de candles não substitui a contagem de pregões independentes.
  Relatar incerteza por sessão/bloco temporal e por raiz, não por linha como se
  todas fossem independentes.
- Os dois SQLite estão disponíveis localmente em `data/`: `bovdb-labels-B4-v1.sqlite`
  (744 MB) e `bovdb-v3.1-internal.2.sqlite` (429 MB). O B4 contém 1.255.202
  linhas em cada tabela de rótulos e identifica o segundo arquivo como sua base
  de origem. O SHA-256 da base local confere com `source_sha256` no B4.
- A configuração atual do BovDB não aprova WDO; embora existam símbolos WDO no
  cadastro, o `price1` local tem zero candles WDO e o B4 tem zero rótulos WDO.

## Preservação de espaço e ambiente autorizado

- Usar o checkout existente em `C:\mysystems\projects\nca-optimizer-benchmark`
  e o WSL2 Ubuntu já configurado. Não clonar o repositório, criar um segundo
  checkout nem copiar `.venv_wsl`.
- Reutilizar `/mnt/c/mysystems/projects/nca-optimizer-benchmark/.venv_wsl`
  por meio de `source scripts/wsl_cuda_env.sh`.
- Usar os arquivos locais existentes, sem modificar os bancos de origem. No WSL,
  definir `BOVDB_B4_DB=/mnt/c/mysystems/projects/nca-optimizer-benchmark/data/bovdb-labels-B4-v1.sqlite`
  e `BOVDB_SOURCE_DB=/mnt/c/mysystems/projects/nca-optimizer-benchmark/data/bovdb-v3.1-internal.2.sqlite`.
- Os bancos estão sob `data/`, ignorada pelo Git. Mantê-los fora de commits;
  não criar uma segunda cópia nem converter os originais nesta etapa. Consultas
  devem ser somente leitura.
- Antes de converter ou exportar, medir o tempo das consultas representativas.
  Se leituras analíticas repetidas forem o gargalo, avaliar um cache derivado
  em Parquet após congelar o contrato dos dados. Se o gargalo for o carregamento
  em batches, avaliar arrays memmap ou TFRecord no piloto. Registrar tamanho e
  tempo de leitura/escrita e manter a origem SQLite intacta.
- Reutilizar `/mnt/c/mysystems/projects/nca-optimizer-benchmark/.venv_wsl` e
  carregar as bibliotecas CUDA com `source scripts/wsl_cuda_env.sh`. O venv e os
  bancos são acessíveis pelo Ubuntu, mas a visibilidade atual da GPU pelo
  TensorFlow ainda precisa ser revalidada antes do treino.
- Não versionar dados, caches derivados, predições completas, checkpoints ou
  caches pesados. Antes do primeiro treino, definir um diretório temporário e
  verificar espaço livre. Manter no repositório apenas código, configuração e
  resumos pequenos e rastreáveis.

## Fases e critérios de saída

| Fase | Trabalho | Critério para avançar |
|---|---|---|
| 0. Ambiente e proveniência | Confirmar branch, WSL, versão do Python/TensorFlow/CUDA, GPU visível, espaço livre, caminhos locais e hashes; conferir o hash da base de origem contra os metadados B4. | Leitura somente; bancos locais íntegros; ambiente existente funcional. |
| 1. Auditoria dos rótulos | Em leitura somente, medir cobertura/nulos, prevalência, durações, mudanças de classe e concordância entre 5/10/15m por raiz e pregão; conferir `trend_mean` contra voto majoritário. | Tabelas de auditoria reproduzíveis e inconsistências documentadas. |
| 2. Contrato dos dados | Escolher universo por liquidez observada (`amount_stock`, negócios e sessões), regra de contratos/vencimento, timestamp/horizonte, lacunas e colunas permitidas. Excluir SIDEWAYS centrado. Reusar a auditoria B4 da Fase 1 para as linhas já existentes. | Especificação congelada em YAML antes de consultar resultados de teste. |
| 3. Features causais e splits | Definir e construir indicadores causais de OHLCV/atividade disponíveis até a decisão; escalar dentro do treino; separar por datas em walk-forward/expanding; purgar amostras cujos alvos/fronteiras cruzem cortes. | Auditoria de vazamento e split por data/instrumento aprovada. |
| 4. Baselines | Avaliar persistência/maioria, Elastic Net ou regressão logística, LightGBM/XGBoost e um MLP/TCN compacto. Primeiro comparar os três alvos individualmente e maioria, sem busca grande. | Métricas temporais por alvo/root/bloco e tempo/VRAM do piloto. |
| 5. Multi-escala e discordância | Comparar: (a) três modelos independentes; (b) encoder compartilhado com três cabeças e perda mascarada para alvos ausentes; (c) alvo de maioria; (d) alvo suave derivado da fração de votos. Relatar também abstention/coverage pela discordância. | Comparação pareada nas mesmas datas, entradas, sementes e orçamento; sem tratar votos como probabilidades verdadeiras. |
| 6. Generalização e inferência | Repetir nos blocos temporais e raízes acordados; estimar intervalos por sessão/bloco; corrigir comparações múltiplas; reportar calibração quando houver probabilidades. | Conclusões limitadas ao período/universo efetivamente testados. |
| 7. Extensões opcionais | Pré-treino autossupervisionado compacto em candles sem rótulo; representação congelada de modelo temporal; adaptação a regime com dados passados. Cada extensão terá ablação própria. | Só avançar se fase 5 mostrar sinal útil e o piloto couber no limite local. |
| 8. Artigo | Produzir tabelas/figuras ligadas a artefatos, seção de limitações e disponibilidade consistente com o status interno dos dados. | Toda afirmação numérica aponta para configuração, log e saída reproduzível. |

## Seleção do universo por liquidez (Fase 2)

Usar `amount_stock` (quantidade de contratos negociados) como métrica primária,
`business` (negócios) como apoio, e número de pregões com dados para medir
cobertura. Comparar a mediana por pregão, agregando contratos da mesma raiz;
`volume` é valor financeiro em BRL e não deve ser o único critério entre
produtos com notionais/multiplicadores diferentes. A tabela reproduzível está
em [reports/futures_liquidity.md](reports/futures_liquidity.md).

Na fotografia local, WIN e IND lideram com folga. Proposta de universo principal
para esta base: WIN e IND; CCMF e BGIG ficam fora do núcleo por menor liquidez,
com possível uso exploratório se houver hipótese própria. EURF, WEUF e SJCF têm
poucos pregões/observações. WDO seria candidato relevante para avaliar, mas não
pode entrar com os arquivos atuais: `price1` e B4 têm zero candles/rótulos WDO e
a configuração de origem não aprova essa raiz. Para incluí-lo, é necessário
ampliar a fonte intradiária e gerar B4 para WDO; isso não exige revalidar de
novo os rótulos dos símbolos já auditados na Fase 1.

WSP e ISP também estão ausentes dos arquivos locais: não aparecem no cadastro de
ticker, em `price1` ou no B4. Portanto, o protocolo confirmatório desta branch
fica restrito a WIN e IND. CCMF e BGIG não entram no núcleo, apesar de terem
dados, porque a liquidez observada é muito menor; podem ser retomados apenas como
extensão exploratória claramente separada.

## Contratos congelados e extração (Fases 2–3)

As decisões executáveis estão em [`config/data_contract.yaml`](config/data_contract.yaml)
e [`config/experiment_protocol.yaml`](config/experiment_protocol.yaml). O
contrato trata cada vencimento como uma série independente, reinicia janelas em
mudança de contrato/pregão/lacuna e mantém todos os contratos de uma data no
mesmo corte temporal. Não cria série contínua ajustada. Ausência de negócio não
gera candle sintético nem preenchimento.

O extrator [`scripts/build_features.py`](scripts/build_features.py) lê os
SQLite em modo somente leitura e cria um Parquet seletivo, ignorado pelo Git,
com 182.266 linhas WIN/IND e 12,6 MB nesta fotografia. O manifesto registra os
hashes de origem, hashes dos contratos, cobertura, cortes e folds. A consulta
usa a chave composta completa dos rótulos; os tipos SQLite de `date/time`
diferem entre as bases e são normalizados explicitamente para texto na junção.

As features congeladas são retornos logarítmicos de 1/5/15 minutos observados
consecutivos, corpo e amplitude relativos ao fechamento, desvio-padrão
populacional de retornos em janelas de 5/15/30 linhas e `log1p` de volume,
negócios e quantidade negociada. O aquecimento exige a janela completa e fica
nulo. As entradas usam o candle concluído no timestamp; os targets continuam
sendo B0 ex post e são interpretados somente como rótulos previstos.

A divisão cronológica é por pregão: 60% treino, 20% validação, 20% teste,
arredondando treino e validação para baixo e deixando o restante no teste. No
snapshot, isso corresponde a 71/23/25 pregões observados, respectivamente. Há
quatro folds expanding de desenvolvimento, com 47/57/67/77 pregões de treino e
blocos seguintes de 10 pregões para validação; nenhum inclui datas de teste.
O escalonamento ainda será implementado junto dos pipelines dos baselines, com
ajuste exclusivo no treino de cada fold.

## Alinhamento temporal do alvo (decisão da Fase 2)

**Recomendação para o protocolo principal: não deslocar o alvo em um dia.** O
estudo compara rótulos B0 para o mesmo candle; o pareamento inicial é
`X(ticker, pregão, hora) -> y_B0(ticker, pregão, hora)`, usando apenas
indicadores causais disponíveis até aquela hora. O rótulo B0 permanece uma
referência retrospectiva, não um ground truth disponível em tempo real. Um
alvo da próxima sessão mudaria a pergunta para previsão de outro pregão.

Os registros do estudo NCA anterior descrevem `shift(-1)` por **uma linha
observada** de cada ticker, não um deslocamento universal de um dia. A linha
seguinte podia cair na próxima sessão e criava alvos que cruzavam fronteiras de
split; esse alinhamento não tornou os pivôs causais. Portanto, não copiar esse
shift automaticamente para este estudo. A auditoria global da Fase 1 já validou
os rótulos dos registros B4 existentes; a Fase 2 reutiliza esse resultado. Só
será necessária geração e checagem específica se a fonte for ampliada, por
exemplo para incluir WDO.

Se o objetivo científico passar a ser prever a próxima sessão, definir isso na
Fase 2 como protocolo alternativo: alinhar com o próximo pregão disponível do
mesmo ticker e ao mesmo horário de decisão, sem usar `data + 1` de calendário.
Definir continuidade/rolagem do contrato e horários ausentes. Implementar o
alinhamento na Fase 3 e purgar amostras de treino cujo pregão-alvo atravesse a
fronteira para validação/teste.

## Protocolo de modelagem proposto

### Entradas, instante de previsão e alvo

Cada amostra representa um candle elegível de um contrato e pregão. As
entradas serão indicadores causais derivados de OHLCV/atividade, calculados
com janelas retrospectivas; nenhuma feature derivada de B4 será usada. A lista
de indicadores, fórmulas, lookbacks e aquecimento será decidida após a auditoria
e congelada no contrato dos dados antes de consultar o teste. O pareamento
principal recomendado usa o mesmo timestamp para entrada e rótulo B0; não
aplica shift diário. As três saídas supervisionadas são os vetores B0 de
5/10/15m. Se a Fase 2 aprovar previsão da próxima sessão, o contrato deve
definir o pregão-alvo, horário, continuidade de contrato e purge de fronteiras.
Alvos nulos ficam mascarados por cabeça na perda multitarefa; a comparação
comum também reportará uma interseção de linhas em que os três alvos existam.

### Discordância entre escalas

Para linhas com os três rótulos presentes, guardar a contagem de votos e o
score de consenso `mean_score`. Comparar alvo duro de maioria e loss suave
contra `mean_score`, com a mesma arquitetura e os mesmos cortes. Tratar o
score como resumo determinístico da família B0; ele não mede incerteza
epistêmica nem substitui anotação humana.

### Validação e métricas

- Cortes cronológicos por pregão, iguais entre alvos e modelos; nenhum shuffle.
- Purge/embargo baseado na informação de fronteira/segmento e na janela de
  features, determinada pela inspeção do gerador e das colunas armazenadas.
- Métricas principais: MCC, balanced accuracy e macro-F1 por cabeça/alvo.
- Métricas secundárias: cobertura, prevalência, matrizes de confusão, Brier/
  log-loss/calibração quando aplicáveis, e desempenho por raiz e bloco.
- Registrar seeds, versões, candidatos, tempo de treino e pico de memória.
  Limitar o número de experimentos; a comparação de metaheurísticas fica fora
  do núcleo deste novo artigo, salvo se houver uma hipótese secundária clara.

## Plano de capacidade da GTX 1650 Max-Q (4 GB)

1. Revalidar no WSL `nvidia-smi` e `tf.config.list_physical_devices("GPU")`;
   não inferir compatibilidade atual apenas do relatório antigo.
2. Fazer um piloto curto com uma raiz, uma janela temporal e batch pequeno; medir
   uso de VRAM, throughput e tempo por época antes de fixar folds/seeds.
3. Reutilizar um encoder pequeno entre as três cabeças multitarefa; processar
   janelas em batches e evitar materializar/duplicar todas as janelas na RAM/VRAM.
4. Manter Elastic Net e modelos de árvore no CPU quando isso reduzir custo de
   VRAM. Avaliar modelos fundacionais apenas com encoder congelado e depois de
   medir o footprint real. Não planejar pré-treino/fine-tuning de modelos grandes.
5. Definir diretório de run temporário e orçamento de disco antes da geração de
   predições; não guardar checkpoints intermediários por padrão.

## Perguntas que o estudo não responderá sem novos dados

- Qual rótulo é “verdadeiro” sem referência independente ou revisão humana.
- Se existe lucro executável: `price1` não contém livro de ofertas; custos e
  slippage exigiriam cenários explícitos ou dados de execução adicionais.
- Se B1/B2/Fuzzy generalizam para seis meses: suas versões completas ainda
  precisam ser geradas e auditadas na mesma amostra.
- Se os resultados generalizam para além de 2026-01 a 2026-06; ampliar a janela
  com proveniência aprovada fortalece uma validação futura independente.
