#Exercice 1 : Lecture du fichier

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for ligne in reader:
        print(ligne)
