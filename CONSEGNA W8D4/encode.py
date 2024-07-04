from stegano import lsb

secret = lsb.hide("./pippo.jpeg", "Hey Pippo!")
secret.save("./pippo-secret.png")

