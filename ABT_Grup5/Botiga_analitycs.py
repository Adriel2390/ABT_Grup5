import csv

#Funcion de lectura del archivo CSV
def llegir_csv(arxiu_csv):
    dades = []
    with open(arxiu_csv, newline='', encoding='utf-8') as arxiu:
        lector_csv = csv.DictReader(arxiu)
        for l in lector_csv:
            dades.append(l)
    return dades
#La funcion "llegir_csv" lo hizo Iker junto con Jordi



#Funcion de calcular la facturacion con y sin IVA
def facturacio():
    Factuacio_senseIVA = 0  
    Factuacio_ambIVA = 0

    arxiu_csv = "dades_botiga.csv"
    CSV = llegir_csv(arxiu_csv)

    for i in CSV:
        quantitat_venuda = int(i['Quantitat_Venuda'])
        preu = float(i['Preu_Unitari'])
        IVA = float(i['IVA'])

        preu_amb_IVA = preu * (1 + IVA / 100)

        Factuacio_senseIVA += quantitat_venuda * preu  
        Factuacio_ambIVA += quantitat_venuda * preu_amb_IVA

    print(f"|La facturació sense IVA és: {Factuacio_senseIVA:.2f}€|")
    print("|--------------------------------------|")
    print(f"|La facturació amb IVA és: {Factuacio_ambIVA:.2f}€--|")
#La funcion "facturacio" lo hizo Jordi junto con Adriel



#Funcion para mosrtar la seccion de "Producte" y "Estoc_Disponible", esto ayuda a la funcion "mostrar_3_productes"
def mostrar():
    arxiu_csv = "dades_botiga.csv"
    CSV = llegir_csv(arxiu_csv)

    for i in CSV:
        print(f"Producte: {i['Producte']}")
        print("|----------------------------------------------|")
        print(f"|Estoc_Disponible: {i['Estoc_Disponible']}|")
        print("|______________________________________________|")
#La funcion "Mostrar" lo hizo Iker



#Funcion que muestra los 3 productos mas vendidos
def mostrar_3_productes():
    arxiu_csv = "dades_botiga.csv"
    dades = llegir_csv(arxiu_csv)
    dades_facturacio = []
    
    for i in dades:
        producte = i["Producte"]
        quantitat_venuda = int(i["Quantitat_Venuda"])
        preu_unitari = float(i["Preu_Unitari"])
        facturacio = quantitat_venuda * preu_unitari
    
        dades_facturacio.append({"Producte": producte, "Facturacio": facturacio})
    
    print("Els 3 productes amb més facturació:")
    for i in range(min(3, len(dades_facturacio))):
        print("_____________________________________________________________________")
        print(f"|Producte: {dades_facturacio[i]['Producte']}, Facturació: {dades_facturacio[i]['Facturacio']:.2f}€")
        print("|____________________________________________________________________|")
#La funcion "mostrar_3_productes" lo hizo Adriel



#Funcion del Menu
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
        if opcio == 1: 
            facturacio()
        elif opcio == 2: 
            mostrar()
        elif opcio == 3: 
            mostrar_3_productes()
        elif opcio == 4: 
            print("Adiós") 
            break
        else: print("\nOpció no vàlida. Torna-ho a intentar")

menu()
#La funcion "Menu" lo hizo Alejandro
