import os
import fitz  # PyMuPDF
from pathlib import Path
from tqdm import tqdm

BASE_DIR = Path("article/references")
OUT_DIR = BASE_DIR / "md_references"

LIT_DIR = BASE_DIR / "literature"
SEARCH_DIR = BASE_DIR / "nca_search" / "papers"

OUT_LIT = OUT_DIR / "literature_all"
OUT_SEARCH = OUT_DIR / "nca_search_all"

OUT_LIT.mkdir(parents=True, exist_ok=True)
OUT_SEARCH.mkdir(parents=True, exist_ok=True)

def convert_pdf_file(pdf_path, out_path):
    try:
        doc = fitz.open(pdf_path)
        md_lines = []
        md_lines.append(f"# {pdf_path.stem}\n")
        md_lines.append(f"**Source File**: `{pdf_path}`")
        md_lines.append(f"**Total Pages**: {len(doc)}\n")
        md_lines.append("---\n")

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            md_lines.append(f"<!-- Page {page_num + 1} -->")
            md_lines.append(f"## Page {page_num + 1}\n")
            md_lines.append(text)
            md_lines.append("\n---\n")

        out_path.write_text("\n".join(md_lines), encoding="utf-8")
        return len(doc), out_path.stat().st_size
    except Exception as e:
        print(f"[ERROR] Failed {pdf_path}: {e}")
        return 0, 0

def main():
    print("=== Converting Literature PDFs ===")
    lit_pdfs = list(LIT_DIR.glob("*.pdf"))
    for pdf_path in tqdm(lit_pdfs, desc="Literature PDFs"):
        out_file = OUT_LIT / f"{pdf_path.stem}.md"
        if not out_file.exists():
            pages, size = convert_pdf_file(pdf_path, out_file)
            print(f"  Saved: {out_file.name} ({pages} pages, {size} bytes)")
        else:
            print(f"  Already exists: {out_file.name}")

    print("\n=== Converting Search PDFs ===")
    search_pdfs = list(SEARCH_DIR.rglob("*.pdf"))
    for pdf_path in tqdm(search_pdfs, desc="Search PDFs"):
        topic = pdf_path.parent.name
        topic_out_dir = OUT_SEARCH / topic
        topic_out_dir.mkdir(parents=True, exist_ok=True)
        out_file = topic_out_dir / f"{pdf_path.stem}.md"
        if not out_file.exists():
            pages, size = convert_pdf_file(pdf_path, out_file)
            print(f"  Saved: {topic}/{out_file.name} ({pages} pages, {size} bytes)")
        else:
            print(f"  Already exists: {topic}/{out_file.name}")

    print("\n[COMPLETE] All literature and search PDFs converted to Markdown.")

if __name__ == "__main__":
    main()
