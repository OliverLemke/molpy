import numpy as np
import os

def distance(point1,point2):
    """
    Calculate distance between two points

    Parameters
    ----------
    point1: array_like
        The first point.
    point2: array_like
        The second point.

    Returns
    -------
    float
        The distance between point1 and point2
    """
    point1=np.asarray(point1)
    point2=np.asarray(point2)
    return np.linalg.norm(point1-point2)

def read_xyz(molecule):
    filename_m=molecule
    data=np.genfromtxt(fname=filename_m,skip_header=2,dtype='unicode')
    labels=data[:,0]
    geometry=np.float_(data[:,1:])
    mass=np.asarray([atomic_mass[el] for el in labels])

    return {'labels':labels,'geometry':geometry,'mass':mass}

dirname = os.path.dirname(os.path.abspath(__file__))
atomic_mass = {'H': 1.00784, 'C': 12.0107,'O': 15.999}
