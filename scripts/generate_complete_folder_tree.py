import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

base_dir = Path("article/references")

def print_tree(dir_path, prefix=""):
    items = sorted(list(dir_path.iterdir()))
    dirs = [i for i in items if i.is_dir()]
    files = [i for i in items if i.is_file()]
    
    for i, d in enumerate(dirs):
        is_last_dir = (i == len(dirs) - 1) and (len(files) == 0)
        connector = "└── " if is_last_dir else "├── "
        pdf_cnt = len(list(d.rglob("*.pdf")))
        md_cnt = len(list(d.rglob("*.md")))
        print(f"{prefix}{connector}{d.name}/ ({pdf_cnt} PDFs, {md_cnt} MDs)")
        new_prefix = prefix + ("    " if is_last_dir else "│   ")
        if d.name in ["md_references", "nca_search_all", "papers", "literature"]:
            sub_items = sorted(list(d.iterdir()))
            for j, sub in enumerate(sub_items):
                is_last_sub = (j == len(sub_items) - 1)
                sub_conn = "└── " if is_last_sub else "├── "
                if sub.is_dir():
                    s_pdf = len(list(sub.rglob("*.pdf")))
                    s_md = len(list(sub.rglob("*.md")))
                    print(f"{new_prefix}{sub_conn}{sub.name}/ ({s_pdf} PDFs, {s_md} MDs)")
                elif sub.is_file() and sub.suffix in ['.md', '.pdf']:
                    print(f"{new_prefix}{sub_conn}{sub.name}")

print("=== EXACT REPOSITORY TREE ===")
print_tree(base_dir)
