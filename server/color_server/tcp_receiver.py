#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:04:13 2016

@author: thibaud
"""

import logging
import socket
from threading import Thread


class TCPserver(Thread):
    def __init__(self, port, frame_length, queue):
        """
        This constructor init TCP socket
        :param port: default 9999
        :param frame_length: default 1 slab * 324 LEDs * 3 colors = 972 bytes long
        :param queue: queue to put data in
        """
        Thread.__init__(self)

        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # No port hold
        self.port = port
        self.queue = queue
        self.frame_length = frame_length + 1 # +1 byte for frame number between 0 and 25 (used for synchro) at the beginging
        self.s = None
        self.f = None
        self.buffer = b'' # Buffer's type is bytes

    def run(self):
        """
        Thread function
        :return:
        """
        logging.info("Lancement du Thread d'écoute TCP...")
        # Start connection
        self.sock.bind(("", self.port))                                        # Listen on port 9999 from everywhere
        self.sock.listen(1)                                                    # 1 client max

        self.__connexion()

        while True:
            while len(self.buffer) < self.frame_length:
                if self.s == None:
                    self.__connexion()
                try:
                    b = self.s.recv(2048)
                except socket.error:
                    continue
                # In case of disconnection
                if len(b) == 0:
                    logging.info("Le client s'est déconnecté")
                    self.s.close()
                    self.s = None
                self.buffer += b

            # Write in the reception FIFO only 1 frame
            self.queue.put(self.buffer[:self.frame_length])
            self.buffer = self.buffer[self.frame_length:]

    def reset_connection(self):
        """
        Function called to reset TCP socket
        :return:
        """
        if self.s is None:
            return
        logging.info("Réinitialisation de la connexion TCP")
        self.s.close()
        self.s = None
        self.__connexion();

    def __connexion(self):
        """
        Function called to start listening
        :return:
        """
        logging.info("En attente de connexion TCP sur le port " + str(self.port))
        # Wait for connection
        self.s, self.f = self.sock.accept()
        logging.info("Client TCP connecté")
        self.buffer = b''  # Buffer's type is bytes

