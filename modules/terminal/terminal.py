# Terminal module

import os
import zmq
import subprocess

executing = True
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:8650")

while executing:
    #  Wait for next request from client
    message = socket.recv_json()[0]
    if message == "ping":
        socket.send_json(["pong"])
    elif message == "stop":
        socket.send_json(["stopped"])
        os._exit(0)
    else:
        print("Braintux: {}".format(message))
        socket.send_json(["sent"])