# Qt module - parser

import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.RCVTIMEO = 500
port = 8652
socket.connect("tcp://localhost:{}".format(port))

def parse(args):
    
    socket.send_json(["ping"])
    try:
        socket.recv_json()[0]
        print("Qt don't have options.")
    except:
        print("Qt: Off.")
        os._exit(0)