# Piloto de capacidade do MLP

Piloto de uma raiz e um fold de desenvolvimento: WIN, alvo B0 de 5m, 47 pregões de treino e 10 de validação. As datas do teste ficaram excluídas.

- GPU: NVIDIA GeForce GTX 1650 Max-Q, 4,096 MiB disponíveis; TensorFlow 2.21.0 reconheceu `/GPU:0`.
- MLP: 11–32–16–1, dropout 0.10, batch 256, cinco épocas, sem embaralhar linhas; `StandardScaler` ajustado apenas no treino.
- Treino/validação: 29,119 / 6,382 linhas elegíveis.
- Tempo por época: 6.635 s na primeira época (inclui inicialização) e 0.411–0.418 s nas quatro seguintes; taxa agregada de 17,557 amostras/s incluindo a primeira época.
- Tempo total incluindo compilação e avaliação: 10.92 s; acurácia binária de validação: 0.749 (medida apenas para verificar funcionamento do piloto).
- Memória: pico do TensorFlow 69,723,648 bytes (~66.5 MiB); processo Python 1,453,312 KiB de RSS. Durante o treino, `nvidia-smi` observou 317–327 MiB de uso total na GPU, contra 182 MiB antes do processo.
- O MLP completou cinco épocas sem falhas. Esse piloto curto dimensiona uma arquitetura inicial; não comprova estabilidade para modelos maiores ou lotes maiores.

O CV completo com os mesmos quatro folds está em [`mlp_cv_summary.md`](mlp_cv_summary.md), com resumos reproduzíveis em CSV/JSON. Os rótulos B0 continuam retrospectivos e não são métricas de negociação.
