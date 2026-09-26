# Exercice 24 : Classement des mois

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaires_par_mois = {}
    
    for ligne in reader:
        mois = ligne["mois"]
        annee = ligne["annee"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        
        if mois not in chiffre_affaires_par_mois:
            chiffre_affaires_par_mois[mois] = {
                "annee": annee,
                "total": 0
            }
            
        chiffre_affaires_par_mois[mois]["total"] += chiffre_affaires
        
mois_classes = sorted(
    chiffre_affaires_par_mois,
    key=lambda mois : chiffre_affaires_par_mois[mois]["total"],
    reverse=True
)

for rang, mois in enumerate(mois_classes, start=1):
    total = chiffre_affaires_par_mois[mois]["total"]
    print(f"Numéro {rang} : {mois} - {total}")
    print("-"*50)