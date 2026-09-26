# Exercice 22 : Identification des mois de croissance

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaire_par_mois = {}
    
    for ligne in reader:
        mois = ligne["mois"]
        annee = ligne["annee"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        
        if mois not in chiffre_affaire_par_mois:
            chiffre_affaire_par_mois[mois] = {
                "annee": annee,
                "total": 0
            }
            
        chiffre_affaire_par_mois[mois]["total"] += chiffre_affaires
        
ordre_mois = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre"
]

for i in range(1, len(ordre_mois)):
    mois_actuel = ordre_mois[i]
    mois_precedent = ordre_mois[i - 1]
    
    chiffre_affaires_actuel = chiffre_affaire_par_mois[mois_actuel]["total"]
    chiffre_affaires_precedent = chiffre_affaire_par_mois[mois_precedent]["total"]
    
    if chiffre_affaires_actuel > chiffre_affaires_precedent:
        print(
            f"{mois_actuel} : "
            f"{chiffre_affaires_actuel} : "
            f"Augmentation par rapport à {mois_precedent}"
        )
        print("-"*50)