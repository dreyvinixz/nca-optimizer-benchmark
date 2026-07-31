import requests
import json
import os
import re
import fitz
from pathlib import Path
from urllib.parse import quote

OUT_PDF_DIR = Path("article/references/nca_journal_521_pdfs")
OUT_MD_DIR = Path("article/references/md_references/nca_journal_521_2024_plus")

OUT_PDF_DIR.mkdir(parents=True, exist_ok=True)
OUT_MD_DIR.mkdir(parents=True, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/html, */*"
}

print("=== Fetching Recent Papers (>= 2024) from Neural Computing and Applications (Journal 521) ===")

# Query OpenAlex API specifically for Neural Computing and Applications (ISSN 0941-0643) year >= 2024
openalex_url = (
    "https://api.openalex.org/works?"
    "filter=primary_location.source.issn:0941-0643,publication_year:>2023"
    "&sort=cited_by_count:desc"
    "&per_page=30"
)

print(f"Querying OpenAlex: {openalex_url}")
res = requests.get(openalex_url, headers=headers, timeout=15)

if res.status_code != 200:
    print(f"OpenAlex request failed: {res.status_code}")
    exit(1)

data = res.json()
results = data.get("results", [])
print(f"Found {len(results)} recent papers (>= 2024) in NCA.\n")

downloaded_count = 0

for idx, item in enumerate(results, 1):
    title = item.get("title", f"NCA_Paper_{idx}")
    year = item.get("publication_year", 2024)
    doi = item.get("doi", "")
    doi_clean = doi.replace("https://doi.org/", "")
    
    # Try to locate PDF URL
    open_access = item.get("open_access", {})
    pdf_url = open_access.get("oa_url") or item.get("primary_location", {}).get("pdf_url")
    
    clean_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_').lower()
    clean_title = clean_title[:60]
    filename_pdf = f"{year}_{clean_title}.pdf"
    pdf_path = OUT_PDF_DIR / filename_pdf
    md_path = OUT_MD_DIR / f"{year}_{clean_title}.md"
    
    print(f"[{idx}/{len(results)}] {year} — {title[:70]}...")
    print(f"   DOI: {doi}")
    
    # Attempt download if pdf_url is available
    success = False
    if pdf_url and not pdf_path.exists():
        try:
            print(f"   Downloading PDF from: {pdf_url}")
            pdf_res = requests.get(pdf_url, headers=headers, timeout=20, allow_redirects=True)
            if pdf_res.status_code == 200 and len(pdf_res.content) > 10000:
                with open(pdf_path, "wb") as f:
                    f.write(pdf_res.content)
                print(f"   SUCCESS! Downloaded PDF ({len(pdf_res.content)} bytes)")
                success = True
            else:
                print(f"   Download failed (status {pdf_res.status_code}, len {len(pdf_res.content)})")
        except Exception as e:
            print(f"   Download error: {e}")
    elif pdf_path.exists():
        print(f"   PDF already exists locally.")
        success = True
        
    # If PDF exists, convert to Markdown
    if pdf_path.exists() and not md_path.exists():
        try:
            doc = fitz.open(pdf_path)
            md_lines = [f"# {title}\n", f"**Year**: {year} | **Journal**: Neural Computing and Applications (NCA)", f"**DOI**: {doi}\n", "---\n"]
            for page_num in range(len(doc)):
                md_lines.append(f"## Page {page_num + 1}\n" + doc[page_num].get_text("text") + "\n---\n")
            md_path.write_text("\n".join(md_lines), encoding="utf-8")
            print(f"   Converted to MD: {md_path.name} ({len(doc)} pages)")
            downloaded_count += 1
        except Exception as e:
            print(f"   MD conversion error: {e}")

print(f"\n[SUMMARY] Processed {len(results)} NCA articles (>= 2024). Saved PDFs & MDs in {OUT_MD_DIR}")
