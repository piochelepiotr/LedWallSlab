#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 5 10:01:13 2017

@author: thibaud
"""

from PIL import Image, ImageDraw


class Text():
    def __init__(self, slab_number, version, sversion):
        self.slab_number = slab_number
        self.version = version
        self.sversion = sversion

    @staticmethod
    def __img_to_frame(img):
        frame = bytearray([0, 0, 0, 0])  # Create an empty bytearray we'll fill
        for i in range(18):
            for j in range(18):
                frame.append(255)  # First byte sent to a LED always OxFF
                for k in range(3):  # RGB loop
                    frame.append(img.getpixel((i, j))[k])
        # To make the new frame display, we send the correct amount of 0xFF (push cascading data on SPI bus)
        for i in range(21):  # Push to update, cf translator.py
            frame.append(255)
        return frame

    def get_version_frame(self):
        img = Image.new('RGB', (18, 18))
        d = ImageDraw.Draw(img)
        d.text((0, 3), str(self.version), fill=(255, 0, 0))
        d.text((7, 3), str(self.sversion), fill=(0, 0, 255))
        return Text.__img_to_frame(img)

    def get_slab_number_frame(self):
        img = Image.new('RGB', (18, 18))
        d = ImageDraw.Draw(img)
        d.text((4, 3), str(self.slab_number), fill=(0, 255, 0))
        return Text.__img_to_frame(img)


