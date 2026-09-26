# Exercice 20 : Bénéfice par service

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    benefice_par_service = {}
    
    for ligne in reader:
        service = ligne["service"]
        annee = ligne["annee"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        depenses = float(ligne["depenses"])
        
        benefice = chiffre_affaires - depenses
        
        if service not in benefice_par_service:
            benefice_par_service[service] = {
                "annee": annee,
                "total": 0
            }
            
        benefice_par_service[service]["total"] += benefice
        
    for service, informations in benefice_par_service.items():
        print(f"Service : {service}")
        print(f"Bénéfice : {informations['total']}")
        print("-"*50)
        
    service_benefice_plus_eleve = max(
        benefice_par_service,
        key=lambda service : benefice_par_service[service]["total"]
    )
    
print(f"Service ayant généré le bénéfice le plus élevé : {service_benefice_plus_eleve}")
print(f"Bénéfice : {benefice_par_service[service_benefice_plus_eleve]['total']}")
    