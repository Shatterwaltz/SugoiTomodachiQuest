from game.stats import Stats 
import random

"""Represents a piece of gear"""
class Gear(object):

	"""Requires the current floor number be passed in.
	   Used in mod generation."""
	def __init__(self, floorNumber):
		random.seed()
		"""0: Helmet
		   1: Chest
		   2: Gauntlets
		   3: Greaves
		   4: Ring"""
		self.__gearType = random.randint(0,4)
		"""Number of mods to generate"""
		self.__modCount = random.randint(1,6)
		"""How many tiers of mod values are available"""
		self.__availableTiers = int(floorNumber / 2)+1
		self.__mods = []
		"""Only made so I can grab the list of stats."""
		self.__statObject = Stats()
		"""stores the chance for each tier to be used for mod generation"""
		self.__tierDropChances = self.__generateTierTable()
		for i in (range((self.__modCount))):
			"""Add a tuple (stat, modifier) to list of mods"""
			self.__mods.append( (random.choice(list(self.__statObject.__dict__)), self.__generateModValue()))
	@property
	def gearType(self):
		return self.__gearType
	
	@property
	def modCount(self):
		return self.__modCount
	
	@property
	def mods(self):
		return self.__mods
	
	"""Apply algorithm to create table of chance to roll each item tier"""
	def __generateTierTable(self):
		"""first, assign an even probability to every tier."""
		dropTable = [(100.0/self.__availableTiers) for i in range(self.__availableTiers)]
                """the value i is used in modifying drop rates"""
		i = len(dropTable)/2
		"""n is used to track the current step, working backwards through the array"""
		n = len(dropTable)-1
		while(i>1):
			temp = dropTable[n]
			
			"""Divide current element by i"""
			dropTable[n] /= i 
			"""Add the lost drop chance to the tier on opposite end of array"""
			dropTable[len(dropTable)-1-n]+=temp-dropTable[n]
			"""Decrementing i lowers the amount the drop chance is changed.
			Decrementing n moves to the next value to be modified."""
			i-=1
			n-=1
			
		"""Random tier selection will be done by comparing a random number to each 
		probability. If the random number is smaller than the current probability, 
		the result corresponding to that probability is chosen. To make this doable, 
		modifying the array here to make each probability equal to itself summed with 
		all probabilities lower than itself. Easier if we sort rarest->most common."""
		dropTable.reverse()
		for i in range(1, len(dropTable)):
			dropTable[i]+=dropTable[i-1]
		return dropTable

	"""Selects a tier from the list of tiers with weighted probabilities, and then randomly
		returns a value from within its corresponding range."""
	def __generateModValue(self):
		roll = random.random()*100
		for i in range(len(self.__tierDropChances)):
			if roll<self.__tierDropChances[i]:
				return random.randint(5*(self.__availableTiers-i)-4, 5*(self.__availableTiers-i))
