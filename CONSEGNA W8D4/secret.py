from stegano import lsb

message = lsb.reveal("./pippo-secret.png")
print(message)