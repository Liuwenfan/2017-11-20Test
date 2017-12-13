#!/usr/bin/env python

from socket import *
from time import ctime

HOST = 'localhost'
PORT = 60000
BUFFSIZE = 1024
ADDR = (HOST, PORT)

TcpSerSock = socket(AF_INET, SOCK_STREAM)
TcpSerSock.bind(ADDR)
TcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    TcpCliSock, addr = TcpSerSock.accept()
    print('connection from :', addr)

    while True:
        data = TcpCliSock.recv(BUFFSIZE)
        if not data:
            break
        print('[%s] %s' % (ctime(), data))
        TcpCliSock.send("[{}] {}".format(ctime(), data))

    TcpSerSock.close()
