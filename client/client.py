#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:22:21 2016

@author: thibaud
"""

import socket
import struct

HOST, PORT = "137.194.67.238", 9999
#HOST, PORT = "localhost", 9999

NUMBER_OF_LED = 324

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, int(PORT)))

while True:
    data = int(input("> "), 16)
    # Connect to server and send data
    for i in range(NUMBER_OF_LED):
        sock.sendall((data).to_bytes(3, 'big'))     # 'big' means MSB first
