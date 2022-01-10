import zmq
import random
import sys
import time

port = "1009"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while True:

    string = input("enter your message here: ")
    msg = socket.recv()
    print(msg)
    socket.send_string(string +" from client")
    # socket.send_string("client message to server2")
    time.sleep(1)