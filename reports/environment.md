# Fase 0 — ambiente e proveniência

**Verificado em:** 2026-10-26  
**Branch/commit no início da checagem:** `feat/one-minute-labels-clean` / `dd6e3ac`  
**Estado do Git:** havia alterações locais de README/roadmap e helper/checklist em preparação; registrei o estado sem limpar nem descartar arquivos. O commit atual da branch foi atualizado durante a sessão.  
**Execução:** somente leitura para bancos e manifesto.

## Ambiente WSL2

| Item | Resultado |
|---|---|
| Distribuição/kernel | Ubuntu; Linux `6.18.33.1-microsoft-standard-WSL2`, x86_64 |
| Python / SQLite no `.venv_wsl` | Python 3.12.13 / SQLite 3.53.1 |
| TensorFlow | 2.21.0 |
| GPU visível pelo TensorFlow | `NVIDIA GeForce GTX 1650 with Max-Q Design`, 4096 MiB; `tf.config.list_physical_devices("GPU")` retornou GPU:0 |
| Driver / CUDA Toolkit | 621.01 / CUDA 13.1.115 |
| CUDA/cuDNN do ambiente Python | CUDA runtime 12.9.79; cuBLAS 12.9.2.10; cuDNN 9.23.0.39 |
| RAM WSL disponível na verificação | 5.2 GiB |
| Espaço livre | C: 14 GiB (98% usado); `/tmp` 2.9 GiB |

O ambiente e os dois arquivos SQLite abriram pelo WSL. O helper `scripts/wsl_cuda_env.sh` foi carregado. A GPU é visível; o espaço em C: é o limite operacional mais próximo. Não reservar cache derivado ou artefatos grandes antes de definir e medir o orçamento de disco.

## Arquivos e hashes

| Arquivo | Tamanho | SHA-256 | Integridade/proveniência |
|---|---:|---|---|
| `data/bovdb-labels-B4-v1.sqlite` | 743,989,248 bytes | `2d8c18c8d1a46be788ee2810a9caba043c2413102e4ee4f5c9927646037ce4c8` | `PRAGMA quick_check=ok`; hash igual ao manifesto |
| `data/bovdb-v3.1-internal.2.sqlite` | 428,638,208 bytes | `32cadf06387ae172edc804804fe762ef26f9f0928424ee83ce9e37a848389eab` | `PRAGMA quick_check=ok`; hash igual a `label_run.source_sha256` do B4 |
| Manifesto externo `bovdb-labels-B4-v1.manifest.json` | 2,143 bytes | `977ef4f0448d66c129e8fa2b3caccd20fb5071658fd402e41fc93270d2ed1061` | Hash do artefato B4 e hash da fonte conferem |
| Configuração externa `config/v3_1_universe.yaml` | 577 bytes | `2b08914d5eed3a93245d02d234b8e79e323dada159571bfe5b054424c0ed920b` | Fonte das raízes futuras aprovadas |

O manifesto identifica o B4 como `B4-v1`, release interno `v3.1-internal.3`, privado e não oficial público. O B4 registra 1.255.202 candles, 41 tickers, 119 pregões (`2026-01-02` a `2026-06-30`) e 1.255.202 linhas em cada uma das quatro tabelas de rótulos. O banco-fonte local é o `bovdb-v3.1-internal.2.sqlite` indicado pelo metadado e seu hash confere.

Os bancos permanecem em `data/`, ignorados pelo Git; não foram copiados, convertidos nem alterados durante esta auditoria.

## Resultado da fase

**Aprovada com ressalva de capacidade:** proveniência, integridade, acesso WSL, ambiente Python/TensorFlow e GPU foram confirmados. O pouco espaço livre em C: exige medir antes de gerar caches ou dados derivados. A configuração aprovada lista raízes `WIN`, `IND`, `EURF`, `WEUF`, `CCMF`, `SJCF` e `BGIG`.


## Comandos de reprodução no WSL

```bash
cd /mnt/c/mysystems/projects/nca-optimizer-benchmark
source scripts/wsl_cuda_env.sh
export BOVDB_B4_DB=/mnt/c/mysystems/projects/nca-optimizer-benchmark/data/bovdb-labels-B4-v1.sqlite
export BOVDB_SOURCE_DB=/mnt/c/mysystems/projects/nca-optimizer-benchmark/data/bovdb-v3.1-internal.2.sqlite
export BOVDB_UNIVERSE_CONFIG=/mnt/c/mysystems/services/bovdb/bovdb-pipeline/config/v3_1_universe.yaml
export BOVDB_B4_MANIFEST=/mnt/c/mysystems/services/bovdb/bovdb-pipeline/rotulos/data/bovdb-labels-B4-v1.manifest.json
.venv_wsl/bin/python scripts/audit_labels.py
```
