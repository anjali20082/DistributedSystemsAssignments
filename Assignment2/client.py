
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:8888
#   Sends "Hello" to server, expects "World" back
#

import zmq
import sys

port = "8880"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

context = zmq.Context()

#  Socket to talk to server
print("----------------Connecting to the server-----------------")
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)

    
#  Do 8 requests, waiting each time for a response
for request in range(8):
    print("Sending request %s …" % request)
    socket.send_string("Hello server")

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))