import random
from room import Room

"""generate and printMap are the only two important ones. import these."""

def generate(width, height, targetRoomCount):
	w = width
	h = height
	if w < 1:
		w = 1
	if h < 1:
		h = 1
	if targetRoomCount < 1 or targetRoomCount > w*h:
		targetRoomCount = w*h
		print(targetRoomCount)
	return generateHelper(w, h, targetRoomCount)

def printMap(map):
	ostring=""
	for i in range(len(map[0])):
		for j in range(len(map)):
			if map[j][i]==None:
				ostring+="|????"
			else:
				ostring+="|"+str(map[j][i].printAdj())
		ostring+="|\n"	
	return ostring	

	
	
"""Errors if you create a map too small, use generate() to be safe"""	
def generateHelper(width, height, targetRoomCount):
	print("generating...")
	"""init empty 2d array"""
	map = [[None for h in range(height)] for w in range(width)]
	"""Place room in center of map"""
	map[int(width/2)][int(height/2)] = Room(int(width/2), int(height/2))
	"""Loop will fill entire map with rooms."""
	for i in range((targetRoomCount-1)):
		"""possible locations to add a room are stored in this list and then randomly chosen"""
		possibleRoomLocations = [] 
		for w in range(width):
			for h in range(height):
				temp=ifEmptyGetAdjacent(w, h, map)
				if temp!=None:
					"""Add a tuple containing the coords of an empty space and an adjacent room"""
					possibleRoomLocations.append((w, h, temp))
		"""Grab a random option from list of possibilities"""
		selection = random.choice(possibleRoomLocations)
		"""init a room at selected location"""
		newRoom = Room(selection[0], selection[1])
		map[selection[0]][selection[1]] = newRoom
		selection[2].addAdjacentRoom(newRoom)
		newRoom.addAdjacentRoom(selection[2])
	print("generation complete")
	return map
	
"""given coordinates, return an adjacent room if it coordinates are empty"""	
def ifEmptyGetAdjacent(x, y, map):
	if map[x][y]==None:
		choices=[]
		if x>0:
			if map[x-1][y] != None:
				choices.append(map[x-1][y])
		if y>0:
			if map[x][y-1] != None:
				choices.append(map[x][y-1])
		
		if x<len(map)-1:
			if map[x+1][y] != None:
				choices.append(map[x+1][y])
		
		if y<len(map[0])-1:
			if map[x][y+1] != None:
				choices.append(map[x][y+1])
				
		if choices!=[]:
			return random.choice(choices)		
	return None	

