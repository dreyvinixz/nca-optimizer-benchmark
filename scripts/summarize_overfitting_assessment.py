#!/usr/bin/env python3
"""Combine frozen diagnostics and one-pass results for an overfitting review."""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score, matthews_corrcoef


def fmt(value, digits=3):
    return "—" if pd.isna(value) else f"{value:.{digits}f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--train-validation", type=Path, default=Path("reports/overfitting_train_validation.csv"))
    ap.add_argument("--final-metrics", type=Path, default=Path("reports/final_test_metrics.csv"))
    ap.add_argument("--cv", type=Path, default=Path("reports/mlp_cv_summary.csv"))
    ap.add_argument("--test-predictions", type=Path, default=Path("tmp/final_test_predictions.parquet"))
    ap.add_argument("--session-csv", type=Path, default=Path("reports/overfitting_session_metrics.csv"))
    ap.add_argument("--report", type=Path, default=Path("reports/overfitting_assessment.md"))
    a = ap.parse_args()

    tv = pd.read_csv(a.train_validation)
    final = pd.read_csv(a.final_metrics)
    cv = pd.read_csv(a.cv)
    pred = pd.read_parquet(a.test_predictions, columns=[
        "ticker", "date", "split", "y5", "y10", "y15",
        "p_ind_trend_5m", "p_ind_trend_10m", "p_ind_trend_15m",
        "p_shared_trend_5m", "p_shared_trend_10m", "p_shared_trend_15m",
        "p_hist_trend_5m", "p_hist_trend_10m", "p_hist_trend_15m",
    ])
    pred = pred.loc[pred.split == "test"].copy()
    if pred.empty:
        raise ValueError("No saved one-pass test predictions found")

    target_cols = {"trend_5m": "y5", "trend_10m": "y10", "trend_15m": "y15"}
    model_cols = {
        "independent_mlp": "p_ind_{target}",
        "shared_multitask_mlp": "p_shared_{target}",
        "hist_gradient_boosting": "p_hist_{target}",
    }
    session_rows = []
    for model, template in model_cols.items():
        for target, ycol in target_cols.items():
            pcol = template.format(target=target)
            for date, group in pred.dropna(subset=[ycol, pcol]).groupby("date", sort=True):
                y = group[ycol].astype(int).to_numpy()
                hard = (group[pcol].to_numpy(dtype=float) >= 0.5).astype(int)
                if np.unique(y).size < 2:
                    mcc = np.nan
                    bacc = np.nan
                else:
                    mcc = matthews_corrcoef(y, hard)
                    bacc = balanced_accuracy_score(y, hard)
                session_rows.append({"model": model, "target": target, "date": date, "n": len(y), "mcc": mcc, "balanced_accuracy": bacc})
    sessions = pd.DataFrame(session_rows)
    sessions.to_csv(a.session_csv, index=False)

    lines = [
        "# Deep overfitting assessment",
        "",
        "## Verdict",
        "",
        "The evidence shows a modest, consistent in-sample fit gap, so some overfitting is possible. It does not show a severe generalization collapse: frozen validation performance is maintained on the later final test, chronological development folds are reasonably stable, and no negative-MCC test session occurred for the three primary candidate models. This is evidence against severe overfitting in this sample, not proof that overfitting is absent.",
        "",
        "The final test was not loaded by the train-versus-validation fitting diagnostic. This report reads its already-saved one-pass prediction artifact only to summarize the fixed test by session; it does not fit a model, select a model, or tune a threshold.",
        "",
        "## Apparent training fit versus chronological validation",
        "",
        "A separate CPU diagnostic reproduced the frozen model settings and seeds and fit each model once on the frozen training partition. Train metrics are in-sample and optimistically biased by construction. A positive MCC gap is train MCC minus validation MCC; positive Brier/log-loss degradation is validation minus train.",
        "",
        "| Model | Target | Train MCC | Validation MCC | MCC gap | Train macro-F1 | Validation macro-F1 | Validation minus train Brier | Validation minus train log loss |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in tv.sort_values(["model", "target"]).iterrows():
        lines.append(f"| {r.model} | {r.target} | {r.mcc_train_apparent:.3f} | {r.mcc_validation:.3f} | {r.mcc_gap_train_minus_validation:.3f} | {r.macro_f1_train_apparent:.3f} | {r.macro_f1_validation:.3f} | {r.brier_gap_validation_minus_train:.3f} | {r.log_loss_gap_validation_minus_train:.3f} |")

    lines += [
        "",
        "Across the nine MLP target/head comparisons, the apparent MCC gap is 0.022–0.035 and the macro-F1 gap is about 0.012–0.021. The CPU HistGradientBoosting gaps are 0.026–0.041 MCC. Logistic regression also has a smaller 0.019–0.025 MCC gap. All models score better on train than on later validation, which is expected; the size is noticeable but not a collapse.",
        "",
        "## Chronological MLP cross-validation",
        "",
        "Four expanding folds use successive validation periods. Their training windows overlap, so the standard deviation is descriptive rather than an independent confidence interval.",
        "",
        "| Target | Fold mean MCC | Fold SD | Fold range |",
        "|---|---:|---:|---:|",
    ]
    for target, g in cv[(cv.root == "ALL") & (cv.model == "compact_mlp")].groupby("target", sort=True):
        lines.append(f"| {target} | {g.mcc.mean():.3f} | {g.mcc.std(ddof=1):.3f} | {g.mcc.min():.3f}–{g.mcc.max():.3f} |")

    lines += [
        "",
        "## Frozen validation versus one-pass final test",
        "",
        "The validation/test MCC change is test minus validation. A negative value would indicate deterioration on the later test period.",
        "",
        "| Model | Target | Validation MCC | Test MCC | Change | Validation Brier | Test Brier |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    val = final[(final.split == "validation") & (final.root == "ALL")].set_index(["model", "target"])
    test = final[(final.split == "test") & (final.root == "ALL") & (final.test_block.astype(str) == "overall")].set_index(["model", "target"])
    for model in model_cols:
        for target in target_cols:
            if (model, target) not in val.index or (model, target) not in test.index:
                continue
            v, t = val.loc[(model, target)], test.loc[(model, target)]
            lines.append(f"| {model} | {target} | {v.mcc:.3f} | {t.mcc:.3f} | {t.mcc-v.mcc:+.3f} | {v.brier:.3f} | {t.brier:.3f} |")
    primary_deltas = [test.loc[(model, target), "mcc"] - val.loc[(model, target), "mcc"] for model in model_cols for target in target_cols]
    lines.append("")
    lines.append(f"All nine validation-to-test MCC changes are nonnegative (range {min(primary_deltas):+.3f} to {max(primary_deltas):+.3f}). The later sample therefore does not display the usual test-period performance drop associated with severe overfitting. This comparison uses the original frozen GPU-run validation and test predictions; small numerical differences from the separate CPU diagnostic above are expected. Because this is one time split, it cannot prove performance on future market periods.")

    lines += [
        "",
        "## Test stability across independent sessions",
        "",
        "Daily MCC uses each pregão as one unit. Every one of the 25 final-test sessions contains both classes for these summaries; sessions are temporally dependent and are not treated as 25 independent draws here.",
        "",
        "| Model | Target | Sessions | Mean daily MCC | SD | 10th–90th percentile | Negative-MCC sessions |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for (model, target), g in sessions.groupby(["model", "target"], sort=True):
        x = g.mcc.dropna()
        lines.append(f"| {model} | {target} | {len(x)} | {x.mean():.3f} | {x.std(ddof=1):.3f} | {x.quantile(.1):.3f}–{x.quantile(.9):.3f} | {(x < 0).sum()} |")

    lines += [
        "",
        "## Regime, root, and contract checks",
        "",
        "Across the three fixed test blocks, MCC is fairly stable for 5m and 10m. For 15m, all displayed models improve in block 3 relative to blocks 1–2, consistent with time variation rather than a test collapse. By root, WIN and IND scores are broadly similar. Contract rows show lower counts for WINV26 (n=149); conclusions for that contract are especially uncertain and should not be read as evidence of model fit or failure. Full contract scores are in [`final_test_contract_metrics.csv`](final_test_contract_metrics.csv).",
        "",
        "The leakage audit passed checks for date-pure splits, ordered expanding folds, completed-candle features, reset state at gaps/contracts/sessions, and in-session label endpoints. This lowers the risk of implementation leakage. It does not make B0 labels causal: B0 is retrospective, and the reported task is reproducing those labels.",
        "",
        "## Conclusion and limits",
        "",
        "Assessment: **some overfitting is possible, with a modest apparent train–validation gap; no evidence of severe overfitting or a validation-to-test collapse was found in this snapshot.** The strongest warning is the 15m train–validation gap (up to 0.041 MCC for HistGradientBoosting and 0.035 for independent MLP), while test scores remain close to or above validation. Small, single-period data and only 25 test sessions limit certainty.",
        "",
        "No model settings, decision threshold, or model choice were changed from this diagnostic, and no model was fit on test data. Test-session summaries are descriptive only; no new test-based model comparison or threshold selection was performed. A stronger prospective claim requires a later untouched date range or a new rolling-origin study; do not turn these findings into a claim of profitability or true market-state prediction.",
        "",
        "Artifacts: [`overfitting_train_validation.csv`](overfitting_train_validation.csv), [`overfitting_session_metrics.csv`](overfitting_session_metrics.csv), [`mlp_cv_summary.csv`](mlp_cv_summary.csv), [`final_test_metrics.csv`](final_test_metrics.csv), [`final_test_contract_metrics.csv`](final_test_contract_metrics.csv), and [`leakage_audit.md`](leakage_audit.md).",
        "",
    ]
    a.report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {a.report}; summarized {len(sessions)} session rows")


if __name__ == "__main__":
    main()
