import random
import string

def gen_password(type = "semplice"):
    if type == "semplice":
        caratteri = string.ascii_letters + string.digits
        lunghezza = 8
    elif type == "complessa":
        caratteri = string.ascii_letters + string.digits + string.punctuation 
        lunghezza = 20
    else:
        raise ValueError("Il tipo deve essere: 'semplice' o 'complessa'\n")
    
    password = ''.join(random.choice(caratteri) for i in range(lunghezza))
    return password

password_semplice = gen_password("semplice")
password_complessa = gen_password("complessa")
print(f"Questa è una password semplice: {password_semplice}")
print(f"Questa è una password complessa: {password_complessa}")