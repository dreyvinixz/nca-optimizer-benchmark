# Projeto Overleaf — manuscrito NCA

Este pacote contém uma cópia das fontes atuais do manuscrito, organizada para importação como projeto no Overleaf. O arquivo principal é `main.tex`; ele inclui explicitamente `literature_review.tex` (revisão sistemática) e `nca_related_work.tex` (posicionamento do estudo frente ao precursor). As citações aos trabalhos precursores foram anonimizadas nesta cópia para revisão duplo-cega. A folha de rosto com autoria e agradecimentos está separada em `titlepage.tex`.

## Importação

1. No Overleaf, escolha **New Project → Upload Project** e envie `nca_overleaf_template.zip`.
2. Em **Menu → Compiler**, selecione **pdfLaTeX**.
3. Confirme que `main.tex` está definido como documento principal e compile. O Overleaf executa BibTeX automaticamente para as referências.
4. `titlepage.tex` é um documento independente: use-o como documento principal apenas para compilar a folha de rosto, se necessário.

O pacote inclui a classe Springer Nature, os estilos bibliográficos, as seções e as figuras referenciadas. Ele não inclui os arquivos auxiliares locais da compilação nem o PDF compilado.

As trajetórias de convergência estão separadas por backbone e protocolo de fitness. Cada curva mostra a média dos três seeds comuns, sem faixa de incerteza, e o detalhe interno amplia as 250 avaliações finais. A seção de resultados separa MCC, acurácia nos dois holdouts e acurácia do Experimento 3 com validação cruzada temporal. A tabela de esforço distingue chamadas ao objetivo de ajustes efetivos do modelo, contabilizando cache e três ajustes por candidato na validação cruzada.

## Conferência antes de submissão

Esta é uma cópia de trabalho para Overleaf, não uma declaração de que o artigo está pronto para submissão. Revise o conteúdo científico e as tabelas, confirme os metadados da folha de rosto e verifique no Overleaf se a versão da classe Springer Nature aceita pelo periódico é compatível com o pacote.
