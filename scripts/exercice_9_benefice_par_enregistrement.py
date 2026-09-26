# Exercice 9 : Bénéfice par enregistrement

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for ligne in reader:
        mois = ligne["mois"]
        region = ligne["region"]
        service = ligne["service"]

        chiffre_affaires = float(ligne["chiffre_affaires"])
        depenses = float(ligne["depenses"])

        benefice = chiffre_affaires - depenses

        print(f"Mois : {mois}")
        print(f"Région : {region}")
        print(f"Service : {service}")
        print(f"Chiffre d'affaires : {chiffre_affaires:,} FCFA")
        print(f"Dépenses : {depenses:,} FCFA")
        print(f"Bénéfice : {benefice:,} FCFA")
        print("-"*50)

