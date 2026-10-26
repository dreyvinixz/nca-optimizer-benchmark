# Roadmap — multi-escala e incerteza dos rótulos intradiários

**Status:** planejamento; treinamento deste estudo ainda não iniciado  
**Branch:** `feat/one-minute-multitask-study`  
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
- O B4 v3.1-internal.3 é um artefato interno, não uma publicação pública.
  B1/B2/Fuzzy não cobrem atualmente o painel inteiro e não entram na análise
  principal até que sejam regenerados e auditados em todo o período.
- A contagem de candles não substitui a contagem de pregões independentes.
  Relatar incerteza por sessão/bloco temporal e por raiz, não por linha como se
  todas fossem independentes.

## Preservação de espaço e ambiente autorizado

- Usar o checkout existente em `C:\mysystems\projects\nca-optimizer-benchmark`
  e o WSL2 Ubuntu já configurado. Não clonar o repositório, criar um segundo
  checkout nem copiar `.venv_wsl`.
- Reutilizar `/mnt/c/mysystems/projects/nca-optimizer-benchmark/.venv_wsl`
  por meio de `source scripts/wsl_cuda_env.sh`.
- Ler a base diretamente do BovDB existente, configurando o caminho local por
  variável de ambiente, por exemplo:
  `BOVDB_B4_DB=/mnt/c/mysystems/services/bovdb/bovdb-pipeline/rotulos/data/bovdb-labels-B4-v1.sqlite`.
  Não copiar o SQLite de 744 MB para este repositório.
- A checagem de caminho confirmou que o venv WSL e o SQLite estão acessíveis
  pelo Ubuntu. A visibilidade atual da GPU pelo TensorFlow ainda precisa ser
  revalidada antes do treino; o registro antigo de `docs/gpu_wsl_setup.md`
  contém versão de driver anterior à observada no Windows.
- Não versionar dados, bases derivadas, predições completas, checkpoints ou
  caches pesados. Antes do primeiro treino, definir um diretório temporário,
  verificar espaço livre e adicionar regras Git para os artefatos novos.
  Manter no repositório apenas código, configuração e resumos pequenos e
  rastreáveis.

## Fases e critérios de saída

| Fase | Trabalho | Critério para avançar |
|---|---|---|
| 0. Ambiente e proveniência | Confirmar branch, WSL, versão do Python/TensorFlow/CUDA, GPU visível, espaço livre, caminho externo e hashes do manifesto/base. | Leitura somente; nenhuma cópia da base; ambiente existente funcional. |
| 1. Auditoria dos rótulos | Em leitura somente, medir cobertura/nulos, prevalência, durações, mudanças de classe e concordância entre 5/10/15m por raiz e pregão; conferir `trend_mean` contra voto majoritário. | Tabelas de auditoria reproduzíveis e inconsistências documentadas. |
| 2. Contrato dos dados | Fixar universo futuro, regra de contratos/vencimento, timestamp de previsão, política de minutos ausentes e colunas permitidas. Excluir SIDEWAYS centrado. | Especificação congelada em YAML antes de consultar resultados de teste. |
| 3. Features causais e splits | Construir entradas exclusivamente com OHLCV/atividade disponível até o instante da decisão; escalar dentro do treino; separar por datas em walk-forward/expanding; purgar amostras cujos alvos/fronteiras cruzem cortes. | Auditoria de vazamento e split por data/instrumento aprovada. |
| 4. Baselines | Avaliar persistência/maioria, Elastic Net ou regressão logística, LightGBM/XGBoost e um MLP/TCN compacto. Primeiro comparar os três alvos individualmente e maioria, sem busca grande. | Métricas temporais por alvo/root/bloco e tempo/VRAM do piloto. |
| 5. Multi-escala e discordância | Comparar: (a) três modelos independentes; (b) encoder compartilhado com três cabeças e perda mascarada para alvos ausentes; (c) alvo de maioria; (d) alvo suave derivado da fração de votos. Relatar também abstention/coverage pela discordância. | Comparação pareada nas mesmas datas, entradas, sementes e orçamento; sem tratar votos como probabilidades verdadeiras. |
| 6. Generalização e inferência | Repetir nos blocos temporais e raízes acordados; estimar intervalos por sessão/bloco; corrigir comparações múltiplas; reportar calibração quando houver probabilidades. | Conclusões limitadas ao período/universo efetivamente testados. |
| 7. Extensões opcionais | Pré-treino autossupervisionado compacto em candles sem rótulo; representação congelada de modelo temporal; adaptação a regime com dados passados. Cada extensão terá ablação própria. | Só avançar se fase 5 mostrar sinal útil e o piloto couber no limite local. |
| 8. Artigo | Produzir tabelas/figuras ligadas a artefatos, seção de limitações e disponibilidade consistente com o status interno dos dados. | Toda afirmação numérica aponta para configuração, log e saída reproduzível. |

## Protocolo de modelagem proposto

### Entradas e alvo

Cada amostra representa um candle elegível de um contrato e pregão. As
entradas serão calculadas com janelas retrospectivas; nenhuma feature derivada
de B4 será usada. As três saídas supervisionadas são os vetores B0 de 5/10/15m.
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
