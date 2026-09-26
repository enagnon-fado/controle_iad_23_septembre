# Exercice 5 : Chiffre d'affaires total

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaire_total = 0
    
    for ligne in reader:
        chiffre_affaire_total += float(ligne["chiffre_affaires"])
        
print(f"Chiffre d'affaire total = {chiffre_affaire_total}")