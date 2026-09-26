# Exercice 16 : Répartition des clients par région

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    nb_total_clients_par_region = {}
    
    for ligne in reader:
        region = ligne["region"]
        annee = ligne["annee"]
        clients = int(ligne["clients"])
        
        if region not in nb_total_clients_par_region:
            nb_total_clients_par_region[region] = {
                "annee": annee,
                "total": 0
            }
            
        nb_total_clients_par_region[region]["total"] += clients
        
    # Afficher le nombre de clients par région
    for region, informations in nb_total_clients_par_region.items():
        print(f"Région : {region}")
        print(f"Nombre total de clients : {informations['total']}")
        print("-"*50)
    
    # Afficher la région ayant enregistré le plus grand nombre de clients    
    region_grand_clients = max(
        nb_total_clients_par_region,
        key=lambda region : nb_total_clients_par_region[region]["total"]
    )
    
print(f"Région ayant enregistré le plus grand nombre de clients : {region_grand_clients}")
print(f"Nombre de clients : {nb_total_clients_par_region[region_grand_clients]['total']}")