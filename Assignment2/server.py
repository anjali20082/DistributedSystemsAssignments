#
#   Hello World server in Python
#   Binds REP socket to tcp://*:8888
#   Expects b"Hello" from client, replies with b"World"
import time
import zmq
import sys

port = "8880"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request from client: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string("Hi client! from %s" % port)