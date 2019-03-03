# Terminal module - parser

import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.RCVTIMEO = 500
port = 8650
socket.connect("tcp://localhost:{}".format(port))

def parse(args):
    
    socket.send_json(["ping"])
    try:
        socket.recv_json()[0]
        if len(args) > 2:
            function = args[2]
            if function == "sendtext":
                if len(args) > 3:
                    text = args[3]
                    socket.send_json([text])
                else:
                    print("Usage: braintux terminal sendtext <text>")
            else:
                print("Usage: braintux terminal <function> [OPTIONS]")
        else:
            print("Usage: braintux terminal <function> [OPTIONS]")
    except:
        print("Terminal: Off.")
        os._exit(0)