import argparse
import molpy

parser = argparse.ArgumentParser(description="Reads XYZ files and calculates the distance between two atoms at index1 and index2")
parser.add_argument('filename', type=str, help="The XYZ file to read")
parser.add_argument('index1', type=int, help="Index of the first atom")
parser.add_argument('index2', type=int, help="Index of the second atom")


def main():
	args = parser.parse_args()
	mol = molpy.util.read_xyz(args.filename)
	print("The distance is %.3f Angstrom" %(molpy.util.distance(mol["geometry"][args.index1,:],mol["geometry"][args.index2,:])))

