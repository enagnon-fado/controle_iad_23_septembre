# Exercice 6 : Chiff re d'aff aires moyen

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaire_total = 0
    mois = set()
    
    for ligne in reader:
        chiffre_affaire_total += float(ligne["chiffre_affaires"])
        mois.add(ligne["mois"])
        
chiffre_affaire_moyen = chiffre_affaire_total/len(mois)

print(f"Nombre de mois = {len(mois)}")
print(f"Chiffre d'affaire total = {chiffre_affaire_total}")
print(f"Chiffre d'affaire moyen par mois = {chiffre_affaire_moyen}")