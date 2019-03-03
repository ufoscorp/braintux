import sys
from datetime import datetime

import zmq


def handle(message):
    return (message[0]+"?")

port = 8660

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://127.0.0.1:{}'.format(port))

while True:
    message = socket.recv_json()
    print(datetime.now(), message)
    response = handle(message)
    socket.send_json(response)