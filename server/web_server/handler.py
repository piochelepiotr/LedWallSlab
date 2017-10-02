#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:18:59 2016

@author: jarassevincent
"""

from http.server import BaseHTTPRequestHandler
from web_server.patch import Patch
import cgi
from bs4 import BeautifulSoup
import json
import os

class WebHandler(BaseHTTPRequestHandler):

    def nullFunction(self):
        pass

    updateFunction = nullFunction
    showNumbersFunction = nullFunction

    def do_GET(self):
        self.send_response(200)
        page = open("web_server/Public/" + self.path[1:], 'r')
        if self.path.split('.', 1)[1] == "html":
            if self.path.split('.', 1)[0] == "/acceuil":
                returned_page = self.parse_acceuil()
            else:
                returned_page = page.read()
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            self.wfile.write(bytes(returned_page, "utf-8"))
        if self.path.split('.', 1)[1] == "css":
            self.send_header("Content-type", "text/css; charset=UTF-8")
            self.end_headers()
            self.wfile.write(bytes(page.read(), "utf-8"))
        if self.path.split('.', 1)[1] == "js":
            self.send_header("Content-type", "application/javascript; charset=UTF-8")
            self.end_headers()
            self.wfile.write(bytes(page.read(), "utf-8"))
        if self.path.split('.', 1)[1] == "txt":
            self.send_header("Content-type", "text/txt; charset=UTF-8")
            self.end_headers()
            self.wfile.write(bytes(page.read(), "utf-8"))

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        self.send_response(201)
        self.send_header("Content-type","text/html; charset=UTF-8")
        self.end_headers()
        self.wfile.write(bytes(open("web_server/Public/" + self.path[1:], 'r').read(), "utf-8"))
        meta = {}
        meta["total"] = form["quantite"]
        meta["width"] = form["width"]
        meta["height"] = form["height"]
        config = []
        for i in range(int(meta["total"].value)):
            config.append({})
            config[i]["x"] = form["slabx"+str(i)]
            config[i]["y"] = form["slaby"+str(i)]

        data = {}
        data["meta"] = meta
        data["config"] = config
        if os.path.exists(os.getcwd()+"web_server/configs/current.txt"):
            os.remove(os.getcwd()+"web_server/configs/current.txt")
        with open(os.getcwd()+"web_server/configs/current.txt",'w') as f:
            json.dump(data,f)

        #self.patch = Patch(form[form.keys()[0]].value, form[form.keys()[1]].value, form[form.keys()[2]].value)
        #WebHandler.updateFunction(self.patch)

    def parse_acceuil(self):
        with open("web_server/Public/acceuil.html", "r") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc)

        for pre in soup.find_all('div'):
            try:
                if "configs" in pre.get("id"):
                    pre.string = "Toto"
            except:
                print("Parse error")
        return soup.prettify()
