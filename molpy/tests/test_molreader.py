import molpy
import pytest
import numpy as np

@pytest.mark.parametrize('molecule, Center_of_mass',[('water',[0,0,0]),('benzene',[-1.405,0,0])])

def test_read(molecule,Center_of_mass):
	mol = molpy.data.get_molecule(molecule)
	assert np.average(mol['geometry'],weights=mol['mass'],axis=0)==pytest.approx(Center_of_mass, abs=1e-3)
