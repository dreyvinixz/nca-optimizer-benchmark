import re
import os
from pathlib import Path

BASE_MD_DIR = Path("article/references/md_references")

nca_files = [
    ("NCA Solar Benchmark (Dhingra 2025)", BASE_MD_DIR / "s00521_2025_11546_2_nca_benchmark.md"),
    ("NCA Submission Guidelines", Path("article/references/nca_submission_guidelines.md")),
    ("NCA EA Engineering (2020)", BASE_MD_DIR / "nca_search_all" / "03_optimizer_comparison_benchmark" / "2020_evolutionary_algorithms_and_their_applications_to_engineering_problems.md"),
]

# Scan 2024+ NCA papers to analyze average length and section structure
nca_2024_dir = BASE_MD_DIR / "nca_journal_521_2024_plus"
nca_2024_files = list(nca_2024_dir.glob("*.md")) if nca_2024_dir.exists() else []

page_counts = []
sections_found = {}

for f in nca_2024_files:
    text = f.read_text(encoding="utf-8", errors="ignore")
    # extract page count from header if present
    page_match = re.search(r'## Page (\d+)', text)
    pages = [int(m) for m in re.findall(r'## Page (\d+)', text)]
    if pages:
        page_counts.append(max(pages))
    
    # extract H1/H2 headers
    headers = re.findall(r'^(?:#|##)\s+([0-9\.]*\s*[A-Z][A-Za-z\s\-]+)', text, re.MULTILINE)
    for h in headers:
        h_clean = h.strip()
        if len(h_clean) > 3 and not h_clean.startswith("Page"):
            sections_found[h_clean] = sections_found.get(h_clean, 0) + 1

avg_pages = sum(page_counts) / len(page_counts) if page_counts else 25
min_pages = min(page_counts) if page_counts else 15
max_pages = max(page_counts) if page_counts else 54

print(f"=== NCA Structural Metrics (Sample of {len(page_counts)} papers) ===")
print(f"Average Page Count (Published PDF Layout): {avg_pages:.1f} pages")
print(f"Min Page Count: {min_pages} pages | Max Page Count: {max_pages} pages")
print("\nMost Common Sections Found in NCA Papers:")
sorted_sections = sorted(sections_found.items(), key=lambda x: x[1], reverse=True)
for sec, cnt in sorted_sections[:15]:
    print(f"  - {sec} ({cnt} occurrences)")
