import random
import pprint
class Room:
	"""Have a field to store monsters in this room"""
	"""Have a field to put a chest"""

	
	"""Add adjacent room."""
	def addAdjacentRoom(self, room):
		"""print(str(room.getCoords())+" "+str(self.getCoords()))"""
		if room.getCoords()[0]>self.coordinates[0]:
			print ("E of "+str(self.coordinates))
			self.adjacentRooms[2]=room
		if room.getCoords()[0]<self.coordinates[0]: 
			print ("W of "+str(self.coordinates))
			self.adjacentRooms[3]=room
		if room.getCoords()[1]>self.coordinates[1]: 
			print ("S of "+str(self.coordinates))
			self.adjacentRooms[1]=room
		if room.getCoords()[1]<self.coordinates[1]: 
			print ("N of "+str(self.coordinates))
			self.adjacentRooms[0]=room
		print("Now my list is "+str(self.adjacentRooms))
		
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
			ostring += "_"
		if self.adjacentRooms[1]!=None:
			ostring+="S"
		else:
			ostring += "_"
		if self.adjacentRooms[2]!=None:
			ostring+="E"
		else:
			ostring += "_"
		if self.adjacentRooms[3]!=None:
			ostring+="W"
		else:
			ostring += "_"
		return ostring	
	
	def __init__(self, x, y):
		self.coordinates = (x,y)
		"""List holds references to four other rooms.
		[North, South, East, West].
		If None, then no room in that direction."""
		self.adjacentRooms = [None, None, None, None]
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
			print("__________")
			"""Grab a random option from list of possibilities"""
			selection = random.choice(possibleRoomLocations)
			"""init a room at selected location"""
			newRoom = Room(selection[0], selection[1])
			map[selection[1]][selection[0]] = newRoom
			selection[2].addAdjacentRoom(newRoom)
			newRoom.addAdjacentRoom(selection[2])
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
		for i in range(len(map[0])):
			for j in range(len(map)):
				if map[j][i]==None:
					ostring+="|????"
				else:
					ostring+="|"+str(map[i][j].printAdj())
			ostring+="|\n"	
		return ostring
