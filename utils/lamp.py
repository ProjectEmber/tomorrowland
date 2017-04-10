import random
from datetime import datetime

from generator import MODELS


class Lamp:
    def __init__(self, lamp_id, address, control_unit):
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
        self.control_unit = control_unit
        self.consumption = model[1]
        self.power_on = False
        self.level = 1.0
        self.sent = int(datetime.now().timestamp())
        self.last_replacement = int(datetime(2017, 2, 25).timestamp())

    def change_power(self):
        """
        Change the power status of the lamp according to a time variable function
        """
        self.power_on = False  # TODO to make a variable

    def change_consumption(self):
        self.consumption = self.consumption + random.randint(-5, +5)
        if self.consumption < 40:
            self.consumption = 40
        if self.consumption > 100:
            self.consumption = 100

    def update_sent(self):
        """
        Update the time instant of when the data is retrieved
        """
        self.sent = int(datetime.now().timestamp())

