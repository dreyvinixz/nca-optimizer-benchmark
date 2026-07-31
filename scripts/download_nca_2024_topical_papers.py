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

queries = [
    "optimization neural network stock financial forecasting",
    "metaheuristic hyperparameter tuning classification benchmark",
    "particle swarm optimization grey wolf differential evolution neural",
    "intraday market prediction machine learning evolutionary algorithm"
]

print("=== Fetching Relevant 2024+ Papers from Neural Computing and Applications (Journal 521) ===")

fetched_works = {}

for q in queries:
    url = (
        f"https://api.openalex.org/works?"
        f"filter=primary_location.source.issn:0941-0643,publication_year:>2023"
        f"&search={quote(q)}"
        f"&per_page=15"
    )
    print(f"Searching query: '{q}'...")
    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            data = res.json()
            for work in data.get("results", []):
                doi = work.get("doi", "")
                if doi and doi not in fetched_works:
                    fetched_works[doi] = work
    except Exception as e:
        print(f"  Error querying: {e}")

print(f"\nFound {len(fetched_works)} unique relevant 2024+ papers from NCA.\n")

downloaded_count = 0

for idx, (doi, item) in enumerate(fetched_works.items(), 1):
    title = item.get("title", f"NCA_Paper_{idx}")
    year = item.get("publication_year", 2024)
    doi_clean = doi.replace("https://doi.org/", "")
    
    open_access = item.get("open_access", {})
    pdf_url = open_access.get("oa_url") or item.get("primary_location", {}).get("pdf_url")
    
    clean_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_').lower()
    clean_title = clean_title[:65]
    filename_pdf = f"{year}_{clean_title}.pdf"
    pdf_path = OUT_PDF_DIR / filename_pdf
    md_path = OUT_MD_DIR / f"{year}_{clean_title}.md"
    
    print(f"[{idx}/{len(fetched_works)}] {year} — {title[:75]}...")
    print(f"   DOI: {doi}")
    
    # Download PDF if URL is present
    if pdf_url and not pdf_path.exists():
        try:
            print(f"   Downloading PDF from: {pdf_url}")
            pdf_res = requests.get(pdf_url, headers=headers, timeout=25, allow_redirects=True)
            if pdf_res.status_code == 200 and len(pdf_res.content) > 10000 and pdf_res.content[:4] == b'%PDF':
                with open(pdf_path, "wb") as f:
                    f.write(pdf_res.content)
                print(f"   SUCCESS! Saved PDF ({len(pdf_res.content)} bytes)")
            else:
                print(f"   Note: Direct OA PDF link not a raw PDF file (status {pdf_res.status_code})")
        except Exception as e:
            print(f"   Download error: {e}")
    elif pdf_path.exists():
        print(f"   PDF exists locally.")
        
    # Convert to MD if PDF is available
    if pdf_path.exists() and not md_path.exists():
        try:
            doc = fitz.open(pdf_path)
            md_lines = [
                f"# {title}\n",
                f"**Year**: {year} | **Journal**: Neural Computing and Applications (NCA, Journal 521)",
                f"**DOI**: {doi}\n",
                "---\n"
            ]
            for page_num in range(len(doc)):
                md_lines.append(f"## Page {page_num + 1}\n" + doc[page_num].get_text("text") + "\n---\n")
            md_path.write_text("\n".join(md_lines), encoding="utf-8")
            print(f"   Converted to Markdown: {md_path.name} ({len(doc)} pages)")
            downloaded_count += 1
        except Exception as e:
            print(f"   MD conversion error: {e}")

print(f"\n[COMPLETE] Successfully processed relevant 2024+ NCA articles!")
