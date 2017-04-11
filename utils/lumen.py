from datetime import datetime

import numpy

class Lumen:
    def __init__(self, lumen_id, address):
        """
        Lumen constructor
        
        :param lumen_id: Integer: id of the lumen sensor (it must be the same of the lamp
         where it is located)
        :param address: String: street where the lumen sensor is (same boundary of the id)
        """
        self.id = lumen_id
        self.address = address
        self.ambient = 5.0  # Fixed value at t0
        self.retrieved = int(datetime.now().timestamp())
        self.time = 0.0

    def change_ambient(self):
        """
        Change the ambient value according to a time variable function
        """
        # self.time = numpy.round(self.time + 0.05, 2)
        # self.ambient = numpy.round(34.0*numpy.abs(1.0/8.0*numpy.sin(self.time)), 2)
        self.ambient = 5.0

    def update_retrieved(self):
        """
        Update the time instant of when the data is retrieved
        """
        self.retrieved = int(datetime.now().timestamp())

    def __getstate__(self):
        state = dict(self.__dict__)
        del state['time']
        return state

