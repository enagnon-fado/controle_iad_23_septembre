# Exercice 13 : Nombre total de clients

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    client_total = 0
    
    for ligne in reader:
        clients = int(ligne["clients"])
        client_total += clients
        
print(f"Nombre total de clients : {client_total}")