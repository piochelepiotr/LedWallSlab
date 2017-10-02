  #!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:22:21 2016

@author: thibaud
"""

import socket
import time

#HOST, PORT = "137.194.67.238", 9999
HOST, PORT = "localhost", 9999

NUMBER_OF_LED = 324

while True:
    # Create a socket (SOCK_STREAM means a TCP socket)
    print("Tentative de connexion")
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, int(PORT)))
    except ConnectionRefusedError:
        print("Serveur indisponible, tentative de reconnexion dans 2s")
        time.sleep(1)
        continue

    print("Connecté")
    try:
        while True:
                for i in range (NUMBER_OF_LED):
                    # Connect to server and send data
                    for i in range(i):
                        sock.sendall(0x000000.to_bytes(3, 'big'))     # 'big' means MSB first
                    sock.sendall(0xFF0000.to_bytes(3, 'big'))  # 'big' means MSB first
                    for i in range(NUMBER_OF_LED-2-i):
                        sock.sendall(0x000000.to_bytes(3, 'big'))  # 'big' means MSB first
                    time.sleep(0.02)
    except socket.error:
        print("Déconnecté par le serveur")


