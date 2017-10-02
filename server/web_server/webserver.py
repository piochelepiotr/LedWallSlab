#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:18:59 2016

@author: jarassevincent
"""

from http.server import HTTPServer
from threading import Thread
from web_server.handler import WebHandler

class WebServer(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.webserver = HTTPServer(("", port), WebHandler)

    def run(self):
        try:
            self.webserver.serve_forever()
        finally:
            self.webserver.server_close()

    def changeUpdateFunction(self, newUpdateFunction):
        WebHandler.updateFunction = newUpdateFunction

    def changeShowNumbersFunction(self, newShowNumbersFunction):
        WebHandler.showNumbersFunction = newShowNumbersFunction
