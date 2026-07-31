# Templates LaTeX para Overleaf — Journal NCA (Springer Nature)

Esta pasta contém o pacote LaTeX oficial e pré-configurado para o journal **Neural Computing and Applications (NCA)**:

## Arquivos Disponíveis

1. **`nca_overleaf_template.zip`** (Pronto para Overleaf)
   - Contém todos os arquivos da classe `sn-jnl.cls`, estilo bibliográfico `sn-mathphys-num.bst`, `main.tex`, `titlepage.tex`, `references.bib` e todas as seções em `sections/`.
   - **Como usar no Overleaf**:
     1. Abra o [Overleaf](https://www.overleaf.com/).
     2. Clique em **New Project** $\rightarrow$ **Upload Project**.
     3. Selecione o arquivo [`nca_overleaf_template.zip`](file:///c:/mysystems/projects/nca-optimizer-benchmark/article/templates/nca_overleaf_template.zip).
     4. Selecione o compilador **pdfLaTeX** nas configurações do projeto no Overleaf.
     5. Clique em **Recompile**.

2. **`sn-jnl.cls`**
   - Classe LaTeX oficial da Springer Nature v0.1/v3.1.

---

## Estrutura do Pacote ZIP (`nca_overleaf_template.zip`)

```
nca_overleaf_template.zip
├── sn-jnl.cls             # Classe oficial Springer Nature
├── sn-mathphys-num.bst     # Estilo de referências numeradas NCA
├── sn-mathphys.bst         # Estilo de referências de apoio
├── main.tex               # Manuscrito principal anônimo (double-blind)
├── titlepage.tex          # Folha de rosto separada com metadados dos autores
├── references.bib         # Base de referências BibTeX
└── sections/              # Seções modulares em LaTeX
    ├── introduction.tex
    ├── related_work.tex
    ├── data.tex
    ├── methodology.tex
    ├── results.tex
    ├── discussion.tex
    ├── limitations.tex
    ├── conclusion.tex
    └── declarations.tex
```
