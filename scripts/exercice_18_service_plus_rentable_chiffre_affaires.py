# Exercice 18 : Service le plus rentable en chiffre d'affaires

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
        
    service_plus_rentable = max(
        chiffre_affaires_par_service,
        key=lambda service : chiffre_affaires_par_service[service]["total"]
    )
    
print(f"Service plus rentable : {service_plus_rentable}")
print(f"Chiffre d'affaire : {chiffre_affaires_par_service[service_plus_rentable]['total']}")