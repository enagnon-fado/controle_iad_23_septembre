# Exercice 28 : Analyse de la satisfaction client

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    for ligne in reader:
        satisfaction = float(ligne["satisfaction"])
        
        if satisfaction >= 90:
            appreciation = "Très bonne"
        elif satisfaction >= 80:
            appreciation = "Bonne"
        elif satisfaction >= 70:
            appreciation = "Moyenne"
        else:
            appreciation = "A améliorer"
        
        print(f"Satisfaction : {satisfaction}")    
        print(f"Appréciation : {appreciation}")
        print("-"*50)