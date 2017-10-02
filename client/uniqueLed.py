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

NUMBER_OF_LED = 972

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, int(PORT)))

# Connect to server and send data
buffer = b''
for i in range(NUMBER_OF_LED - 1):
    buffer += 0x000000.to_bytes(3, "big")
buffer += 0xFF0000.to_bytes(3, "big")
sock.sendall(buffer)     # 'big' means MSB first

