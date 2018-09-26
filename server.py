# Save as server.py 
# Message Receiver
import os
from socket import *
host = ""
port = 13213
buf = 1000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
    stuff = UDPSock.recvfrom(buf)
    (data,addr)=stuff
    print (data.decode("utf-8"))
    if data == "exit":
        break
UDPSock.close()
os._exit(0)

