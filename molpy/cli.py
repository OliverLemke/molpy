import argparse
#import molpy

from .util import read_xyz, distance

parser = argparse.ArgumentParser(description="Reads XYZ files and calculates the distance between two atoms at index1 and index2")
parser.add_argument('filename', type=str, help="The XYZ file to read")
parser.add_argument('index1', type=int, help="Index of the first atom")
parser.add_argument('index2', type=int, help="Index of the second atom")

def main():
	args = parser.parse_args()
	#mol = molpy.util.read_xyz(args.filename)
	mol = read_xyz(args.filename)
	print(f"Reading XYZ-file:{args.filename}")
	
	s1 = mol["labels"][args.index1]
	s2 = mol["labels"][args.index2]

	print(f"Calculating distance between {s1} at index {args.index1} and {s2} at index {args.index2}")

	dist = distance(mol["geometry"][args.index1,:],mol["geometry"][args.index2,:])

	print(f"The distance is {dist:.3f} Angstrom")

