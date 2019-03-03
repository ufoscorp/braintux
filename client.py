from datetime import datetime
import os
import sys
import time

import zmq


port = 8660

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.RCVTIMEO = 500
socket.connect('tcp://localhost:{}'.format(port))

while True:
    socket.send_json([input()])
    message = socket.recv_json()
    print(datetime.now(), message)