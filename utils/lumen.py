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
        self.ambient = 1.0  # Fixed value at t0
        self.time = 0.0

    def change_ambient(self):
        """
        Change the ambient value according to a time variable function
        """
        self.time = numpy.round(self.time + 0.2, 1)
        self.ambient = numpy.round(10.0*numpy.power(numpy.sin(self.time), 2), 1)

    def __getstate__(self):
        state = dict(self.__dict__)
        del state['time']
        return state

