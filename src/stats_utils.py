"""Basic statistical analysis of the sales dataset."""
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sales.csv"


def compute_stats(df, column="amount"):
    """Return a dict of basic statistics for the given column."""
    return {
        "count": df[column].count(),
        "mean": df[column].mean(),
        "median": df[column].median(),
        "min": df[column].min(),
        "max": df[column].max(),
        "std": df[column].std(),
    }


def print_stats(stats):
    print("Sales amount statistics")
    print("-" * 30)
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key:>8}: {value:.2f}")
        else:
            print(f"{key:>8}: {value}")


def main():
    df = pd.read_csv(DATA_PATH)
    stats = compute_stats(df)
    print_stats(stats)


if __name__ == "__main__":
    main()
