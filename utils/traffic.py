from datetime import datetime

import numpy

from generator import STREETS


class Traffic:
    def __init__(self, i):
        """
        Traffic constructor
        :param i: Integer: used to take the street for the list in order 
        """
        self.address = STREETS[i][0]
        self.retrieved = int(datetime.now().timestamp())
        self.intensity = 0.0
        self.time = 0.0

    def update_retrieved(self):
        """
        Update the time instant of when the data is retrieved
        """
        self.retrieved = int(datetime.now().timestamp())

    def update_intensity(self):
        """
        Update the traffic intensity value recorded
        """
        self.time = numpy.round(self.time + 0.05, 2)
        self.intensity = numpy.round((self.time - numpy.floor(self.time)), 2)

    def __getstate__(self):
        state = dict(self.__dict__)
        del state['time']
        return state
