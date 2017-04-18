import random
from namesake import getname

# tuples of street names and control unit numbers
STREETS = []

# tuples of model names and power consumption values
MODELS = [
    ['NORMAL', 40],
    ['LED', 60],
    ['OLD', 100]
]

from utils.lamp import Lamp
from utils.lumen import Lumen
from utils.traffic import Traffic


def get_lists(num):
    # Prepare lists
    """
    List constructor for the simulation
    
    :param num: Integer: number of lamps (and lumens) in the simulation
    :return: three lists: lamps, lumens and traffics each one containing the proper objects
    """
    lamps = []
    lumens = []
    traffics = []

    for i in range(0, 100):
        STREETS.append(getname().replace("-", ""))

    # Traffic sensor generation
    h = 0
    for i in range(0, len(STREETS)):
        # We need to create only one traffic sensor for each street
        traffics.append(Traffic(i))
        # Lamp and Lumen generation
        for j in range(0, num):
            # Choose a random street
            address = STREETS[i]
            control_unit = "cu1"
            # Generate a Lamp and a Lumen with the same id and street (they are co-located)
            new_lamp = Lamp(h, address, control_unit)
            new_lumen = Lumen(h, address)
            # Append them to the proper list
            lumens.append(new_lumen)
            lamps.append(new_lamp)
            h = h + 1

    return lamps, lumens, traffics
