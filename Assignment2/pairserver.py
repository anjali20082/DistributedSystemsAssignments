import zmq
import random
import sys
import time

port = "1009"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    string = input("enter your message here: ")
    socket.send_string(string + " from server")
    msg = socket.recv()
    print(msg)
    time.sleep(1)