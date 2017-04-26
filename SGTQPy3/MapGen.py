import random
import pprint
class Room:
	"""Have a field to store monsters in this room"""
	
	"""List holds references to four other rooms.
	[North, South, East, West].
	If None, then no room in that direction."""
	adjacentRooms = [None, None, None, None]
	
	"""Have a field to put a chest"""
	
	"""coordinates tuple"""
	coordinates = (0,0)
	
	"""Add adjacent room."""
	def addAdjacentRoom(self, room):
		print(str(room.getCoords())+" "+str(self.getCoords()))
		if room.getCoords()[0]>self.coordinates[0]:
			print ("E")
			self.adjacentRooms[2]=room
		if room.getCoords()[0]<self.coordinates[0]: 
			print ("W")
			self.adjacentRooms[3]=room
		if room.getCoords()[1]>self.coordinates[1]: 
			print ("S")
			self.adjacentRooms[1]=room
		if room.getCoords()[1]<self.coordinates[1]: 
			print ("N")
			self.adjacentRooms[0]=room
	
	def getAdjacencyList(self):
		return self.adjacentRooms
	
	def getCoords(self):
		return self.coordinates
	
	"""Print list of directions in which other rooms lie"""
	def printAdj(self):
		ostring = ""
		if self.adjacentRooms[0]!=None:
			ostring+="N"
		else:
			ostring += "X"
		if self.adjacentRooms[1]!=None:
			ostring+="S"
		else:
			ostring += "X"
		if self.adjacentRooms[2]!=None:
			ostring+="E"
		else:
			ostring += "X"
		if self.adjacentRooms[3]!=None:
			ostring+="W"
		else:
			ostring += "X"
		return ostring	
	
	def __init__(self, x, y):
		self.coordinates = (x,y)
	
class MapGen:

	"""possibly some errors if you try to generate a map with width or height 1"""
	def generate(self, width, height):
		
		"""init empty 2d array"""
		map = [[None for w in range(width)] for h in range(height)]
		"""Place room in center of map"""
		map[int(height/2)][int(width/2)] = Room(int(height/2), int(width/2))
		"""Loop will fill entire map with rooms."""
		for i in range((width*height-1)):
			"""possible locations to add a room are stored in this list and then randomly chosen"""
			possibleRoomLocations = [] 
			for w in range(width):
				for h in range(height):
					temp=self.ifEmptyGetAdjacent(w, h, map)
					if temp!=None:
						"""Add a tuple containing the coords of an empty space and an adjacent room"""
						possibleRoomLocations.append((w, h, temp))
			"""Grab a random option from list of possibilities"""
			selection = random.choice(possibleRoomLocations)
			"""init a room at selected location"""
			newRoom = Room(selection[0], selection[1])
			map[selection[1]][selection[0]] = newRoom
			selection[2].addAdjacentRoom(newRoom)
			'''newRoom.addAdjacentRoom(selection[2])'''
		return map
		
	"""given coordinates, return an adjacent room if it coordinates are empty"""	
	def ifEmptyGetAdjacent(self, x, y, map):
		if map[y][x]==None:
			if x>0:
				if map[y][x-1] != None:
					return map[y][x-1]
			
			if y>0:
				if map[y-1][x] != None:
					return map[y-1][x]
			
			if x<len(map[0])-2:
				if map[y][x+1] != None:
					return map[y][x+1]
			
			if y<len(map)-2:
				if map[y+1][x] != None:
					return map[y+1][x]
					
		return None	
	
	def printMap(self, map):
		ostring=""
		for j in range(len(map[0])):
			for i in range(len(map)):
				if map[i][j]==None:
					ostring+="|????"
				else:
					ostring+="|"+str(map[i][j].printAdj())
			ostring+="|\n"	
		return ostring



r= Room(1,1)
s=Room(0,1)
r.addAdjacentRoom(s)
print(r)
print(s)
print(r.getAdjacencyList())
print(s.getAdjacencyList())

