#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 09:10:13 2016

@author: thibaud
"""

import log
import logging
from color_server.server import ColorServer
import sys
import os
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'django_server/'))
#os.environ["DJANGO_SETTINGS_MODULE"] = "django_server.ledwall.settings"
#import django
#django.setup()
#import config.views as view
#from external_run import DjangoThread
import time


"""
This script import the ledwall server
It receive video frames (RGB) from the client
Frames are gamma corrected and sent to LEDs
"""


def main():
    # Start logging system
    log.config_logger()

    # Start color server
    logging.info("Création du ColorServer")
    # /!\ Vitesse SPI gêne les autres Threads, pourquoi ?
    color_server = ColorServer(9999, 8888, 10000000) # Data TCP on port 9999 and sync on port 8888 UDP
                                                     # SPI @ 10Mbps
    color_server.start_server()

    try:
        color_server.join_server()
    except KeyboardInterrupt:
        print('########################### Interrupted #############################')
        #django_server.stop_server()
        sys.exit(0)



# If main program, start main
if __name__ == "__main__":
    main()

