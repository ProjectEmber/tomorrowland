import random
from datetime import datetime

from generator import MODELS


class Lamp:
    def __init__(self, lamp_id, address):
        """
        Lamp constructor
        :param lamp_id: Integer
        :param address: String
        """
        # Data attributes are defined according to lumen.json in datatype
        self.id = lamp_id
        self.address = address
        model = random.choice(MODELS)
        self.model = model[0]
        self.consumption = model[1]
        self.power_on = True
        self.level = 1.0
        self.sent = int(datetime.now().timestamp())
        self.last_replacement = int(datetime.now().timestamp() - datetime(2017, 2, 25).timestamp())

    def change_power(self):
        """
        Change the power status of the lamp according to a time variable function
        """
        self.power_on = True  # TODO to make a variable

    def update_sent(self):
        """
        Update the time instant of when the data is retrieved
        """
        self.sent = int(datetime.now().timestamp())

