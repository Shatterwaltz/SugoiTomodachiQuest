from game import gear

def gear_test(floorNumber):
	"""Creates a gear from floor 10 of the dungeon, 
		and displays its type, how many mods to generate, 
		what mods were rolled."""
	print("Generating gear as if it dropped from floor "+str(floorNumber))
	g = gear.Gear(floorNumber)
	print("gear type: "+str(g.gearType))
	print(str(g.modCount)+" mods generated.")
	print("List of mods: "+str(g.mods))