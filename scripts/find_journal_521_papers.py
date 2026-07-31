import os
from pathlib import Path
import fitz

BASE_DIR = Path("article/references")

print("=== Scanning all PDFs for Journal 521 (Neural Computing and Applications) ===")

nca_pdfs = []

for pdf_file in BASE_DIR.rglob("*.pdf"):
    try:
        doc = fitz.open(pdf_file)
        text_page1 = doc[0].get_text("text") if len(doc) > 0 else ""
        if "s00521" in text_page1.lower() or "neural computing and applications" in text_page1.lower() or "neural comput & applic" in text_page1.lower():
            nca_pdfs.append((pdf_file.name, pdf_file, len(doc)))
    except Exception as e:
        pass

print(f"Total Journal 521 (NCA) PDF files found: {len(nca_pdfs)}\n")
for idx, (name, path, pages) in enumerate(nca_pdfs, 1):
    print(f"{idx}. {name}")
    print(f"   Path: {path}")
    print(f"   Pages: {pages}\n")
