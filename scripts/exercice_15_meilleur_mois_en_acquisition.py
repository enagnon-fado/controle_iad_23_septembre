# Exercice 15 : Meilleur mois en acquisition

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    nouveaux_clients_par_mois = {}
    
    for ligne in reader:
        mois = ligne["mois"]
        annee = ligne["annee"]
        nouveaux_clients = int(ligne["nouveaux_clients"])
        
        if mois not in nouveaux_clients_par_mois:
            nouveaux_clients_par_mois[mois] = {
                "annee": annee,
                "total": 0
            }
            
        nouveaux_clients_par_mois[mois]["total"] += nouveaux_clients
        
    mois_nouveaux_clients_max = max(
        nouveaux_clients_par_mois,
        key=lambda mois : nouveaux_clients_par_mois[mois]["total"]
    )
    
print(f"Mois : {mois_nouveaux_clients_max}")
print(f"Année : {nouveaux_clients_par_mois[mois_nouveaux_clients_max]['annee']}")
print(f"Nombre de nouveaux clients : {nouveaux_clients_par_mois[mois_nouveaux_clients_max]['total']}")
        
        