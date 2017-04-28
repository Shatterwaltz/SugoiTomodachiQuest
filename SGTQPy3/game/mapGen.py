import random
from room import Room
class MapGen:

	"""possibly some errors if you try to generate a map with width or height 1"""
	def generate(self, width, height):
		print("generating...")
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
			newRoom.addAdjacentRoom(selection[2])
		print("generation complete")
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
