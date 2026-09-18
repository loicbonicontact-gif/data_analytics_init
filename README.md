# Onboarding Data Analyst — DataCorp

Projet d'entraînement : premiers scripts Python d'analyse statistique de
données de ventes, écrits pendant ma phase d'onboarding Data Analyst.

## Contenu

| Fichier | Description |
|---|---|
| `src/stats_utils.py` | Fonctions d'analyse statistique de transactions de vente : nettoyage des données, calcul de la moyenne, médiane, écart-type, étendue, et détection des transactions anormalement élevées (outliers). Charge les montants depuis un fichier CSV. |
| `notes.txt` | Journal de bord de l'apprentissage. |

## Utilisation

```bash
python src/stats_utils.py
```

Le script lit `data/sales.csv` (montants en 2ème colonne) et affiche un
rapport statistique des ventes.

## Outils utilisés

Python (bibliothèque standard : `csv`, `os`).
