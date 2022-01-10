import sys
import zmq
# 
port = "2220"


# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from scores server...")
socket.connect ("tcp://localhost:%s" % port)
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while(True):
    msg = socket.recv_pyobj()
    print(msg)
    
