# visualizer.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_cumulative_returns(prices_dict, save_path="reports/cumulative_returns.png"):
   
    df = pd.DataFrame(prices_dict)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

    daily_returns = df.pct_change()
    cumulative_df = (1 + daily_returns).cumprod()

    plt.figure(figsize=(10, 6))
    for ticker in cumulative_df.columns:
        plt.plot(
            cumulative_df.index, cumulative_df[ticker], label=ticker, linewidth=2
        )

    plt.title("Cumulative Returns Comparison", fontsize=14, fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Growth Multiplier (1.0 = Base)")
    plt.legend(title="Tickers")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Cumulative return chart saved to {save_path}")


def plot_correlation_heatmap(
    prices_dict, save_path="reports/correlation_heatmap.png"
):
    
    df = pd.DataFrame(prices_dict)
    if "Date" in df.columns:
        df.drop(columns=["Date"], inplace=True)

    daily_returns = df.pct_change().dropna()
    corr_matrix = daily_returns.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        vmax=1.0,
        vmin=-1.0,
        linewidths=0.5,
        fmt=".2f",
    )
    plt.title(
        "Stock Return Correlation Heatmap", fontsize=14, fontweight="bold"
    )
    plt.tight_layout()

    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Correlation heatmap saved to {save_path}") 

def plot_sharpe_ratios(report_dict, save_path="reports/sharpe_ratios.png"):
    """
    Plots a bar chart comparing the Sharpe Ratios of all individual stocks.
    Reads data directly from the generated report dictionary.
    """
    tickers = []
    sharpe_ratios = []

    # Extract individual stock Sharpe ratios from the report dictionary
    for ticker, metrics in report_dict.items():
        if isinstance(metrics, dict) and "sharpe_ratio" in metrics:
            tickers.append(ticker)
            sharpe_ratios.append(metrics["sharpe_ratio"])

    plt.figure(figsize=(8, 5))
    
    # Create horizontal bar plot
    bars = plt.barh(tickers, sharpe_ratios, color="skyblue", edgecolor="navy")
    
    # Add values on top of bars
    plt.bar_label(bars, fmt="%.2f", padding=3)

    # Reference line at 0
    plt.axvline(0, color="black", linewidth=0.8, linestyle="--")

    plt.title("Sharpe Ratio Comparison (Risk-Adjusted Performance)", fontsize=13, fontweight="bold")
    plt.xlabel("Sharpe Ratio")
    plt.ylabel("Tickers")
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()

    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Sharpe ratio chart saved to {save_path}")    