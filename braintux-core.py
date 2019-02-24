#!/usr/bin/env python3

# Default imports
import os, sys, subprocess
from views.terminal import Terminal
from db import Database
terminal = Terminal()
db = Database()
modules = ["whatsapp", "youtube"]
views = ["whatsapp", "terminal"]

def sendToView(content):

    subprocess.Popen("echo {} > {}/chat.tmp".format(content, os.getcwd()), shell=True)

try:


    # management of module instances
    if sys.argv[1] == "start":
        # Start a module
        if sys.argv[2] == "whatsapp":

            if db.isUp("whatsapp") == False:

                p = subprocess.Popen("python3 {}/views/whatsapp.py start '{}' '{}'".format(os.getcwd(), sys.argv[3], sys.argv[4]), shell=True)
                db.turnOn("whatsapp", p.pid)
                sendToView("Running Whatsapp Web, don´t forget to scan the QR Code! ")
            
            else:

                sendToView("Already running.")

    if sys.argv[1] == "restart":
        
        if sys.argv[2] == "whatsapp":

            if db.isUp("whatsapp") == False:

                p = subprocess.Popen("python3 {}/views/whatsapp.py start '{}' '{}'".format(os.getcwd(), sys.argv[3], sys.argv[4]), shell=True)
                db.turnOn("whatsapp", p.pid)
                prinsendToView("Running Whatsapp Web, don´t forget to scan the QR Code! ")
            
            else:

                sendToView("Already running.")

    if sys.argv[1] == "kill" or sys.argv=="stop":
        #Stop a module
        module = sys.argv[2]
        if module in modules:
            PID = db.getPID(module)
            if PID != False:
                subprocess.Popen("kill "+PID)
                db.turnOff(module)
            else:




    # args to modules
    if sys.argv[1] == "youtube":
        # Apenas um argumento pra cada função
        if sys.argv[2] == "search":
            youtube=subprocess.Popen("python3 {}/modules/youtube.py search '{}'".format(os.getcwd(), sys.argv[3]), shell=True)
        if sys.argv[2] == "download":
            youtube=subprocess.Popen("python3 {}/modules/youtube.py download '{}' '{}'".format(os.getcwd(), sys.argv[3], sys.argv[4]), shell=True)



    # modules to view
    if sys.argv[1] == "sendtext":
        message = sys.argv[2]
        sendToView(message)
    
    if sys.argv[1] == "sendfile":
        file = sys.argv[2]
        sendToView(file)



        
        
except IndexError:

    with open(os.getcwd()+"/help.txt", "r") as help:
        message = help.read()
        for view in views:
            subprocess.Popen("python3 {}/views/{}.py sendtext '{}'".format(os.getcwd(), view, message), shell=True)
