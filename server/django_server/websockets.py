# -*- coding: utf-8 -*-
import argparse
import random
import os

import cherrypy
import logging
from ws4py.websocket import WebSocket

class ConsoleWebSocketHandler(WebSocket):
    def opened(self):
        #cherrypy.engine.publish('websocket-broadcast', TextMessage("Nouveau client WS \n"))
        return

    def received_message(self, m):
        text = m.data.decode('utf-8')
        if text == "connect":
            self.send("connected")
            with open('log/current.log') as f:
                content = f.readlines()
            for line in content:
                self.send(line)
            logging.info("Connexion d'une console distante")
        else:
            logging.info("Message d'une console distante : " + text)


    def closed(self, code, reason=None):
        #cherrypy.engine.publish('websocket-broadcast', TextMessage("Suppression d'un client WS \n"))
        logging.info("Déconnexion de la console distante")


class WebSocketRoot(object):
    @cherrypy.expose
    def console(self):
        return
