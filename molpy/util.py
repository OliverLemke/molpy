import numpy as np
import os


def distance(point1, point2):
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
    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)

#Dirname = os.path.dirname(os.path.abspath(__file__))

def read_xyz(molecule):
    """
    Reads in an .xyz file

    Parameters
    ----------
    molecule: str
        Location of the .xyz file to be read.

    Returns
    -------
    dict
        Dictionary containing the labels of the atoms ["labels"], the geometry ["geometry"] and the masses ["mass"].
    """
    filename_m = molecule
    data = np.genfromtxt(fname=filename_m, skip_header=2, dtype='unicode')
    labels = data[:, 0]
    geometry = np.float_(data[:, 1:])
    mass = np.asarray([atomic_mass[el] for el in labels])

    return {'labels': labels, 'geometry': geometry, 'mass': mass}

atomic_mass = {'H': 1.00784, 'C': 12.0107, 'O': 15.999}
