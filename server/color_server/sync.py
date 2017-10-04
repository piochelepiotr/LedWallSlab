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
    def __init__(self, port, sync_queue, server):
        Thread.__init__(self)

        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket
        self.port = port
        self.sync_queue = sync_queue
        self.server = server

    # Server listening for sync top
    def run(self):
        logging.info("Lancement du Thread d'écoute de synchronisation...")
        # Start connection
        self.sock.bind(("", self.port))                                        # Listen on port from everywhere
        last = 0
        while True:
            frame_to_show, emmiter = self.sock.recvfrom(1)
            frame_to_show = int.from_bytes(frame_to_show, byteorder='big')
            if 0 <= frame_to_show <= 25:     # while frame_to_show comes from UDP transmission, errors are possible
                self.sync_queue.put(frame_to_show)
            elif frame_to_show == 118 and last == 118:  # 118 = 'v' --> show version
                self.server.show_version()
            elif frame_to_show == 110 and last == 110:  # 110 = 'n' --> show slab number
                self.server.show_slab_number()
            elif frame_to_show == 115 and last == 115:  # 115 = 's' --> restart server
                self.server.restart_server()
            elif frame_to_show == 114 and last == 114:  # 114 = 'r' --> reboot slab
                self.server.reboot()
            elif frame_to_show == 108 and last == 108:  # 108 = 'l' --> return live
                self.server.live()
            last = frame_to_show
