#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:04:13 2016

@author: thibaud
"""

import logging
import socket
from threading import Thread


class UDPsync(Thread):
    def __init__(self, port, sync_queue):
        Thread.__init__(self)

        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        self.port = port
        self.sync_queue = sync_queue

    # Server listening for sync top
    def run(self):
        logging.info("Lancement du Thread d'écoute de synchronisation...")
        # Start connection
        self.sock.bind(("", self.port))                                        # Listen on port from everywhere
        while True:
            frame_to_show, emmiter = self.sock.recvfrom(1)
            frame_to_show = int.from_bytes(frame_to_show, byteorder='big')
            if 0 <= frame_to_show <= 25:     # while frame_to_show comes from UDP transmission, errors are possible
                self.sync_queue.put(frame_to_show)
