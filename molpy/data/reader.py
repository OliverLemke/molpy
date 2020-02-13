import os
import numpy as np
from ..util import read_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')  #works in general

with open(filename) as handle:
    look_and_say = handle.read()

def get_molecule(molecule):
    return read_xyz(os.path.join('data',molecule+'.xyz'))
