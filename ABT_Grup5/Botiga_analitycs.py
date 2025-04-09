import csv

def facturacio():
    Factuacio_senseIVA = 0
    Factuacio_ambIVA = 0

    arxiu_csv = "dades_botiga.csv"
    with open(arxiu_csv, newline='', encoding='utf-8') as arxiu:
        lector_csv = csv.DictReader(arxiu)
        
        for i in lector_csv:
            quantitat_venuda = int(i['Quantitat_Venuda'])
            preu = float(i['Preu_Unitari'])
            IVA = float(i['IVA'])

            preu_amb_IVA = preu * (1 + IVA / 100)
            Factuacio_senseIVA += quantitat_venuda * preu
            Factuacio_ambIVA += quantitat_venuda * preu_amb_IVA

    print(f"La facturació sense IVA és: {Factuacio_senseIVA:.2f}€")
    print(f"La facturació amb IVA és: {Factuacio_ambIVA:.2f}€")

def mostrar():
    arxiu_csv = "dades_botiga.csv"
    dades = []
    with open(arxiu_csv, newline='', encoding='utf-8') as arxiu:
        lector_csv = csv.DictReader(arxiu)
        for i in lector_csv:
            print(i["Producte"], i["Estoc_Disponible"])
    
        for i in range(1, len(dades)):
            for j in range(len(dades[0])):
                print(dades[0][j] + ": " + dades[i][j])
            print("")


def menu():
    while True:
        print("\n ___________________________________________________________________")
        print("|----------------Informacion del Mercado de W Tech------------------|")
        print("|___________________________________________________________________|")
        print("|------|1. Mostrar facturacio mensual (amb i sense IVA)--------|----|")
        print("|------|2. Mostrar estock disponible---------------------------|----|")
        print("|------|3. Mostrar els 3 primers products amb mes facturacio---|----|")
        print("|------|4. Sortir----------------------------------------------|----|")

        opcio = int(input("tria una opció de 1 al 4: "))
        if opcio == 1: facturacio()
        elif opcio == 2: mostrar()
        elif opcio == 3: print
        elif opcio == 4: break
        else: print("\nOpció no vàlida. Torna-ho a intentar.\n")

menu()
