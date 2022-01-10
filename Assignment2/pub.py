import zmq
import random
import sys
import time

port = "2220"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

mesg = [4, 5, 6, 7]
msgcurr = 0

while(True):
    time.sleep(1)
    socket.send_pyobj({msgcurr:mesg[msgcurr]})
    if(msgcurr == 3):
        msgcurr = 0
    else:
        msgcurr = msgcurr + 1    