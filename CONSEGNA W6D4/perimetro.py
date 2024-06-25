import math

scelta = 0
while(scelta == 0):
    scelta = int(input("Scegli la figura geometrica: \n1- Quadrato\n2- Rettangolo\n3- Cerchio\n"))
    if (scelta == 1):
        lato = int(input("\nScegli la misura del lato: "))
        perimetro = lato * 4
        print(f"\nIl perimetro del quadrato è : {perimetro}\n")
    elif (scelta == 2):
        base = int(input("\nScegli la misura della base: \n"))
        altezza = int(input("\nScegli la misura dell'altezza\n"))
        perimetro = 2 * (base + altezza)
        print(f"\nIl perimentro del rettangolo è: {perimetro}\n")
    elif (scelta == 3):
        raggio = int(input("\nInserisci la misura del raggio\n"))
        perimetro = 2 * math.pi * raggio
        print(f"\nLa circonferenza del cerchio è: {perimetro}\n")
    else:
        print("\nScelta non valida, riprova!\n")
