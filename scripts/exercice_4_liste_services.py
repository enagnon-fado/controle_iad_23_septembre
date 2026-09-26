# Exercice 4 : Liste des services

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    services = set()
    
    for ligne in reader:
        services.add(ligne["service"])
        
for service in sorted(services):
    print(service)