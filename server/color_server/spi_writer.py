#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:04:13 2016

@author: thibaud
"""

import spidev
import logging
from threading import Thread
import time


class SPIwriter(Thread):
    def __init__(self, speed, emit_ring_buffer, sync_queue):
        Thread.__init__(self)

        # Declaration of SPI interface
        self.spi = spidev.SpiDev()

        # Saving queue pointer
        self.emit_ring_buffer = emit_ring_buffer
        self.sync_queue = sync_queue

        # Open SPI port 0, chip 0 @ speed
        self.spi.open(1, 0)
        self.spi.max_speed_hz = speed

        # Stop flag
        self.terminated = False

    # Server listening for LED data
    def run(self):
        logging.info("Thread de communication SPI opérationnel")
        # The thread write available data on the SPI bus
        while not self.terminated:
            frame_to_show = self.sync_queue.get()   # wait until frame number to show UDP received
            buffer = self.emit_ring_buffer[frame_to_show]
            # spi.xfer only allow 4096 length frames
            while len(buffer) > 4096:
                self.spi.xfer(list(buffer[:4096]))
                buffer = buffer[4096:]
            # Write on the bus
            self.spi.xfer(list(buffer))

    def stop(self):
        self.terminated = True
