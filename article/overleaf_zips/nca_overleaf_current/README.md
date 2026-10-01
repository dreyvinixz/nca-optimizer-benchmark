# Projeto Overleaf — manuscrito NCA

Este pacote contém uma cópia das fontes atuais do manuscrito, organizada para importação como projeto no Overleaf. O arquivo principal é `main.tex`; ele inclui explicitamente `literature_review.tex` (revisão sistemática) e `nca_related_work.tex` (posicionamento do estudo frente ao precursor). As citações aos trabalhos precursores foram anonimizadas nesta cópia para revisão duplo-cega. A folha de rosto com autoria e agradecimentos está separada em `titlepage.tex`.

A figura de visão geral metodológica é incluída como PDF vetorial horizontal (`figures/methodology_workflow_vector.pdf`); seu fonte TikZ editável está ao lado.

## Importação

1. No Overleaf, escolha **New Project → Upload Project** e envie o ZIP `nca_overleaf_current.zip`.
2. Em **Menu → Compiler**, selecione **pdfLaTeX**.
3. Confirme que `main.tex` está definido como documento principal e compile. O Overleaf executa BibTeX automaticamente para as referências.
4. `titlepage.tex` é um documento independente: use-o como documento principal apenas para compilar a folha de rosto, se necessário.

O pacote inclui a classe Springer Nature, os estilos bibliográficos, as seções e as figuras referenciadas. Ele não inclui os arquivos auxiliares locais da compilação nem o PDF compilado.

## Conferência antes de submissão

Esta é uma cópia de trabalho para Overleaf, não uma declaração de que o artigo está pronto para submissão. Revise o conteúdo científico e as tabelas, confirme os metadados da folha de rosto e verifique no Overleaf se a versão da classe Springer Nature aceita pelo periódico é compatível com o pacote.
