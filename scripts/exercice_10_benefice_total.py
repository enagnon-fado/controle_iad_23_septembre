# Exercice 10 : Bénéfice total

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    benefice_total = 0
    
    for ligne in reader:
        chiffre_affaires = float(ligne["chiffre_affaires"])
        depenses = float(ligne["depenses"])
        
        benefice = chiffre_affaires - depenses
        
        benefice_total += benefice
        
print(f"Bénéfice totale = {benefice_total}")
        
    