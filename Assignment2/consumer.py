import time
import zmq
import random
import math

def consumer():
    consumer_id = random.randrange(1,10005)
    print("I am consumer #%s" % (consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:1111")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:1112")
    
    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = { 'consumer' : consumer_id, 'num' : math.pow(data,2)}
        # if data%2 == 0: 
        # if data:
        print("data from producer to consumer ", consumer_id, "is: ", result['num'])
        consumer_sender.send_json(result)

consumer()