# Exercice 25 : Classement des services

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaire_par_service = {}
    
    for ligne in reader:
        service = ligne["service"]
        annee = ligne["annee"]
        chiffre_affaires = float(ligne["chiffre_affaires"])
        
        if service not in chiffre_affaire_par_service:
            chiffre_affaire_par_service[service] = {
                "annee": annee,
                "total": 0
            }
            
        chiffre_affaire_par_service[service]["total"] += chiffre_affaires
        
services_classes = sorted(
    chiffre_affaire_par_service,
    key=lambda service : chiffre_affaire_par_service[service]["total"],
    reverse=True
)

for rang, service in enumerate(services_classes, start=1):
    total = chiffre_affaire_par_service[service]["total"]
    print(f"Numéro {rang} : {service} - {total}")
    print("-"*50)
        