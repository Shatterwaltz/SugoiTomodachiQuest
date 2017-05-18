import random
from room import Room

"""generate and printMap are the only two important ones. import these."""

"""width and height of map grid, number of rooms to generate, 
   secretChance is a decimal value from 0-1 denoting chance of
   spawning an NPC room or a secret room."""
def generate(width, height, targetRoomCount, secretChance):
	w = width
	h = height
	"""If dungeon is too small, turn into a 1x2"""
	if w*h < 2:
		w = 2
		h=1
		
	"""Safeties for number of rooms to generate"""
	if targetRoomCount < 1 or targetRoomCount > w*h:
		targetRoomCount = w*h
	
	if secretChance < 0:
		secretChance = 0
	if secretChance > 1:
		secretChance = 1
	return generateHelper(w, h, targetRoomCount, secretChance)

def mapToString(map):
	ostring=""
	for i in range(len(map[0])):
		for j in range(len(map)):
			if map[j][i]==None:
				ostring+="|?:????"
			else:
				ostring+="|"+str(map[j][i].roomType)+":"+str(map[j][i].printAdj())
		ostring+="|\n"	
	return ostring	

	
	
"""Errors can occur if you create a map too small, use generate() to be safe"""	
def generateHelper(width, height, targetRoomCount, secretChance):
	print("generating...")
	"""init random number generator"""
	random.seed()
	"""init empty 2d array"""
	map = [[None for h in range(height)] for w in range(width)]
	"""Place room in center of map. Type is start room."""
	map[int(width/2)][int(height/2)] = Room(int(width/2), int(height/2), 1)
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
		newRoom = Room(selection[0], selection[1], 0)
		map[selection[0]][selection[1]] = newRoom
		selection[2].addAdjacentRoom(newRoom)
		newRoom.addAdjacentRoom(selection[2])
	"""Turn a room into boss room"""
	random.choice(getDeadEnds(map)).roomType = 2
	"""Check if a secret room should generate, then do so if should"""
	if random.random() < secretChance:
		random.choice(getDeadEnds(map)).roomType = 3
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

"""Return a list of normal dead ends. These are ideal for turning into special rooms."""
def getDeadEnds(map):
	deadEnds = []
	for i in range(len(map)):
		for j in range(len(map[0])):
			if map[i][j]!=None:
				if map[i][j].getNumberAdjacent() == 1 and map[i][j].roomType == 0:
					deadEnds.append(map[i][j])
	return deadEnds