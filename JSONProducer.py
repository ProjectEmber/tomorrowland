import json
from threading import Thread
from time import sleep


class JSONProducer(Thread):
    def __init__(self, type, producer, period, data, test):
        """
        Class constructor
        :param type: String: Kafka topics where to write into ("lamp", "traffic" or "lumen")
        :param producer: KafkaProcuder instance
        :param period: Integer: time period in seconds
        :param data: Object instance of Lamp, Traffic or Lumen
        :param test: 0 or 1 - send to Kafka or print
        """
        Thread.__init__(self)
        self._producer = producer
        self._period = period
        self._type = type
        self._data = data
        self._test = test

    def run(self):
        # continuosly
        while True:
            # Depending on the type
            if self._type == "lamp":
                # Update the timestamp for the "sent" attribute
                self._data.update_sent()
                # Produce the element to Kafka or print it
                self._producer.produce(self._type, json.dumps(self._data.__dict__)) \
                    if not self._test else print(json.dumps(self._data.__dict__))
                # Change the power status for the next update
                self._data.change_power()

            if self._type == "lumen":
                # Produce the element to Kafka or print it
                self._producer.produce(self._type, json.dumps(self._data.__dict__)) \
                    if not self._test else print(json.dumps(self._data.__dict__))
                # Change the ambient value for the next update
                self._data.change_ambient()

            if self._type == "traffic":
                self._data.update_retrieved()
                # Produce the element to Kafka or print it
                self._producer.produce(self._type, json.dumps(self._data.__dict__)) \
                    if not self._test else print(json.dumps(self._data.__dict__))
                # Update the traffic intensity value for the next update
                self._data.update_intensity()

            sleep(self._period)
