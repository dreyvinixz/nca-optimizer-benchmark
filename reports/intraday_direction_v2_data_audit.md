# Auditoria do cache direcional intradiário v2

**Resultado: aprovada.** Chaves, features completas e alvos foram comparados com deslocamentos dentro do mesmo ticker e pregão.

- Linhas: 181,974; pregões: 119; features candidatas: 101.
- Linhas completas após aquecimento integral: 91,989 (50.6%).
- WIN: 119,670; IND: 62,304.
- Janela observada: 09:00:00–17:59:00.
- Chave única `(ticker,date,time)`; nenhum nome de coluna de B4/rótulo/endpoint/futuro nas features.
- Em todos os horizontes, o deslocamento corresponde exatamente a h minutos consecutivos observados e não cruza ticker, data ou segmento.

| Horizonte | Alvos válidos | Prevalência de alta | Linhas early | Linhas middle | Linhas late |
|---:|---:|---:|---:|---:|---:|
| 5m | 147,868 | 0.4938 | 57,400 | 48,671 | 41,797 |
| 15m | 124,838 | 0.4967 | 51,796 | 40,099 | 32,943 |
| 30m | 107,782 | 0.5005 | 46,927 | 34,446 | 26,409 |

SHA-256 da origem SQLite: `32cadf06387ae172edc804804fe762ef26f9f0928424ee83ce9e37a848389eab`.
O período inteiro permanece desenvolvimento; esta auditoria não abre nem valida um teste futuro independente.
