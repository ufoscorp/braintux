# Braintux Core

import os
import zmq
import sys
import subprocess

from modules.terminal.parser import parse as terminalParser
from modules.qt.parser import parse as qtParser

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.RCVTIMEO = 500
socket.connect("tcp://127.0.0.1:8660")

if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    root = "/opt/braintux-master"
elif sys.platform == "nt":
    root = r"%ProgramFiles%/braintux-master"

ports = {"terminal":8650, "whatsapp":8651, "qt":8652}
modules = ["whatsapp", "terminal", "youtube", "qt"]
notInstantiableModules = ["youtube"]
args = sys.argv

with open("{}/help.txt".format(root), "r") as help:
    help = help.read()

# Entering a command
if len(args) > 1:

    command = args[1]
    module = command

    if command == "start":
        # Start a module
        if len(args) > 2:
            module = args[2]
            subprocess.Popen('python3 {}/modules/{}/start.py &'.format(root, module), shell=True)

        else:
            print("Usage: braintux start <module>")

    elif command == "stop":
        # Stop a module
        if len(args) > 2:
            module = args[2]
            port = ports[module]
            
            socket = context.socket(zmq.REQ)
            socket.RCVTIMEO = 500
            socket.connect("tcp://localhost:{}".format(port))
            socket.send_json(["stop"])
            try:
                socket.recv_json()[0]
                print("{}: stopped.".format(module))
            except:
                print("{}: Off.".format(module))
                
            os._exit(0)

        else:
            print("Usage: braintux stop <module>")
    
    elif command == "ping":
        # Ping a module
        if len(args) > 2:
            module = args[2]
            port = ports[module]

            socket = context.socket(zmq.REQ)
            socket.RCVTIMEO = 500
            socket.connect("tcp://localhost:{}".format(port))
            socket.send_json(["ping"])
            answered = False
            try:
                answer = socket.recv_json()[0]
                answered = True
            except:
                answered = False
            if answered:
                print("On")
            else:
                print("Off")
                os._exit(0)
        else:
            exit("Usage: braintux ping <module>")

    elif command == "modules":
        # Checking which module is enable
        output = ""
        output += "not Instantiable Modules:\n\n"
        for module in notInstantiableModules:
            output += "{}\n".format(module)
        output += "\nInstantiable Modules:\n\n"
        for module, port in ports.items():
            
            socket = context.socket(zmq.REQ)
            socket.RCVTIMEO = 500
            socket.connect("tcp://localhost:{}".format(port))
            socket.send_json(["ping"])
            try:
                socket.recv_json()[0]
                output += "{}: On.\n".format(module)
            except:
                output += "{}: Off.\n".format(module)
            
        print(output)
        os._exit(0)
    
    elif command == "text":

        if len(args) > 2:
            message = args[2]

            for module, port in ports.items():
            
                socket = context.socket(zmq.REQ)
                socket.RCVTIMEO = 500
                socket.connect("tcp://localhost:{}".format(port))
                socket.send_json([message])
                try:
                    socket.recv_json()[0]
                    print("{}: sent.".format(module))
                except:
                    print("{}: Off.".format(module))
            
            os._exit(0)
        else:
            print("Usage: braintux text")
    
    ### HERE WE HAVE MODULE ACCESS

    elif module == "terminal":
        # Access to terminal module
        terminalParser(args)
    elif module == "qt":
        # Access to qt module
        qtParser(args)
    else:
        print(help)
else:
    print(help)