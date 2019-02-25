#!/usr/bin/env python3

# Default imports
import os, sys
from subprocess import Popen
from db import Database
db = Database()
modules = ["whatsapp", "youtube", "terminal"]
views = ["whatsapp", "terminal"]
if sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="darwin":
	installationPath="/opt/braintux"
elif sys.platform=="nt":
	installationPath=r"%ProgramFiles%/braintux"


def textToView(content):

    with open(installationPath+"/chat.tmp", "w", os.O_NONBLOCK) as chat:

        chat.write('sendtext')
        chat.write(content)

        chat.close()

def fileToView(content):

    with open(installationPath+"/chat.tmp", "w", os.O_NONBLOCK) as chat:

        chat.write('sendfile')
        chat.write(content)

        chat.close()

def kill(module):

    PID = db.getPID(module)
    if PID != False:
        os.system("kill "+str(PID))
        os.system("kill "+str(PID+1))
        db.turnOff(module)
    else:
        textToView("{} aren't in our base.".format(module))

def help():

    with open(installationPath+"/help.txt", "r") as help:
        message = help.read()
        textToView(message)

if len(sys.argv) > 1:

    # args to modules
    if sys.argv[1] == "whatsapp":
        # access functions
        if len(sys.argv) > 2:
            if sys.argv[2] == "start":
                if len(sys.argv) == 5:
                    if db.isUp("whatsapp") == False:
                        textToView("Starting Whatsapp. Don´t forget to scan the QR Code!")
                        p = Popen("python3 {}/views/whatsapp.py start '{}' '{}'".format(installationPath, sys.argv[3], sys.argv[4]), shell=True)
                        db.turnOn("whatsapp", p.pid)
                    else:
                        textToView("Whatsapp already running.")
                else:
                    textToView("Usage: braintux whatsapp start <browser> <group name>\n Example: braintux whatsapp start firefox 'my braintux'")
            
            elif sys.argv[2] == "stop" or sys.argv[2] == "kill":
                kill("whatsapp")
                textToView('Stopping whatsapp...')
            else:
                # function don't exist
                textToView("This module don't have this function.")
        else:
            textToView("Usage: braintux whatsapp <function> [OPTIONS]\nfunctions: start, stop")
    
    elif sys.argv[1] == "terminal":
        # access functions
        if len(sys.argv) > 2:
            if sys.argv[2] == "start":
                if db.isUp("terminal") == False:
                    textToView("Starting terminal.")
                    p = Popen("python3 {}/views/terminal.py start".format(installationPath), shell=True)
                    db.turnOn("terminal", p.pid)
                else:
                    textToView("terminal already running.")
            elif sys.argv[2] == "stop" or sys.argv[2] == "kill":
                kill("terminal")
            else:
                # function don't exist
                textToView("This module don't have this function.")
        else:
            textToView("Usage: braintux terminal <function> [OPTIONS]\nfunctions: start, stop")

    elif sys.argv[1] == "youtube":
        # access functions
        if len(sys.argv) > 2:
            if sys.argv[2] == "search":
                if len(sys.argv) == 4:
                    youtube=Popen("python3 {}/modules/youtube.py search '{}'".format(installationPath, sys.argv[3]), shell=True)
                else:
                    textToView("Usage: braintux youtube search <term>")
            elif sys.argv[2] == "download":
                if len(sys.argv) == 5:
                    youtube=Popen("python3 {}/modules/youtube.py download '{}' '{}'".format(installationPath, sys.argv[3], sys.argv[4]), shell=True)
                else:
                    textToView("Usage: braintux youtube download <term> <choice>")
            else:
                # function don't exist
                textToView("This module don't have this function.")
        else:
            textToView("Usage: braintux youtube <function> [OPTIONS]\nfunctions: search, download")



    # modules to view
    elif sys.argv[1] == "sendtext":
        message = sys.argv[2]
        textToView(message)
    
    elif sys.argv[1] == "sendfile":
        file = sys.argv[2]
        fileToView(file)

    # list modules
    elif sys.argv[1] == "modules":
        processes = db.listProcesses();
        stringOfProcesses = 'Enabled Modules: \n'
        for process in processes:
            stringOfProcesses += process + '\n'
        textToView(stringOfProcesses)
    
    else:
        help()
        
else:
    help()
