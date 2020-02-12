import molpy

def test_distance():
	assert molpy.util.distance([0,1],[0,0])==1

def test_distance2():
	assert molpy.util.distance([1,0],[0,0])==1
