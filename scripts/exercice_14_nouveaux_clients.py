# Exercice 14 : Nouveaux clients

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    total_nouveaux_clients = 0
    
    for ligne in reader:
        nouveaux_clients = int(ligne["nouveaux_clients"])
        total_nouveaux_clients += nouveaux_clients
        
print(f"Nombre total de nouveaux clients : {total_nouveaux_clients}")