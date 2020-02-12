import os

dirname = os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(dirname,'look_and_say.dat') #works in general

with open(filename) as handle:
    look_and_say=handle.read()
