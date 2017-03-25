from datetime import datetime

from generator import STREETS


class Traffic:
    def __init__(self, i):
        """
        Traffic constructor
        :param i: Integer: used to take the street for the list in order 
        """
        self.address = STREETS[i]
        self.retrieved = int(datetime.now().timestamp())
        self.intensity = 5.0

    def update_retrieved(self):
        """
        Update the time instant of when the data is retrieved
        """
        self.retrieved = int(datetime.now().timestamp())

    def update_intensity(self):
        """
        Update the traffic intensity value recorded
        """
        self.intensity = 5.0  # TODO to make a math function (maybe a cos?)
