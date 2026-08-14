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