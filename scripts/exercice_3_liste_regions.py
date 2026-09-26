# Exercice 3 : Liste des régions

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    regions = set()
    
    for ligne in reader:
        regions.add(ligne["region"])
        
for region in regions:
    print(region)