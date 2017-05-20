class Room(object):
	"""Have a field to store monsters in this room"""
	"""Have a field to put a chest"""
	def __init__(self, x, y, type):
		self.__coordinates = (x,y)
		"""List holds references to four other rooms.
		[North, South, East, West].
		If None, then no room in that direction."""
		self.__adjacentRooms = [None, None, None, None]
		self.__roomType = type
		
	@property
	def coordinates(self):
		return self.__coordinates
	
	@property
	def adjacentRooms(self):
		return self.__adjacentRooms
	
	"""0: normal
	   1: start room
	   2: boss room
	   3: Hidden room 
	   4: Quest room"""
	@property
	def roomType(self):
		return self.__roomType
	
	@roomType.setter
	def roomType(self, value):
		if value > 4 or value < 0:
			self.__roomType = 0
		else:
			self.__roomType = value
	
	"""Add adjacent room. Doesn't perform safety checks, so be careful.
	   should only add rooms that would be adjacent to it."""
	def addAdjacentRoom(self, room):
		if room.coordinates[0]>self.__coordinates[0]:
			self.__adjacentRooms[2]=room
		if room.coordinates[0]<self.__coordinates[0]: 
			self.__adjacentRooms[3]=room
		if room.coordinates[1]>self.__coordinates[1]: 
			self.__adjacentRooms[1]=room
		if room.coordinates[1]<self.__coordinates[1]: 
			self.__adjacentRooms[0]=room

	def getNumberAdjacent(self):
		count = 0
		for i in range(len(self.__adjacentRooms)):
			if self.__adjacentRooms[i]!=None:
				count+=1
		return count
	
	
	"""Print list of directions in which other rooms lie"""
	def printAdj(self):
		ostring = ""
		if self.__adjacentRooms[0]!=None:
			ostring+="N"
		else:
			ostring += "_"
		if self.__adjacentRooms[1]!=None:
			ostring+="S"
		else:
			ostring += "_"
		if self.__adjacentRooms[2]!=None:
			ostring+="E"
		else:
			ostring += "_"
		if self.__adjacentRooms[3]!=None:
			ostring+="W"
		else:
			ostring += "_"
		return ostring	
	
	