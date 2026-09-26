# Exercice 17 : Chiffre d'affaires par service

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaires_par_service = {}
    
    for ligne in reader:
        service = ligne["service"]
        annee = ligne["annee"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        
        if service not in chiffre_affaires_par_service:
            chiffre_affaires_par_service[service] = {
                "annee": annee,
                "total": 0
            }
            
        chiffre_affaires_par_service[service]["total"] += chiffre_affaires

    for service, informations in chiffre_affaires_par_service.items():
        print(f"Service : {service}")
        print(f"Chiffre d'affaire : {informations['total']}")
        print("-"*50)