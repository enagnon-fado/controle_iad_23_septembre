# Exercice 26 : Rapport de synthèse

import csv

path = "donnees.csv"

with open(path, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    
    chiffre_affaires_total = 0
    depenses_total = 0
    clients_total = 0
    nouveaux_clients_total = 0
    benefice_total = 0
    
    chiffre_affaires_par_mois = {}
    depenses_par_mois = {}
    chiffre_affaires_par_service = {}
    clients_par_region = {}
    
    mois = set()
    
    for ligne in reader:
        
        mois_actuel = ligne["mois"]
        annee = ligne["annee"]
        service = ligne["service"]
        region = ligne["region"]
        
        chiffre_affaires = float(ligne["chiffre_affaires"])
        depenses = float(ligne["depenses"])
        clients = int(ligne["clients"])
        nouveaux_clients = int(ligne["nouveaux_clients"])
        
        chiffre_affaires_total += chiffre_affaires
        depenses_total += depenses
        clients_total += clients
        nouveaux_clients_total += nouveaux_clients
        
        mois.add(mois_actuel)
        
        if mois_actuel not in chiffre_affaires_par_mois:
            chiffre_affaires_par_mois[mois_actuel] = {
                "annee": annee,
                "total": 0
            }
            
        chiffre_affaires_par_mois[mois_actuel]["total"] += chiffre_affaires
        
        if service not in chiffre_affaires_par_service:
            chiffre_affaires_par_service[service] = 0
            
        chiffre_affaires_par_service[service] += chiffre_affaires
        
        if region not in clients_par_region:
            clients_par_region[region] = 0
            
        clients_par_region[region] += clients
        
benefice_total = chiffre_affaires_total - depenses_total

chiffre_affaires_moyen = chiffre_affaires_total/len(mois)

meilleur_mois = max(
    chiffre_affaires_par_mois,
    key=lambda mois : chiffre_affaires_par_mois[mois]["total"]
)

chiffre_affaires_meilleur_mois = chiffre_affaires_par_mois[meilleur_mois]["total"]
annee_meilleur_mois = chiffre_affaires_par_mois[meilleur_mois]["annee"]

meilleur_service = max(
    chiffre_affaires_par_service,
    key=chiffre_affaires_par_service.get
)

chiffre_affaires_meilleur_service = chiffre_affaires_par_service[meilleur_service]

meilleur_region = max(
    clients_par_region,
    key=clients_par_region.get
)
    
clients_meilleur_region = clients_par_region[meilleur_region]       

chiffre_affaires_janvier = chiffre_affaires_par_mois["Janvier"]["total"]
chiffre_affaires_decembre = chiffre_affaires_par_mois["Décembre"]["total"]

evolution = (
    (chiffre_affaires_decembre - chiffre_affaires_janvier)
    /chiffre_affaires_janvier
)*100

print("="*60)
print("             RAPPORT RECAPITULATIF ")
print("="*60)
print("Période analysée : Janvier à décembre 2025")
print(f"Chiffre d'affaires total : {chiffre_affaires_total}")
print(f"Chiffre d'affaires moyen : {chiffre_affaires_moyen}")
print(f"Dépenses totales : {depenses_total}")
print(f"Bénéfice total : {benefice_total}")
print(f"Nombre total de clients : {clients_total}")
print(f"Nombre total de nouveaux clients : {nouveaux_clients_total}")

print("-"*60)

print(
    f"Meilleur mois en chiffre d'affaires : "
    f"{meilleur_mois} 2025 : "
    f"{chiffre_affaires_meilleur_mois}"
)

print(
    f"Meilleur service en chiffre d'affaires : "
    f"{meilleur_service} "
    f"{chiffre_affaires_meilleur_service}"
)

print(
    f"Meilleure région en nombre de clients : "
    f"{meilleur_region} "
    f"{clients_meilleur_region}"
)

print(
    f"Evolution du chiffre d'affaires entre janvier et décembre : "
    f"{evolution:.2f}%"
)

print("="*60)