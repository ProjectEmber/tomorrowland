from threading import Thread
from time import sleep
from random import randint

from kafka import KafkaProducer
import json
import generator
import sys
import requests
from JSONProducer import JSONProducer

test = 0

lamp_per_street = 0
kafka_remote_addr = ""
control_unit_address = ""
test = 0

def citysimulator():
    """
    The Ember City Simulator:
        - inizializes the Kafka Producer
        - gets lists of lamps, lumens and traffics objects
        - starts a Thread for each oject
    """
    p = KafkaProducer(bootstrap_servers=kafka_remote_addr) if not test else ""

    lamps, lumens, traffics = generator.get_lists(20);

    # for each element we pass:
    # - the topic where to write into
    # - the Kafka Producer used
    # - the lamp, lumen or traffic object reference
    # - if it is a test or not
    for lamp in lamps:
        l = dict()
        l['lamp'] = json.dumps(lamp.__dict__).encode('utf-8')
        requests.post("http://" + control_unit_address + "/newlamp",l)  # register all the lamps to the control unit
        JSONProducer('lamp', control_unit_name, 10, lamp, test).start()
    for lumen in lumens:
        JSONProducer('lumen', p, 10, lumen, test).start()
    for traffic in traffics:
        JSONProducer('traffic', p, 10, traffic, test).start()


if __name__ == "__main__":
    # Set test to 1 if you want to print jsons instead of sending them to Kafka
    # COMMAND LINE
    # reading from command line params
    if "--help" in sys.argv:
        print("USAGE:", "--lamp_per_street=<integer>", "--control_unit=<cu_remote_addr>:<cu_port>", "--test=<0,1>",
              "--kafka=<kafka_remote_addr>:<kafka_port>")
        exit(1)

    # assigning control unit name and kafka address via cli
    try:
        # iterating over args
        for arg in sys.argv:
            if "--lamp_per_street" in arg:
                lamp_per_street = int((arg.split("="))[1])
                continue
            if "--kafka" in arg:
                kafka_remote_addr = str((arg.split("="))[1])
                if len(kafka_remote_addr) == 0:
                    print("No valid kafka address provided!")
                    exit(1)
                continue
            if "--control_unit" in arg:
                control_unit_address = str((arg.split("="))[1])
                if len(control_unit_address) == 0:
                    print("No valid control unit address provided!")
                    exit(1)
                continue
            if "--test" in arg:
                test = int((arg.split("="))[1])
                continue
        if (lamp_per_street == 0) or (len(kafka_remote_addr) == 0) or (len(control_unit_address) == 0):
            print("No valid lamp per street or kafka address or control unit address provided! Setting to default")
            lamp_per_street = 20
            kafka_remote_addr = "localhost:9092"
            control_unit_address = "localhost:5000"
            test = 0

    except Exception as e:
        print(e)
        print("No valid lamp per street or kafka address or control unit address provided!")
        exit(1)

    citysimulator()
