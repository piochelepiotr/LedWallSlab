#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:22:21 2016

@author: thibaud
"""

import socket
import time

HOST, PORT = "137.194.67.238", 9999
#HOST, PORT = "localhost", 9999

NUMBER_OF_LED = 324

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, int(PORT)))

start = time.time()
npic = 0

def nextpic():
    global npic
    npic += 1
    next = start + 1/12.0 * npic
    print(next)
    time.sleep(next - time.time())

while True:
    buffer = b''
    for i in range(11):
        for i in range(NUMBER_OF_LED):
            buffer = buffer + 0xFF0000.to_bytes(3, 'big')  # 'big' means MSB first
        nextpic()
        sock.sendall(buffer)
    buffer = b''
    for i in range(NUMBER_OF_LED):
        buffer = buffer + 0x00FF00.to_bytes(3, 'big')        # 'big' means MSB first
    nextpic()
    sock.sendall(buffer)
