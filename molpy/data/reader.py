import os
import numpy as np
from ..util import read_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(dirname,'look_and_say.dat') #works in general

with open(filename) as handle:
    look_and_say=handle.read()

#def get_molecule(molecule):
#    filename_m=os.path.join(dirname,molecule+'.xyz')
#    data=np.genfromtxt(fname=filename_m,skip_header=2,dtype='unicode')
#    labels=data[:,0]
#    geometry=np.float_(data[:,1:])
#    mass=np.asarray([atomic_mass[el] for el in labels])
#
#    return {'labels':labels,'geometry':geometry,'mass':mass}
#
#atomic_mass = {'H': 1.00784, 'C': 12.0107,'O': 15.999}

def get_molecule(molecule):
    return read_xyz(os.path.join(dirname,molecule+'.xyz'))    
    
