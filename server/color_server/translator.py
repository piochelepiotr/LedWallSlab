#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:01:13 2016

@author: thibaud
"""

import logging
from threading import Thread


class Decoder(Thread):
    NUMBER_OF_LED_PER_SLAB = 324

    def __init__(self, gamma_matrix, receive_queue, emit_ring_buffer):
        """
        This function initialize data counters (LED, Slab, RGB color) and save given gamma_matrix
        :param gamma_matrix: [[gammaR, gammaG, gammaB], ..., [gammaR, gammaG, gammaB]]
                             This gamma matrix is used to correct LED illumination
        """

        Thread.__init__(self)

        self.number_of_slabs = len(gamma_matrix)
        self.gamma_matrix = gamma_matrix
        self.emit_ring_buffer = emit_ring_buffer
        self.receive_queue = receive_queue

        # Stop flag
        self.terminated = False

    def run(self):
        logging.info("Thread de conversion des données opérationnel")
        while not self.terminated:
            recv_buffer = self.receive_queue.get()
            frame_number, recv_buffer = recv_buffer[0], recv_buffer[1:] # Extract frame number
            emit_buffer = bytearray([0, 0, 0, 0])

            idx = 0
            for i in range(self.number_of_slabs):
                for j in range(self.NUMBER_OF_LED_PER_SLAB):
                    emit_buffer.append(255)
                    for k in range(3):
                        emit_buffer.append(self.gamma_matrix[i,k,recv_buffer[idx]])
                        idx += 1
            for i in range(Decoder.NUMBER_OF_LED_PER_SLAB * self.number_of_slabs // 16 + 1):
                emit_buffer.append(255)
            self.emit_ring_buffer[frame_number] = emit_buffer

    def stop(self):
        self.terminated = True
