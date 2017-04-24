
class Character:
	'''Character class, NPCs, players, and mobs inherit this class'''
	
	name = ''
	desc = ''
	ctype = '' # the type of character this is
	did = 0 #discord id, 0 is for non player characters
	pos = (0,0) # map room position
	awake = False

	# these will probably change around. Just placeholder for now.
	stats = {
		'hp' : 0,
		'str' : 0,
		'dex' : 0,
		'int' : 0,
		'wis' : 0,
		'atk' : 0,
		'def' : 0,
		'eva' : 0
		'lck' : 0
	}

	def __init__(name, desc, ctype, ctype):
		name = name
		desc = desc
		ctype = ctype
		did = did

	def setstats():
		return None

	def getstats():
		return stats

	def __del__():
		None