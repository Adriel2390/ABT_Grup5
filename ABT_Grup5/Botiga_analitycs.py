import csv

dades = ""
add = []

with open('dades_botiga.csv', newline="") as a:
    data = csv.reader(a, delimiter=",")
    dades = list(data)

#print(dades)

def orden(dades):
    for i in range(1, len(dades)):
        for j in range(len(dades[i])):
            print(dades[0][j] + ": " + dades[i][j])
        print("")

#orden(dades)

def add(dades):
    for i in range(1, len(dades)):
        sum = 0
        med = 0
        print(dades[0][0] + ": " + dades[i][0])

        for j in range(1, len(dades[i])):
            print(dades[0][j] + ": " + dades[i][j])
        print("")

#add(dades)




def menu():
    while True:
        print(" ___________________________________________________________________")
        print("|----------------Informacion del Mercado de W Tech------------------|")
        print("|___________________________________________________________________|")
        print("|------|1. Mostrar facturacio mensual (amb i sense IVA)--------|----|")
        print("|------|2. Mostrar estock disponible---------------------------|----|")
        print("|------|3. Mostrar els 3 primers products amb mes facturacio---|----|")
        print("|------|4. Sortir----------------------------------------------|----|")

        opcio = int(input("tria una opció de 1 al 4: "))
        if opcio == 1: print
        elif opcio == 2: print
        elif opcio == 3: print
        elif opcio == 4: break

#menu()
