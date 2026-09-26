# Exercice 12 : Bénéfices supérieurs à 4 000 000 FCFA

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    benefice_par_mois = {}

    for ligne in reader:
        mois = ligne["mois"]
        annee = ligne["annee"]

        chiffre_affaires = float(ligne["chiffre_affaires"])
        depenses = float(ligne["depenses"])

        benefice = chiffre_affaires - depenses

        if mois not in benefice_par_mois:
            benefice_par_mois[mois] = {
                "annee": annee,
                "total": 0
            }

        benefice_par_mois[mois]["total"] += benefice

# Afficher les mois dont le bénéfice dépasse 4 000 000 FCFA
for mois, informations in benefice_par_mois.items():
    if informations["total"] > 4000000:
        print(f"Mois : {mois}")
        print(f"Année : {informations['annee']}")
        print(f"Bénéfice total : {informations['total']} FCFA")