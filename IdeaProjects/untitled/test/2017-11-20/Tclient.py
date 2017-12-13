#!//usr/bin/env python

from socket import *

HOST='localhost'
PORT=60000
BUFFSIZE=1024
ADDR=(HOST,PORT)

TcpClient=socket(AF_INET,SOCK_STREAM)
TcpClient.connect(ADDR)

while True:
    data=input('> ')
    if not data:
        break
    TcpClient.send(data.encode("utf8"))
    data=TcpClient.recv(BUFFSIZE)
    if not data:
        break
    print(data)

TcpClient.close()
