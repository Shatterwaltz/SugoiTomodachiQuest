"""Just a file for testing map generation and stuff.
   Usable for reference. """
   
"""import map generation method, and map to string method""" 
from mapGen import generate, mapToString

"""Generate a 5x5 map with 24 rooms and a 49% chance to contain a secret room"""
m = generate(5,5,24, .49);

"""Convert map to string and print it"""
print (mapToString(m));

"""
rooms are displayed in format |n:XXXX|
n is the room type, where 
	0=normal
	1=start
	2=boss
	3=secret
X will be either N,S,E,W, or _. Denotes if a room lies in that direction, or nothing."""