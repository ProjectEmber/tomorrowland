import random

# tuples of street names and control unit numbers
STREETS = [
    ['Piazza Massimo D\'Azeglio', "cu1"],
    ['Corso Vittorio Emanuele', "cu1"],
    ['Via Giuseppe Garibaldi', "cu1"],
    ['Via Fratelli Zuccari', "cu1"],
    ['Viale Ungheria', "cu1"]
]

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

    # Traffic sensor generation
    for i in range(0, len(STREETS)):
        # We need to create only one traffic sensor for each street
        traffics.append(Traffic(i))

    # Lamp and Lumen generation
    for i in range(0, num):
        # Choose a random street
        street = random.choice(STREETS)
        address = street[0]
        control_unit = street[1]
        # Generate a Lamp and a Lumen with the same id and street (they are co-located)
        new_lamp = Lamp(i, address, control_unit)
        new_lumen = Lumen(i, address)
        # Append them to the proper list
        lamps.append(new_lamp)
        lumens.append(new_lumen)

    return lamps, lumens, traffics
