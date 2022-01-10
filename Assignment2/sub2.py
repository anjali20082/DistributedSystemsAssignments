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

listeners = [1, 2]
while(True):
    msg = socket.recv_pyobj()
    msgnmber = (msg.keys())
    msgnmber = list(msgnmber)[0]
    # print((msgnmber))
    if(msgnmber in listeners):
        print(msg.get(msgnmber))
