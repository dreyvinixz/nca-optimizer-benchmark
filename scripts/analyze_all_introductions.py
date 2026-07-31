import re
import os
from pathlib import Path

BASE_DIR = Path("article/references/md_references")

key_files = [
    ("NCA Solar Benchmark (2025)", BASE_DIR / "s00521_2025_11546_2_nca_benchmark.md"),
    ("PSO Systematic Review (2022)", BASE_DIR / "2022_pso_systematic_review.md"),
    ("ICCSA Precursor Paper (2025)", BASE_DIR / "ijcnn_precursor_paper.md"),
    ("IJCNN Precursor Paper (2026)", BASE_DIR / "ijcnn_deep_learning_ga_paper.md"),
    ("PSO Comprehensive Survey (2022)", BASE_DIR / "literature_all" / "2022_particle_swarm_optimization_a_comprehensive_survey.md"),
    ("Exhaustive Metaheuristics Review (2023)", BASE_DIR / "literature_all" / "2023_an_exhaustive_review_of_the_metaheuristic_algorithms_for_search_and_optimization_taxonomy_applicatio.md"),
    ("NCA Evolutionary Algorithms (2020)", BASE_DIR / "nca_search_all" / "03_optimizer_comparison_benchmark" / "2020_evolutionary_algorithms_and_their_applications_to_engineering_problems.md"),
    ("CNN-LSTM Stock Prediction (2021)", BASE_DIR / "nca_search_all" / "02_financial_prediction_optimization" / "2021_a_graph_based_cnn_lstm_stock_price_prediction_algorithm_with_leading_indicators.md"),
    ("Stock Market Ensemble Learning (2020)", BASE_DIR / "nca_search_all" / "02_financial_prediction_optimization" / "2020_a_comprehensive_evaluation_of_ensemble_learning_for_stock_market_prediction.md"),
]

def extract_introduction(file_path):
    if not file_path.exists():
        return "File not found."
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    
    # Try to locate Introduction section
    intro_match = re.search(r'(?:#|##|1\b|\bI\b)\.?\s*Introduction.*?(?=(?:#|##|\b2\b|\bII\b)\.?\s*(?:Related Work|Theoretical|Methodology|Background|Literature Review))', text, re.DOTALL | re.IGNORECASE)
    if intro_match:
        intro_text = intro_match.group(0)
        # return first 2,000 characters for concise comparison
        return intro_text[:2500] + ("\n... [truncated for study]" if len(intro_text) > 2500 else "")
    else:
        # Return first 2000 chars of file
        return text[:2000] + "\n... [truncated]"

out_lines = []
out_lines.append("# Análise Comparativa das Introduções — Referências & Periódicos NCA")
out_lines.append("Este documento reúne o estudo comparativo das introduções dos principais artigos de referência do projeto.\n")

for label, path in key_files:
    out_lines.append(f"## {label}")
    out_lines.append(f"**Arquivo**: `{path}`\n")
    intro_excerpt = extract_introduction(path)
    out_lines.append("```text")
    out_lines.append(intro_excerpt.strip())
    out_lines.append("```\n")

out_file = Path("article/references/MASTER_INTRODUCTION_ANALYSIS.md")
out_file.write_text("\n".join(out_lines), encoding="utf-8")
print(f"SUCCESS: Saved master introduction analysis to {out_file} ({out_file.stat().st_size} bytes)")
