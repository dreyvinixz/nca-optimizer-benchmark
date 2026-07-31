import requests
import re
import fitz
from pathlib import Path

OUT_PDF = Path("article/references/literature/additional_key_pdfs")
OUT_MD = Path("article/references/md_references/additional_key_papers")

OUT_PDF.mkdir(parents=True, exist_ok=True)
OUT_MD.mkdir(parents=True, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

target_papers = [
    {
        "title": "Statistical and Machine Learning forecasting methods: Concerns and ways forward",
        "year": 2018,
        "doi": "10.1371/journal.pone.0194889",
        "url": "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0194889&type=printable"
    },
    {
        "title": "Hyperparameter optimization: Foundations, algorithms, best practices, and open challenges",
        "year": 2023,
        "doi": "10.1002/widm.1484",
        "url": "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/widm.1484"
    },
    {
        "title": "Metaheuristic Algorithms on Feature Selection: A Survey of One Decade of Research",
        "year": 2021,
        "doi": "10.1109/access.2021.3056407",
        "url": "https://ieeexplore.ieee.org/ielx7/6287639/9312710/09344597.pdf"
    },
    {
        "title": "NSE Stock Market Prediction Using Deep-Learning Models",
        "year": 2018,
        "doi": "10.1016/j.procs.2018.05.050",
        "url": "https://www.sciencedirect.com/science/article/pii/S1877050918307828/pdf"
    }
]

print("=== Downloading Additional Key Reference Papers ===")

for p in target_papers:
    title = p["title"]
    year = p["year"]
    url = p["url"]
    
    clean_name = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_').lower()[:60]
    pdf_path = OUT_PDF / f"{year}_{clean_name}.pdf"
    md_path = OUT_MD / f"{year}_{clean_name}.md"
    
    print(f"Downloading: [{year}] {title}...")
    try:
        res = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        if res.status_code == 200 and len(res.content) > 10000:
            with open(pdf_path, "wb") as f:
                f.write(res.content)
            print(f"  Saved PDF: {pdf_path.name} ({len(res.content)} bytes)")
            
            # Convert to MD
            doc = fitz.open(pdf_path)
            md_lines = [f"# {title}\n", f"**Year**: {year} | **DOI**: {p['doi']}\n", "---\n"]
            for page_num in range(len(doc)):
                md_lines.append(f"## Page {page_num + 1}\n" + doc[page_num].get_text("text") + "\n---\n")
            md_path.write_text("\n".join(md_lines), encoding="utf-8")
            print(f"  Converted to MD: {md_path.name} ({len(doc)} pages)")
        else:
            print(f"  Status {res.status_code}, len {len(res.content)}")
    except Exception as e:
        print(f"  Error: {e}")

print("\n[COMPLETE] Additional key papers downloaded & converted!")
