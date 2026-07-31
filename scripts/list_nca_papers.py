import csv
from pathlib import Path

csv_path = Path("article/references/nca_search/papers.csv")
if csv_path.exists():
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        nca_rows = [r for r in reader if "neural computing" in r.get("journal","").lower() or "springer" in r.get("publisher","").lower()]
        print(f"Total NCA / Springer papers found in OpenAlex/Crossref search: {len(nca_rows)}\n")
        print("Top 15 NCA / Springer papers:")
        for idx, r in enumerate(nca_rows[:15], 1):
            print(f"{idx}. [{r.get('year')}] {r.get('title')}")
            print(f"   Journal: {r.get('journal')} | Cited by: {r.get('cited_by')} | DOI: {r.get('doi')}\n")
