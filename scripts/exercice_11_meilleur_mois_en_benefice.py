# Exercice 11 : Meilleur mois en bénéfice

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    benefice_par_mois = {}
    
    for ligne in reader:
        mois = ligne["mois"]
        annee = ligne["annee"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        depenses = float(ligne["depenses"])
        
        benefice = chiffre_affaires - depenses
        
        if mois not in benefice_par_mois:
            benefice_par_mois[mois] = {
                "annee": annee,
                "total": 0
            }
            
        benefice_par_mois[mois]["total"] += benefice
        
mois_benefice_max = max(
    benefice_par_mois, 
    key=lambda mois : benefice_par_mois[mois]["total"]
    )
        
print(f"Mois : {mois_benefice_max}")
print(f"Année : {benefice_par_mois[mois_benefice_max]['annee']}")
print(f"Montant du bénéfice : {benefice_par_mois[mois_benefice_max]['total']}")
    
        