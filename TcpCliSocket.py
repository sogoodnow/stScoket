#!usr/bin/env python
from socket import *

HOST = "localhost"
PORT = 25678
BUFSIZE = 1024
ADDR = (HOST, PORT)

cliSersocket = socket(AF_INET, SOCK_STREAM)
cliSersocket.connect(ADDR)

while True:
    data = raw_input("hello there...:")
    if not data:
        break
    cliSersocket.send(data)
    data = cliSersocket.recv(BUFSIZE)
    if not data:
        break
    print data
cliSersocket.close()

