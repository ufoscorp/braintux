#!/usr/bin/env python3

# Default imports
import os, sys, subprocess
from db import Database
db = Database()
modules = ["whatsapp", "youtube"]
views = ["whatsapp", "terminal"]

def textToView(content):

    subprocess.Popen("echo 'sendtext\n{}' > {}/chat.tmp".format(content, os.getcwd()), shell=True)

def fileToView(content):

    subprocess.Popen("echo 'sendfile\n{}' > {}/chat.tmp".format(content, os.getcwd()), shell=True)

try:


    # management of module instances
    if sys.argv[1] == "start":
        # Start a module
        if sys.argv[2] == "whatsapp":

            if db.isUp("whatsapp") == False:

                p = subprocess.Popen("python3 {}/views/whatsapp.py start '{}' '{}'".format(os.getcwd(), sys.argv[3], sys.argv[4]), shell=True)
                db.turnOn("whatsapp", p.pid)
                textToView("Running Whatsapp Web, don´t forget to scan the QR Code! ")
            
            else:

                textToView("Whatsapp already running.")
        
        if sys.argv[2] == "terminal":

            if db.isUp("terminal") == False:

                p = subprocess.Popen("python3 {}/views/terminal.py start".format(os.getcwd()), shell=True)
                db.turnOn("terminal", p.pid)
                textToView("Terminal turning on.")
            
            else:

                textToView("Terminal already running.")

    if sys.argv[1] == "restart":
        
        if sys.argv[2] == "whatsapp":

            if db.isUp("whatsapp") == False:

                p = subprocess.Popen("python3 {}/views/whatsapp.py start '{}' '{}'".format(os.getcwd(), sys.argv[3], sys.argv[4]), shell=True)
                db.turnOn("whatsapp", p.pid)
                textToView("Running Whatsapp Web, don´t forget to scan the QR Code! ")
            
            else:

                textToView("Already running.")

    if sys.argv[1] == "kill" or sys.argv=="stop":
        #Stop a module
        module = sys.argv[2]
        if module in modules:
            PID = db.getPID(module)
            if PID != False:
                subprocess.Popen("kill "+PID)
                db.turnOff(module)
            else:
                textToView("Process aren't in our base.")

    if sys.argv[1] == "modules":
        processes = db.listProcesses();
        stringOfProcesses = 'Enabled Modules: \n'
        for process in processes:
            stringOfProcesses += process + '\n'
        textToView(stringOfProcesses)


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
        textToView(message)
    
    if sys.argv[1] == "sendfile":
        file = sys.argv[2]
        fileToView(file)



        
        
except IndexError:

    with open(os.getcwd()+"/help.txt", "r") as help:
        message = help.read()
        for view in views:
            textToView(message)
