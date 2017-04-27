import asyncio

class CmdDict:
        '''
        handles parsing command strings into tokens to associate with function calls
        Commands may be registered by their primary token, that is the command name itself.
        They must accompany a callback function which defines the code to be executed should
        we receive a registered command
        '''
        def __init__(self):
            self.cmds = {} # hold the command string and the callback function registered to it

        # callback should take one arg; cmdargs - the rest of the tokenized string, 
        def regcmd(self, cmd, cb):
                if cmd != '':
                        self.cmds[cmd] = cb
                        return True
                else:
                        return False

        def callcmd(self, cmdstring):
                tokens = self.tokenize(cmdstring, ' ')
                return self.cmds[tokens[0]](tokens[1:])

        async def callcmdasync(self, cmdstring):
                tokens = self.tokenize(cmdstring, ' ')
                return await self.cmds[tokens[0]](tokens[1:])

        def tokenize(self, cmdstring, delim):
                if delim == None or delim == '':
                        delim = ' '
                return cmdstring.split(delim)

'''
parser = CmdDict()
# register a lambda function
parser.regcmd('!test', lambda cmdargs: [print(t) for t in cmdargs])
parser.callcmd('!test arg1 arg2 arg3 poopy head')

#register a normal function
def hello(cmdargs):
        print('hello {}'.format(cmdargs[0]))
parser.regcmd('!hello', hello)
parser.callcmd('!hello Ibitsu!')
'''
