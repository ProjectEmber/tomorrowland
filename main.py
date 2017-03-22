from threading import Thread
from time import sleep

from confluent_kafka import Producer
import json


def citysimulator():
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    JSONProducer('lamp', p, 10).start()
    JSONProducer('traffic', p, 1).start()
    JSONProducer('lumen', p, 1).start()


class JSONProducer(Thread):

    def __init__(self, type, producer, period):
        Thread.__init__(self)
        file = open(type + '.json', 'r')
        text = file.read()
        self._text = text.replace('\n', '')
        self._producer = producer
        self._period = period
        self._type = type

    def run(self):
        while True:
            sleep(self._period)
            self._producer.produce(self._type, self._text.encode('utf-8'))


citysimulator()
