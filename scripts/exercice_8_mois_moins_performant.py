# Exercice 8 : Mois le moins performant

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
        
mois_min = min(
    chiffre_affaire_par_mois, 
    key=lambda mois : chiffre_affaire_par_mois[mois]["total"]
    )

print(f"Mois : {mois_min}")
print(f"Année : {chiffre_affaire_par_mois[mois_min]["annee"]}")
print(f"Chiffre d'affaire : {chiffre_affaire_par_mois[mois_min]["total"]}")