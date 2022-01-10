import time
import zmq
import pprint

def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:1112")
    collecter_data = {}
    for x in range(1000):
        result = results_receiver.recv_json()
        print(result)
        # collecter_data
        if ((result['consumer']) in collecter_data.keys()):
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1000
        else:
            collecter_data[result['consumer']] = 1
        if x == 999:
            pprint.pprint(collecter_data)

result_collector()