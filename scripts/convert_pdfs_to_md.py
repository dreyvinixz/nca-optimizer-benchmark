"""
Convert Reference PDFs to Markdown (.md)
Extracts full text and structure from key reference PDFs using PyMuPDF (fitz).
"""

import os
from pathlib import Path
import fitz  # PyMuPDF

BASE_DIR = Path(__file__).resolve().parent.parent / "article" / "references"
OUT_DIR = BASE_DIR / "md_references"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Find candidate PDFs
pdf_targets = [
    {
        "name_pattern": "2022_particle_swarm_optimization_algorithm_and_its_applications",
        "output_name": "2022_pso_systematic_review.md",
        "role": "Revisão da literatura e estrutura textual (estilo de escrita e revisão)",
    },
    {
        "name_pattern": "s00521-025-11546-2",
        "output_name": "s00521_2025_11546_2_nca_benchmark.md",
        "role": "Estrutura principal do NCA (tabelas, figuras, formato do journal)",
    },
]

def find_pdf(pattern):
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if pattern.lower() in file.lower() and file.endswith(".pdf"):
                return Path(root) / file
    return None

def convert_pdf_to_md(pdf_path, out_path, role_desc):
    print(f"Converting: {pdf_path.name} -> {out_path.name}")
    doc = fitz.open(pdf_path)
    
    md_lines = []
    md_lines.append(f"# {pdf_path.stem}")
    md_lines.append(f"**Função no projeto**: {role_desc}")
    md_lines.append(f"**Arquivo original**: `{pdf_path}`")
    md_lines.append(f"**Total de páginas**: {len(doc)}\n")
    md_lines.append("---\n")

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        
        md_lines.append(f"<!-- Page {page_num + 1} -->")
        md_lines.append(f"## Page {page_num + 1}\n")
        md_lines.append(text)
        md_lines.append("\n---\n")

    out_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Saved: {out_path} ({out_path.stat().st_size} bytes, {len(doc)} pages)")

def main():
    for target in pdf_targets:
        pdf_file = find_pdf(target["name_pattern"])
        if not pdf_file:
            # try alternative names if any
            if "s00521" in target["name_pattern"]:
                pdf_file = find_pdf("nca_benchmark_reference")
        
        if pdf_file and pdf_file.exists():
            out_file = OUT_DIR / target["output_name"]
            convert_pdf_to_md(pdf_file, out_file, target["role"])
        else:
            print(f"[WARN] PDF not found for pattern: {target['name_pattern']}")

if __name__ == "__main__":
    main()
