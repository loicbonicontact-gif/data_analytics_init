"""Sales transaction statistical analysis (analyser_ventes)."""

import csv
import os


def calculer_etendue(valeurs):
    """
    Calcule l'étendue d'une liste de valeurs.
    L'étendue est la différence entre la valeur maximale et la valeur minimale.
    """
    if not valeurs:
        return 0.0
    return max(valeurs) - min(valeurs)


def analyser_ventes(transactions):
    """
    Analyse une liste de montants de ventes :
    - Nettoie les données (ignore les valeurs négatives ou nulles)
    - Calcule les indicateurs statistiques clés (moyenne, médiane, écart-type, étendue)
    - Détecte les transactions anormalement élevées (outliers)
    """
    
    # --- 1. Nettoyage des données ---
    # On conserve uniquement les montants strictement positifs (ignore les erreurs de saisie)
    valid = [amount for amount in transactions if amount > 0]

    count = len(valid)
    total = sum(valid)
    mean = total / count if count else 0

    # --- 2. Calculs statistiques ---
    # Calcul de la médiane (valeur centrale une fois la liste triée)
    sorted_values = sorted(valid)
    if count == 0:
        median = 0
    elif count % 2 == 0:
        # Si le nombre de valeurs est pair, on fait la moyenne des deux valeurs centrales
        median = (sorted_values[count // 2 - 1] + sorted_values[count // 2]) / 2
    else:
        # Si impair, on prend la valeur exacte du milieu
        median = sorted_values[count // 2]

    # Calcul de la variance et de l'écart-type (mesure de la dispersion autour de la moyenne)
    variance = sum((x - mean) ** 2 for x in valid) / count if count else 0
    std_dev = variance ** 0.5

    # Appel de notre nouvelle fonction pour l'étendue
    etendue = calculer_etendue(valid)

    # --- 3. Détection des anomalies (Outliers) ---
    # Une transaction est considérée comme anormale si elle dépasse 2 fois la moyenne
    outliers = [x for x in valid if x > 2 * mean]

    # --- 4. Retour des résultats sous forme de dictionnaire structuré ---
    return {
        "nombre_transactions": count,
        "somme_totale": total,
        "moyenne": mean,
        "mediane": median,
        "ecart_type": std_dev,
        "etendue": etendue,  # <-- Ajout de l'étendue ici
        "maximum": max(valid) if valid else None,
        "minimum": min(valid) if valid else None,
        "outliers": outliers,
    }


def charger_donnees_csv(chemin_fichier):
    """
    Lit un fichier CSV et retourne une liste de montants (float).
    Gère les formats de nombres à virgule (ex: '15,50' -> '15.50').
    """
    transactions = []
    
    if not os.path.exists(chemin_fichier):
        print(f"❌ Erreur : Le fichier '{chemin_fichier}' est introuvable.")
        return transactions

    with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        
        for ligne in lecteur:
            if not ligne:
                continue
            
            try:
                # On lit la DEUXIEME colonne (index 1) où se trouvent les montants
                valeur_str = ligne[1].replace(',', '.')
                montant = float(valeur_str)
                transactions.append(montant)
            except (ValueError, IndexError):
                # Ignore les lignes qui ne sont pas des nombres ou qui n'ont pas de 2ème colonne
                continue
                
    return transactions


if __name__ == "__main__":
    # 1. Trouver le dossier où se trouve ce script (dossier 'src')
    dossier_src = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Construire et "nettoyer" le chemin pour aller dans 'data/sales.csv'
    chemin_csv = os.path.normpath(os.path.join(dossier_src, "..", "data", "sales.csv"))
    
    # 3. Charger les données depuis le fichier CSV
    sample_transactions = charger_donnees_csv(chemin_csv)
    
    # 4. Analyser les données et afficher le rapport
    if sample_transactions:
        report = analyser_ventes(sample_transactions)

        # --- Affichage amélioré et formaté ---
        print("📊 Rapport d'analyse des ventes 📊")
        print("=" * 40)
        
        for key, value in report.items():
            # Rend la clé plus jolie à lire (ex: "somme_totale" -> "Somme totale")
            cle_affichee = key.replace('_', ' ').capitalize()
            
            # Formate l'affichage : les nombres à virgule auront 2 décimales et le symbole €
            if isinstance(value, float):
                print(f"{cle_affichee:<20}: {value:>10.2f} €")
            elif isinstance(value, list) and value:
                # Si c'est une liste d'outliers non vide
                print(f"{cle_affichee:<20}: {value} €")
            else:
                # Pour les nombres entiers (comme le nombre de transactions)
                print(f"{cle_affichee:<20}: {value}")
                
        print("=" * 40)
    else:
        print("❌ Aucune donnée à analyser.")