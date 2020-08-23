#!/usr/bin/env python3

import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

print("Started Server File")
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print(s)
        while True:
            s.listen()
            conn, addr = s.accept()
            print(conn)
            print(addr)
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(bytes("pong", 'utf-8'))
except:
    print("An exception occurred")
