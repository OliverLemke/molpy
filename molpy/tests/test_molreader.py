import molpy
import pytest
import numpy as np

@pytest.mark.parametrize('molecule, Center_of_mass, natoms',[('water',[10.138, 7.604, 12.673],3),('benzene',[-1.405,0,0],12)])

def test_read(molecule,Center_of_mass,natoms):
	mol = molpy.data.get_molecule(molecule)
	assert np.average(mol['geometry'],weights=mol['mass'],axis=0)==pytest.approx(Center_of_mass, abs=1e-3)
	assert len(mol["geometry"]) == natoms
	assert len(mol["labels"]) == natoms
