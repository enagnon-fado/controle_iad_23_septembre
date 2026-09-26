# Exercice 2 : Affichage des données

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    for ligne in reader:
        print(f"Mois : {ligne['mois']}")
        print(f"Régions : {ligne['region']}")
        print(f"Services : {ligne['service']}")
        print(f"Chiffre d'affaire : {ligne['chiffre_affaires']}")
        print(f"Dépenses : {ligne['depenses']}")
        print("-"*50)
        
        

    
    
    