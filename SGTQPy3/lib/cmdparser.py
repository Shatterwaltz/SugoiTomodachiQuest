
class CmdParser:
	'''
	handles parsing command strings into tokens to associate with function calls
	Commands may be registered by their primary token, that is the command name itself.
	They must accompany a callback function which defines the code to be executed should
	we receive a registered command
	'''

	cmds = {} # hold the command string and the callback function registered to it

	# callback shouls take two args; opts - the rest of the tokenized string, 
	def regcmd(self, cmd, cb):
		if cmd != '':
			cmds[cmd] = cb
			return True
		else:
			return False

	def callcmd(self, cmdstring):
		tokens = self.tokenize(cmdstring)
		return cmds[cmd](tokens[1:])

	def tokenize(self, cmdstring, delim):
		if delim == None or delim == '':
			delim = ' '
		return cmdstring.split(delim)