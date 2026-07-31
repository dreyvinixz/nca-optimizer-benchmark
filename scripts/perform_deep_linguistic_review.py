import re
import sys

# Force utf-8 encoding for stdout
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path

BASE_MD = Path("article/references/md_references")

sources = [
    ("Dhingra et al. (NCA 2025)", BASE_MD / "s00521_2025_11546_2_nca_benchmark.md"),
    ("Gad (Springer 2022)", BASE_MD / "2022_pso_systematic_review.md"),
    ("Makridakis et al. (2018)", BASE_MD / "additional_key_papers" / "2018_statistical_and_machine_learning_forecasting_methods_concern.md"),
    ("Mirjalili et al. (NCA 2020)", BASE_MD / "nca_search_all" / "03_optimizer_comparison_benchmark" / "2020_evolutionary_algorithms_and_their_applications_to_engineering_problems.md"),
]

print("=== DEEP HUMAN LINGUISTIC REVIEW ON REFERENCE ARTICLES ===\n")

for label, path in sources:
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    
    lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 40]
    
    hooks = [l for l in lines if any(k in l.lower() for k in ["forecasting", "prediction", "optimization", "time-series", "benchmark", "neural network"])][:4]
    gaps = [l for l in lines if any(k in l.lower() for k in ["however", "nevertheless", "underexplored", "limitation", "flaw", "gap", "lack"])][:4]
    contribs = [l for l in lines if any(k in l.lower() for k in ["main contributions", "this study", "this paper", "we propose", "we conduct", "we evaluate"])][:4]

    print(f"--- {label} ---")
    print("HUMAN OPENING HOOKS:")
    for h in hooks:
        print(f"  • {h[:120]}...")
    print("\nHUMAN GAP STATEMENTS:")
    for g in gaps:
        print(f"  • {g[:120]}...")
    print("\nHUMAN CONTRIBUTION STATEMENTS:")
    for c in contribs:
        print(f"  • {c[:120]}...")
    print("\n" + "="*60 + "\n")
