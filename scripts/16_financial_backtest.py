import sys
from pathlib import Path
import pandas as pd
import numpy as np
from glob import glob

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

def calculate_max_drawdown(equity_curve: pd.Series) -> float:
    roll_max = equity_curve.cummax()
    drawdown = equity_curve - roll_max
    return drawdown.min()

def main():
    predictions_dir = project_root / "outputs" / "phase2" / "predictions"
    raw_data_path = project_root / "data" / "raw" / "merged_output.csv"
    output_dir = project_root / "outputs" / "phase2" / "tables"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading market data...")
    market_data = pd.read_csv(raw_data_path, usecols=["datetime", "open", "close"])
    market_data["datetime"] = pd.to_datetime(market_data["datetime"])
    
    pred_files = glob(str(predictions_dir / "*_predictions.csv"))
    if not pred_files:
        print("No prediction files found. Run evaluations first.")
        return

    # Transaction cost in points (Slippage + Emoluments)
    # Mini Index (WIN): 1 tick = 5 points. Using 5 points as a realistic conservative cost.
    TRANSACTION_COST = 5.0 

    results = []

    for file_path in pred_files:
        filename = Path(file_path).stem
        parts = filename.replace("_predictions", "").split("_", 1)
        if len(parts) == 2:
            model_type, optimizer = parts[0], parts[1]
        else:
            model_type, optimizer = "unknown", filename

        print(f"Processing backtest for {model_type} - {optimizer}...")
        
        preds = pd.read_csv(file_path)
        preds["datetime"] = pd.to_datetime(preds["datetime"])
        
        # Merge to get open and close prices for the predicted bar
        merged = pd.merge(preds, market_data, on="datetime", how="inner")
        
        if merged.empty:
            continue
            
        # Calculate Trade Return in points
        # Long (y_pred == 1): return = Close - Open
        # Short (y_pred == 0): return = Open - Close
        merged["long_return"] = merged["close"] - merged["open"]
        merged["short_return"] = merged["open"] - merged["close"]
        
        merged["trade_return"] = np.where(merged["y_pred"] == 1, merged["long_return"], merged["short_return"])
        
        # Subtract transaction costs
        merged["trade_return_net"] = merged["trade_return"] - TRANSACTION_COST
        
        # Win Rate
        winning_trades = len(merged[merged["trade_return_net"] > 0])
        total_trades = len(merged)
        win_rate = winning_trades / total_trades if total_trades > 0 else 0
        
        # Profit Factor
        gross_profit = merged[merged["trade_return_net"] > 0]["trade_return_net"].sum()
        gross_loss = abs(merged[merged["trade_return_net"] < 0]["trade_return_net"].sum())
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else float("inf")
        
        # Total Profit
        total_profit = merged["trade_return_net"].sum()
        
        # Max Drawdown
        merged["equity"] = merged["trade_return_net"].cumsum()
        max_drawdown = calculate_max_drawdown(merged["equity"])
        
        # Daily Sharpe Ratio
        merged["date"] = merged["datetime"].dt.date
        daily_returns = merged.groupby("date")["trade_return_net"].sum()
        mean_daily = daily_returns.mean()
        std_daily = daily_returns.std()
        
        if std_daily > 0:
            sharpe_ratio = (mean_daily / std_daily) * np.sqrt(252)
        else:
            sharpe_ratio = 0.0

        results.append({
            "model": model_type,
            "optimizer": optimizer,
            "total_trades": total_trades,
            "total_profit_points": total_profit,
            "win_rate": win_rate,
            "profit_factor": profit_factor,
            "max_drawdown_points": max_drawdown,
            "sharpe_ratio_annualized": sharpe_ratio
        })

    if results:
        df_results = pd.DataFrame(results)
        df_results = df_results.sort_values(by="sharpe_ratio_annualized", ascending=False)
        out_csv = output_dir / "financial_backtest_summary.csv"
        df_results.to_csv(out_csv, index=False)
        print(f"\nFinancial backtest complete. Summary saved to {out_csv}")
        print(df_results.to_string(index=False))

if __name__ == "__main__":
    main()
