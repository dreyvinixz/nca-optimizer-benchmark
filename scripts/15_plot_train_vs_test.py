"""Calculate and plot Train vs Test performance to analyze overfitting."""

import json
import logging
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from src.benchmark import prepare_benchmark
from src.evaluation.metrics import compute_classification_metrics

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("train_vs_test")

def evaluate_model(model_type, candidate, X_train, y_train, X_test, y_test, seed, config):
    if model_type == "rf":
        n_estimators = int(candidate["n_estimators"])
        max_depth = int(candidate["max_depth"])
        min_samples_split = int(candidate["min_samples_split"])
        min_samples_leaf = int(candidate["min_samples_leaf"])
        max_features = candidate.get("max_features", "sqrt")
        class_weight = candidate.get("class_weight", None)
        
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            class_weight=class_weight,
            random_state=seed,
            n_jobs=1,
        )
        model.fit(X_train, y_train)
        
        y_pred_train = model.predict(X_train)
        y_proba_train = model.predict_proba(X_train)[:, 1]
        y_pred_test = model.predict(X_test)
        y_proba_test = model.predict_proba(X_test)[:, 1]
        
    elif model_type == "svm":
        C = float(candidate["C"])
        kernel = candidate["kernel"]
        gamma = float(candidate["gamma"]) if kernel == "rbf" else "scale"
        
        model = SVC(
            C=C,
            gamma=gamma,
            kernel=kernel,
            probability=True,
            random_state=seed,
            max_iter=50000,
        )
        model.fit(X_train, y_train)
        
        y_pred_train = model.predict(X_train)
        y_proba_train = model.predict_proba(X_train)[:, 1]
        y_pred_test = model.predict(X_test)
        y_proba_test = model.predict_proba(X_test)[:, 1]
        
    elif model_type == "mlp":
        from src.models.mlp import fit_predict_mlp
        # Train once to predict test, train again to predict train (simplest way to avoid session wipe issues)
        y_pred_test, y_proba_test, _, _ = fit_predict_mlp(X_train, y_train, X_test, candidate, config["experiment"]["model"], seed)
        y_pred_train, y_proba_train, _, _ = fit_predict_mlp(X_train, y_train, X_train, candidate, config["experiment"]["model"], seed)
        
    else:
        raise ValueError(f"Unknown model_type: {model_type}")
        
    train_metrics = compute_classification_metrics(y_train, y_pred_train, y_proba_train)
    test_metrics = compute_classification_metrics(y_test, y_pred_test, y_proba_test)
    
    return train_metrics["mcc"], test_metrics["mcc"]

def main():
    data, config = prepare_benchmark()
    
    models = ["mlp", "svm", "rf", "cnn"]
    optimizers = ["random_search", "ga", "pso", "de", "gwo"]
    
    # We will use the full training set (train + val) like in evaluate_best_on_test
    X_train_full = np.vstack([data.X_train, data.X_val])
    y_train_full = np.concatenate([data.y_train, data.y_val])

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_full).astype("float32")
    X_test_scaled = scaler.transform(data.X_test).astype("float32")
    
    results = []
    
    for model in models:
        for opt in optimizers:
            path = Path(f"outputs/phase2/metrics/{model}_{opt}_best_by_seed.csv")
            if not path.exists():
                continue
                
            df = pd.read_csv(path)
            for _, row in df.iterrows():
                seed = int(row["seed"])
                candidate = json.loads(row["decoded_hyperparameters"])
                
                logger.info(f"Retraining {model} - {opt} - Seed {seed} for Train vs Test evaluation")
                train_mcc, test_mcc = evaluate_model(model, candidate, X_train_scaled, y_train_full, X_test_scaled, data.y_test, seed, config)
                
                results.append({
                    "Model": model.upper(),
                    "Optimizer": opt.upper().replace("_", " "),
                    "Seed": seed,
                    "Split": "Train",
                    "MCC": train_mcc
                })
                results.append({
                    "Model": model.upper(),
                    "Optimizer": opt.upper().replace("_", " "),
                    "Seed": seed,
                    "Split": "Test",
                    "MCC": test_mcc
                })

    if not results:
        logger.error("No data found to plot. Run the benchmark first.")
        return
        
    results_df = pd.DataFrame(results)
    
    # Set beautiful style
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.2)
    
    # Plot Train vs Test MCC
    g = sns.catplot(
        data=results_df,
        kind="bar",
        x="Model",
        y="MCC",
        hue="Split",
        col="Optimizer",
        col_wrap=3,
        height=4,
        aspect=1.2,
        palette="mako",
        errorbar="sd"
    )
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle("Train vs Test Performance (MCC) per Model and Optimizer")
    
    out_dir = Path("outputs/phase2/figures")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "train_vs_test_mcc.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    logger.info(f"Saved Train vs Test comparison to {out_path}")

if __name__ == "__main__":
    main()
