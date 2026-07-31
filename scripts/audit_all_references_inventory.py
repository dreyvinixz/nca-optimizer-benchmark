import os
from pathlib import Path

base_dir = Path("article/references")

print("=== COMPLETE INVENTORY AUDIT OF article/references/ ===\n")

# List all PDF files across all subdirectories
all_pdfs = list(base_dir.rglob("*.pdf"))
print(f"Total PDF files found across all subfolders: {len(all_pdfs)}")

# List all MD files across all subdirectories
all_mds = list(base_dir.rglob("*.md"))
print(f"Total Markdown (.md) files found across all subfolders: {len(all_mds)}")

print("\n--- Subdirectory breakdown ---")
subdirs = [d for d in base_dir.rglob("*") if d.is_dir()]
for d in subdirs:
    rel_path = d.relative_to(base_dir)
    pdf_cnt = len(list(d.glob("*.pdf")))
    md_cnt = len(list(d.glob("*.md")))
    print(f"Folder: {rel_path} | PDFs: {pdf_cnt} | MDs: {md_cnt}")

# Check if there are any PDFs that DO NOT have a corresponding MD file
print("\n--- Checking for any unconverted PDFs ---")
unconverted = []
for p in all_pdfs:
    stem = p.stem.lower()
    # search if any md file has this stem
    match = any(m.stem.lower() == stem for m in all_mds)
    if not match:
        unconverted.append(p)

print(f"Unconverted PDFs count: {len(unconverted)}")
for u in unconverted:
    print(f"  [MISSING MD]: {u}")

if len(unconverted) == 0:
    print("\n[VERIFIED] 100% of all PDF reference files in the repository HAVE BEEN CONVERTED to Markdown!")
