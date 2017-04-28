class Room:
	"""Have a field to store monsters in this room"""
	"""Have a field to put a chest"""
	def __init__(self, x, y):
		self.__coordinates = (x,y)
		"""List holds references to four other rooms.
		[North, South, East, West].
		If None, then no room in that direction."""
		self.__adjacentRooms = [None, None, None, None]
	
	@property
	def coordinates(self):
		return self.__coordinates
	
	@property
	def adjacentRooms(self):
		return self.__adjacentRooms
	
	"""Add adjacent room."""
	def addAdjacentRoom(self, room):
		if room.coordinates[0]>self.__coordinates[0]:
			self.__adjacentRooms[2]=room
		if room.coordinates[0]<self.__coordinates[0]: 
			self.__adjacentRooms[3]=room
		if room.coordinates[1]>self.__coordinates[1]: 
			self.__adjacentRooms[1]=room
		if room.coordinates[1]<self.__coordinates[1]: 
			self.__adjacentRooms[0]=room

	
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
	
	