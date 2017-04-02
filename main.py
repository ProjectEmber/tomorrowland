from threading import Thread
from time import sleep

from kafka import KafkaProducer
import json
import generator
import sys
import requests
from JSONProducer import JSONProducer

test = 0

def citysimulator():
    """
    The Ember City Simulator:
        - inizializes the Kafka Producer
        - gets lists of lamps, lumens and traffics objects
        - starts a Thread for each oject
    """
    p = KafkaProducer(bootstrap_servers="kafka.project-ember.city:9092") if not test else ""

    lamps, lumens, traffics = generator.get_lists(100);

    # for each element we pass:
    # - the topic where to write into
    # - the Kafka Producer used
    # - the lamp, lumen or traffic object reference
    # - if it is a test or not
    for lamp in lamps:
        requests.post("localhost:3000",lamp)  # register all the lamps to the control unit
        JSONProducer('lamp', p, 10, lamp, test).start()
    for lumen in lumens:
        JSONProducer('lumen', p, 10, lumen, test).start()
    for traffic in traffics:
        JSONProducer('traffic', p, 20, traffic, test).start()


if __name__ == "__main__":
    # Set test to 1 if you want to print jsons instead of sending them to Kafka
    test = 0
    citysimulator()
