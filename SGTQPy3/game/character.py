from game import stats

class Character(object):
    '''
    Class which represents a character in the game.
    A character is anything which needs to have stats and a map position.
    '''
    
    def __init__(self, desc, ctype, did):	
        self.name = ''
        self.desc = ''
        self.ctype = '' # the type of character this is
        self.did = 0 #discord id, 0 is for non player characters
        self.pos = (0,0) # map room position
        self.awake = False
        self.__stats = stats.Stats()
        
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, val):
        if val is stats.Stats:
            self.__state = val
        else:
            pass

