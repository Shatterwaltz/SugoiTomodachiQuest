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

	def reversepolish(self, expr):
		# use a stack to parse and perfrom rp calculation for number of sides
		# take  2 5 + 4 - in RPN, in infix notation this would be (2 + 5) - 4
		ops = {
			'+': lambda a,b: b+a,
			'-': lambda a,b: b-a,
			'*': lambda a,b: b*a,
			'/': lambda a,b: b/a,
			'^': lambda a,b: b**a
		}
		stack = []
		expr = expr.split(' ')
		for c in expr:
			if c in ops: stack.append(ops[c](stack.pop(),stack.pop()));
			else: stack.append(float(c))
		return stack.pop()
		

'''
roller = DieRoller()
print(roller.reversepolish('4 2 + 1 -'))
print(roller.reversepolish('4 2 + 1 13 5 6 * / ^ -'))
print(roller.reversepolish('4 2 + 3 13 5 6 * / ^ -'))
'''