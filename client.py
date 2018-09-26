# Save as client.py 
# Message Sender
import os
from socket import *
host = "192.168.43.101" # set to IP address of target computer
port = 13213
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
print(host)
while True:
    data = input("Enter message to send or type 'exit': ")
    data=data.encode("utf-8")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
UDPSock.close()
os._exit(0)
