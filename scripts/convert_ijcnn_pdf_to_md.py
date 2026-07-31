import os
from pathlib import Path
import fitz  # PyMuPDF

ref_dir = Path("article/references")
out_dir = ref_dir / "md_references"
out_dir.mkdir(parents=True, exist_ok=True)

pdf_file = None
for f in ref_dir.glob("*.pdf"):
    if "Combining_Technical_Indicators" in f.name or "_ICCSA_2026" in f.name:
        pdf_file = f
        break

if not pdf_file:
    print("PDF file not found!")
    exit(1)

print(f"Opening: {pdf_file.name}")
doc = fitz.open(pdf_file)

md_lines = []
md_lines.append(f"# {pdf_file.stem}")
md_lines.append(f"**Original PDF**: `{pdf_file}`")
md_lines.append(f"**Page Count**: {len(doc)}\n")
md_lines.append("---\n")

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text("text")
    md_lines.append(f"<!-- Page {page_num + 1} -->")
    md_lines.append(f"## Page {page_num + 1}\n")
    md_lines.append(text)
    md_lines.append("\n---\n")

out_md = out_dir / "ijcnn_precursor_paper.md"
out_md.write_text("\n".join(md_lines), encoding="utf-8")
print(f"SUCCESS: Saved markdown to {out_md} ({out_md.stat().st_size} bytes, {len(doc)} pages)")
