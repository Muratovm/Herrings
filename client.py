#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

index = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(bytes("ping", 'utf-8'))
        print('Sent', "ping")
        data = s.recv(1024)
        print('Received', data.decode("utf-8"))
        index += 1
    
