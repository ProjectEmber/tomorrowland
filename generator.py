import random

STREETS = [
    'Piazza Massimo D\'Azeglio',
    'Corso Vittorio Emanuele',
    'Via Giuseppe Garibaldi',
    'Via Fratelli Zuccari',
    'Viale Ungheria'
]

MODELS = [
    ['NORMAL', 7],
    ['LED', 5],
    ['OLD', 10]
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
        address = random.choice(STREETS)
        # Generate a Lamp and a Lumen with the same id and street (they are co-located)
        new_lamp = Lamp(i, address)
        new_lumen = Lumen(i, address)
        # Append them to the proper list
        lamps.append(new_lamp)
        lumens.append(new_lumen)

    return lamps, lumens, traffics
