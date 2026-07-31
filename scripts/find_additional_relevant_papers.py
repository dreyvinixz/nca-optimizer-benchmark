import csv
from pathlib import Path

csv_path = Path("article/references/nca_search/papers.csv")
md_dir = Path("article/references/md_references")

existing_md_names = set(f.stem.lower() for f in md_dir.rglob("*.md"))

candidates = []

if csv_path.exists():
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            title = r.get("title", "")
            year = r.get("year", "")
            doi = r.get("doi", "")
            pdf_url = r.get("pdf_url", "")
            venue = r.get("venue", "")
            citations = int(r.get("citations", 0) or 0)
            
            # Check keywords for high relevance
            title_lower = title.lower()
            if any(k in title_lower for k in [
                "stock", "financial", "trading", "intraday", "forecasting",
                "metaheuristic", "grey wolf", "particle swarm", "differential evolution",
                "genetic algorithm", "matthews correlation", "hyperparameter", "benchmark"
            ]):
                if pdf_url and len(pdf_url) > 10:
                    candidates.append({
                        "title": title,
                        "year": year,
                        "doi": doi,
                        "venue": venue,
                        "citations": citations,
                        "pdf_url": pdf_url
                    })

# Sort by citations and year
candidates.sort(key=lambda x: (x["citations"], x["year"]), reverse=True)

print(f"Total relevant candidate papers found in search CSV: {len(candidates)}\n")
print("Top 15 additional papers recommended for download & conversion:")
for idx, c in enumerate(candidates[:15], 1):
    print(f"{idx}. [{c['year']}] {c['title']}")
    print(f"   Venue: {c['venue']} | Citations: {c['citations']} | DOI: {c['doi']}")
    print(f"   PDF: {c['pdf_url']}\n")
