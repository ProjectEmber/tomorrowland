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
        self.ambient = 10.0  # Fixed value at t0

    def change_ambient(self):
        """
        Change the ambient value according to a time variable function
        """
        self.ambient = 10.0  # TODO to make a time variable
