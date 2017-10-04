#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:04:13 2016

@author: thibaud
"""

import logging
from color_server.translator import Decoder
from color_server.gamma import Gamma
from color_server.tcp_receiver import TCPserver
from color_server.spi_writer import SPIwriter
from color_server.sync import UDPsync
import queue

class ColorServer():
    def __init__(self, port, sync_port, SPIspeed):
        gamma_coefs = [[1.12, 1.12, 1.12]]
        self.port = port
        self.sync_port = sync_port
        self.frame_length = len(gamma_coefs) * 324 * 3  # Length of receiving frames
        # New gamma matrix
        self.gamma_matrix = Gamma.gamma_matrix(gamma_coefs)

        self.receive_queue = queue.Queue()  # Receive FIFO
        self.emit_ring_buffer = [bytearray([0, 0, 0, 0])] * 26; # Emit ring buffer
        self.sync_queue = queue.Queue()  # Top synchro FIFO

        # New TCP server
        self.tcp_server = TCPserver(self.port, self.frame_length, self.receive_queue)
        # New SPI writer
        self.spi_writer = SPIwriter(SPIspeed, self.emit_ring_buffer, self.sync_queue)
        # Create a translator (decode / encode)
        self.translator = Decoder(self.gamma_matrix, self.receive_queue, self.emit_ring_buffer)
        # Create the top synchro receiver
        self.sync = UDPsync(self.sync_port, self.sync_queue)

    def refresh(self, config):
        logging.info("Mise à jour de la configuration")
        logging.info(config)
        self.tcp_server.reset_connection()

    # Server listening for LED data
    def start_server(self):
        logging.info("Lancement du ColorServer...")
        self.tcp_server.start()
        self.spi_writer.start()
        self.translator.start()
        self.sync.start()

    def join_server(self):
        self.tcp_server.join()
        self.translator.join()
        self.spi_writer.join()
        self.sync.join()

    def stop_server(self):
        self.tcp_server._stop()
        self.translator._stop()
        self.spi_writer._stop()
        self.sync._stop()

    def update_config(self, config):
        self.tcp_server.reset_connection()

