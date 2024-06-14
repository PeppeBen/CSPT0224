import math

scelta = 0
while True:
    scelta = int(input("Scegli la figura geometrica:\n1- Quadrato\n2- Rettangolo\n3- Cerchio\n"))
    if (scelta == 1):
        lato = int(input("\nScegli la misura del lato: "))
        perimetro = lato * 4
        area = lato**2
        print(f"\nIl perimetro del quadrato è: {perimetro}\n")
        print(f"\nL'area del quadrato è: {area}\n")
    elif (scelta == 2):
        base = area
        altezza = area / 2
        perimetro_r = 2 * (base + altezza)
        area_r = base * altezza
        print(f"\nIl perimentro del rettangolo è: {perimetro_r}\n")
        print(f"\nL'area del rettangolo è: {area_r}\n")
    elif (scelta == 3):
        raggio = area_r
        circonferenza = 2 * math.pi * raggio
        area_c = math.pi * raggio**2
        print(f"\nLa circonferenza del cerchio è: {circonferenza}\n")
        print(f"\n L'area del cerchio è: {area_c}\n")
    else:
        print("\nScelta non valida, riprova!\n")