"""
Search NCA Papers — Literature search for Neural Computing and Applications
Adapted from D:\\tese\\bioswarm_research_pipeline.py

Searches OpenAlex and Crossref for papers published in NCA and related
journals that are relevant to the optimizer benchmark study.

Usage:
    python scripts/search_nca_papers.py

Output:
    article/references/nca_search/papers.csv
    article/references/nca_search/top_papers.md
    article/references/nca_search/bibtex.bib
"""

import os
import re
import sys
import time
import math
import hashlib
import requests
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from datetime import datetime

# ============================================================
# Configuration
# ============================================================

UNPAYWALL_EMAIL = os.getenv("UNPAYWALL_EMAIL", "andreyvinicius@furg.br")

FROM_YEAR = 2018
TO_YEAR = datetime.now().year

# Output directory
BASE_DIR = Path(__file__).resolve().parent.parent / "article" / "references" / "nca_search"
PAPERS_DIR = BASE_DIR / "papers"

OUTPUT_CSV = BASE_DIR / "papers.csv"
OUTPUT_MD = BASE_DIR / "top_papers.md"
OUTPUT_BIB = BASE_DIR / "bibtex.bib"

MAX_RESULTS_PER_QUERY = 25
MAX_DOWNLOADS_PER_TOPIC = 10
MIN_SCORE_TO_DOWNLOAD = 12

# ============================================================
# Search Topics — Adapted for NCA Optimizer Benchmark
# ============================================================

TOPICS = {
    "01_metaheuristic_neural_optimization": [
        "metaheuristic benchmark neural network classification",
        "genetic algorithm neural network hyperparameter optimization",
        "particle swarm optimization MLP classification",
        "differential evolution neural network tuning",
        "grey wolf optimizer deep learning classification",
        "evolutionary algorithm hyperparameter optimization neural network",
        "swarm intelligence neural network training",
        "bio-inspired optimization machine learning benchmark",
    ],
    "02_financial_prediction_optimization": [
        "evolutionary optimization financial time series prediction",
        "swarm intelligence stock market prediction neural network",
        "neural network optimization futures market classification",
        "metaheuristic hyperparameter tuning financial forecasting",
        "genetic algorithm financial prediction machine learning",
        "particle swarm optimization stock market forecasting",
        "intraday prediction neural network optimization",
    ],
    "03_optimizer_comparison_benchmark": [
        "optimizer comparison benchmark machine learning",
        "evolutionary algorithm comparison neural network",
        "metaheuristic comparison study classification",
        "random search genetic algorithm PSO benchmark",
        "convergence analysis metaheuristic optimization",
        "computational budget optimizer comparison",
        "statistical comparison optimization algorithms",
    ],
    "04_mlp_optimization": [
        "multilayer perceptron hyperparameter optimization",
        "MLP tuning evolutionary algorithm",
        "neural network architecture search metaheuristic",
        "feedforward network optimization genetic algorithm",
        "MLP training particle swarm optimization",
    ],
}

# Prioritize NCA and related journals
RELEVANT_VENUE_KEYWORDS = [
    "neural computing", "neurocomputing",
    "applied soft computing", "soft computing",
    "expert systems with applications",
    "knowledge-based systems",
    "engineering applications of artificial intelligence",
    "swarm and evolutionary computation",
    "information sciences",
    "computational intelligence",
    "ieee", "springer", "elsevier",
    "machine learning", "neural network",
    "artificial intelligence", "optimization",
]

HIGH_VALUE_TERMS = [
    "metaheuristic", "benchmark",
    "genetic algorithm", "particle swarm",
    "differential evolution", "grey wolf",
    "hyperparameter", "optimization",
    "neural network", "mlp", "multilayer perceptron",
    "classification", "forecasting", "prediction",
    "financial", "stock market", "futures",
    "convergence", "comparison", "evaluation",
    "mcc", "matthews correlation",
    "temporal validation", "walk-forward",
]

# ============================================================
# Helper Functions
# ============================================================


def slugify(text, max_len=100):
    text = text or "untitled"
    text = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    text = re.sub(r"[-\s]+", "_", text).strip("_")
    return text[:max_len] or "untitled"


def ensure_dirs():
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    PAPERS_DIR.mkdir(exist_ok=True)
    for topic in TOPICS:
        (PAPERS_DIR / topic).mkdir(parents=True, exist_ok=True)


def safe_get_json(url, params=None, headers=None, timeout=40):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        if response.status_code == 429:
            time.sleep(8)
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[WARN] JSON failed: {url} | {e}")
        return None


def safe_download(url, out_path, timeout=60):
    try:
        headers = {"User-Agent": f"NCABenchmarkResearch/1.0 mailto:{UNPAYWALL_EMAIL}"}
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        if response.status_code != 200:
            return False
        content_type = response.headers.get("content-type", "").lower()
        if "pdf" not in content_type and not url.lower().endswith(".pdf"):
            return False
        out_path.write_bytes(response.content)
        return out_path.stat().st_size > 10_000
    except Exception:
        return False


def extract_abstract_from_openalex(inv_index):
    if not inv_index:
        return ""
    words = []
    for word, positions in inv_index.items():
        for pos in positions:
            words.append((pos, word))
    return " ".join(word for _, word in sorted(words))


# ============================================================
# Scoring
# ============================================================


def score_paper(paper):
    title = str(paper.get("title") or "").lower()
    abstract = str(paper.get("abstract") or "").lower()
    venue = str(paper.get("venue") or "").lower()
    year = int(paper.get("year") or 0)
    citations = int(paper.get("citations") or 0)

    text = f"{title} {abstract} {venue}"

    relevance = sum(1 for term in HIGH_VALUE_TERMS if term in text)
    venue_score = sum(1 for term in RELEVANT_VENUE_KEYWORDS if term in venue)

    # Bonus for being published in NCA specifically
    nca_bonus = 10 if "neural computing and applications" in venue else 0

    recency = max(0, year - FROM_YEAR + 1)
    citation_score = math.log1p(citations)

    oa_bonus = 3 if paper.get("is_open_access") else 0
    pdf_bonus = 3 if paper.get("pdf_url") else 0
    doi_bonus = 1 if paper.get("doi") else 0

    total = (
        relevance * 3
        + venue_score * 2
        + nca_bonus
        + recency * 1.5
        + citation_score
        + oa_bonus
        + pdf_bonus
        + doi_bonus
    )

    return round(total, 3)


# ============================================================
# Search APIs
# ============================================================


def search_openalex(query, topic):
    url = "https://api.openalex.org/works"
    params = {
        "search": query,
        "filter": (
            f"from_publication_date:{FROM_YEAR}-01-01,"
            f"to_publication_date:{TO_YEAR}-12-31"
        ),
        "sort": "cited_by_count:desc",
        "per-page": MAX_RESULTS_PER_QUERY,
        "mailto": UNPAYWALL_EMAIL,
    }

    data = safe_get_json(url, params=params)
    results = []

    if not data:
        return results

    for item in data.get("results", []):
        doi = item.get("doi")
        if doi:
            doi = doi.replace("https://doi.org/", "")

        primary_location = item.get("primary_location") or {}
        source = primary_location.get("source") or {}
        best_oa = item.get("best_oa_location") or {}
        open_access = item.get("open_access") or {}

        paper = {
            "source": "OpenAlex",
            "topic": topic,
            "query": query,
            "title": item.get("title"),
            "year": item.get("publication_year"),
            "doi": doi,
            "venue": source.get("display_name"),
            "publisher": source.get("host_organization_name"),
            "citations": item.get("cited_by_count", 0),
            "is_open_access": open_access.get("is_oa", False),
            "oa_status": open_access.get("oa_status"),
            "landing_page_url": best_oa.get("landing_page_url") or item.get("id"),
            "pdf_url": best_oa.get("pdf_url"),
            "abstract": extract_abstract_from_openalex(
                item.get("abstract_inverted_index")
            ),
        }
        paper["score"] = score_paper(paper)
        results.append(paper)

    return results


def search_crossref(query, topic):
    url = "https://api.crossref.org/works"
    params = {
        "query.title": query,
        "filter": (
            f"from-pub-date:{FROM_YEAR}-01-01,"
            f"until-pub-date:{TO_YEAR}-12-31,"
            f"type:journal-article"
        ),
        "sort": "is-referenced-by-count",
        "order": "desc",
        "rows": MAX_RESULTS_PER_QUERY,
        "mailto": UNPAYWALL_EMAIL,
    }

    data = safe_get_json(url, params=params)
    results = []

    if not data:
        return results

    for item in data.get("message", {}).get("items", []):
        title = item.get("title", [""])[0] if item.get("title") else ""

        date_parts = (
            item.get("published-print", {}).get("date-parts")
            or item.get("published-online", {}).get("date-parts")
            or item.get("published", {}).get("date-parts")
            or []
        )
        year = date_parts[0][0] if date_parts and date_parts[0] else None

        paper = {
            "source": "Crossref",
            "topic": topic,
            "query": query,
            "title": title,
            "year": year,
            "doi": item.get("DOI"),
            "venue": (
                item.get("container-title", [""])[0]
                if item.get("container-title")
                else ""
            ),
            "publisher": item.get("publisher"),
            "citations": item.get("is-referenced-by-count", 0),
            "is_open_access": False,
            "oa_status": None,
            "landing_page_url": item.get("URL"),
            "pdf_url": None,
            "abstract": re.sub("<.*?>", "", item.get("abstract", "")),
        }
        paper["score"] = score_paper(paper)
        results.append(paper)

    return results


# ============================================================
# Deduplication and Export
# ============================================================


def deduplicate(papers):
    seen = set()
    unique = []
    for paper in papers:
        title_key = slugify(paper.get("title", ""), 140)
        key = (paper.get("doi") or title_key).lower()
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(paper)
    return unique


def make_bibtex_key(row):
    title = slugify(row.get("title", "paper"), 40)
    year = int(row.get("year") or 0)
    doi_hash = hashlib.md5(str(row.get("doi") or title).encode()).hexdigest()[:6]
    return f"{title}_{year}_{doi_hash}"


def export_bibtex(df):
    entries = []
    for _, row in df.iterrows():
        key = make_bibtex_key(row)
        title = str(row.get("title") or "").replace("{", "").replace("}", "")
        year = int(row.get("year") or 0)
        venue = str(row.get("venue") or "")
        doi = str(row.get("doi") or "")
        url = str(row.get("landing_page_url") or row.get("pdf_url") or "")
        entry = f"""@article{{{key},
  title = {{{title}}},
  journal = {{{venue}}},
  year = {{{year}}},
  doi = {{{doi}}},
  url = {{{url}}}
}}"""
        entries.append(entry)
    OUTPUT_BIB.write_text("\n\n".join(entries), encoding="utf-8")


def export_top_markdown(df, top_n=30):
    lines = ["# Top Papers — NCA Optimizer Benchmark Literature Search\n"]
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    for topic, group in df.groupby("topic"):
        lines.append(f"\n## {topic}\n")
        for _, row in (
            group.sort_values("score", ascending=False).head(top_n).iterrows()
        ):
            nca_tag = " **[NCA]**" if "neural computing" in str(row.get("venue", "")).lower() else ""
            lines.append(
                f"- **{row.get('title')}** ({row.get('year')}) — "
                f"*{row.get('venue')}* — score `{row.get('score')}` — "
                f"citations `{row.get('citations')}`{nca_tag} — "
                f"[link]({row.get('landing_page_url')})"
            )

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


# ============================================================
# Main
# ============================================================


def main():
    ensure_dirs()

    papers = []

    for topic, queries in TOPICS.items():
        for query in queries:
            print(f"\n[SEARCH] {topic} -> {query}")
            papers.extend(search_openalex(query, topic))
            papers.extend(search_crossref(query, topic))
            time.sleep(1)

    papers = deduplicate(papers)

    # Re-score all papers
    for paper in papers:
        paper["score"] = score_paper(paper)

    df = pd.DataFrame(papers)

    if df.empty:
        print("No papers found.")
        return

    df = df.sort_values(["score", "citations", "year"], ascending=False)

    # Download PDFs for top papers
    print("\n[DOWNLOAD] Downloading open access PDFs...")
    local_paths = []
    download_count = {topic: 0 for topic in TOPICS}

    for _, row in tqdm(df.iterrows(), total=len(df), desc="PDFs"):
        topic = str(row.get("topic") or "unknown")
        pdf_url = row.get("pdf_url")
        score = row.get("score", 0)

        if (
            not isinstance(pdf_url, str)
            or not pdf_url.startswith("http")
            or score < MIN_SCORE_TO_DOWNLOAD
            or download_count.get(topic, 0) >= MAX_DOWNLOADS_PER_TOPIC
        ):
            local_paths.append(None)
            continue

        out_dir = PAPERS_DIR / topic
        filename = f"{int(row.get('year') or 0)}_{slugify(row.get('title', 'paper'))}.pdf"
        out_path = out_dir / filename

        if out_path.exists():
            local_paths.append(str(out_path))
            download_count[topic] = download_count.get(topic, 0) + 1
            continue

        if safe_download(pdf_url, out_path):
            local_paths.append(str(out_path))
            download_count[topic] = download_count.get(topic, 0) + 1
        else:
            local_paths.append(None)

        time.sleep(0.8)

    df["local_pdf_path"] = local_paths

    # Save outputs
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    export_top_markdown(df)
    export_bibtex(df)

    # Summary
    nca_papers = df[df["venue"].str.contains("Neural Computing", case=False, na=False)]
    print(f"\nDone.")
    print(f"  Total papers found: {len(df)}")
    print(f"  Papers from NCA journal: {len(nca_papers)}")
    print(f"  Output: {OUTPUT_CSV}")
    print(f"  Output: {OUTPUT_MD}")
    print(f"  Output: {OUTPUT_BIB}")


if __name__ == "__main__":
    main()
