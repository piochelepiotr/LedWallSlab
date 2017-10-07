#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:22:21 2016

@author: thibaud
"""

import socket

HOST, PORT = "137.194.67.238", 9999
#HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto("ll", ("192.168.1.255", 9999))
