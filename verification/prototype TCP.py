#!/usr/bin/env python3

import socket

def envoi():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = b"hello world"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    #data = s.recv(BUFFER_SIZE)
    s.close()

    print ("data sent")

def reception():

    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print ('Connection address:', addr)
    while 1:
        conn, addr = s.accept()
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print ("received data:", data.decode())
        conn.send(data)  # echo
        conn.close()

a=input("mode: ")
if a == "help":
    print('entrez "envoi" pour envoyer des données')
    print('entrez "reception" pour envoyer des données')
elif a == "envoi":
    envoi()
else:
    reception()