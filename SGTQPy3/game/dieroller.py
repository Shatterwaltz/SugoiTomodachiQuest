import random

class DieRoller:
	'''
	A class that allows one to simulate dice rolls of even sides > 1
	'''
	def roll(self, sides):
		if sides % 2 != 0 or sides < 2:
			return -1
		else:
			return random.randrange(1, sides)

	def rolltwo(self, sides):
		if sides % 2 != 0 or sides < 2:
			return (-1,-1)
		else:
			return (random.randrange(1,sides), \
				random.randrange(1,sides))

'''
roller = DieRoller()
print(roller.rolltwo(20))
print(roller.roll(21))
print(roller.roll(20))
'''