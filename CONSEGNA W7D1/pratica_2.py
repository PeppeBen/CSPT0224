import random
import string

def gen_password(tipo = semplice):
    if tipo == semplice:
        caratteri = string.ascii_letters + string.digits
        lunghezza = 8

    elif tipo == complessa:
        caratteri = string.printable.strip 
        lunghezza = 20
    else:
        print("Esco")
    password