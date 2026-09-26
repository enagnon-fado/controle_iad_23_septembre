# Exercice 21 : Évolution entre janvier et décembre

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaires_janvier = 0
    chiffre_affaires_decembre = 0
    
    for ligne in reader:
        mois = ligne["mois"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        
        if mois == "Janvier":
            chiffre_affaires_janvier += chiffre_affaires
        elif mois == "Décembre":
            chiffre_affaires_decembre += chiffre_affaires
            
        evolution = (
            (chiffre_affaires_decembre - chiffre_affaires_janvier)
            /chiffre_affaires_janvier
        )*100
        
print(f"Chiffre d'affaire janvier : {chiffre_affaires_janvier}")
print(f"Chiffre d'affaire décembre : {chiffre_affaires_decembre}")
print(f"Evolution du chiffre d'affaire : {evolution:.2f}%")