"""Sales transaction statistical analysis (analyser_ventes)."""

import csv
from pathlib import Path


def analyser_ventes(transactions):
    """Analyze a list of sale amounts: clean, compute stats, detect outliers."""
    valid = [amount for amount in transactions if amount > 0]

    count = len(valid)
    total = sum(valid)
    mean = total / count if count else 0

    sorted_values = sorted(valid)
    if count == 0:
        median = 0
    elif count % 2 == 0:
        median = (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
    else:
        median = sorted_values[count // 2]

    variance = sum((x - mean) ** 2 for x in valid) / count if count else 0
    std_dev = variance ** 0.5

    outliers = [x for x in valid if x > 2 * mean]

    return {
        "nombre_transactions": count,
        "somme_totale": total,
        "moyenne": mean,
        "mediane": median,
        "ecart_type": std_dev,
        "maximum": max(valid) if valid else None,
        "minimum": min(valid) if valid else None,
        "outliers": outliers,
    }


def charger_transactions(chemin_csv):
    """Read the 'amount' column from a sales CSV file into a list of floats."""
    with open(chemin_csv, newline="", encoding="utf-8") as f:
        return [float(row["amount"]) for row in csv.DictReader(f)]


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent.parent / "data" / "sales.csv"
    sample_transactions = charger_transactions(csv_path)
    report = analyser_ventes(sample_transactions)

    print("Rapport d'analyse des ventes")
    print("-" * 30)
    for key, value in report.items():
        print(f"{key}: {value}")
