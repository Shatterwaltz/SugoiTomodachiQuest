
class Character:
    '''Character class, NPCs, players, and mobs inherit this class'''
    def __init__(self, desc, ctype, did):	
        self.name = ''
        self.desc = ''
        self.ctype = '' # the type of character this is
        self.did = 0 #discord id, 0 is for non player characters
        self.pos = (0,0) # map room position
        self.awake = False
        
        # these will probably change around. Just placeholder for now.
        self.stats = {
            'hp' : 0,
            'str' : 0,
            'dex' : 0,
            'int' : 0,
            'wis' : 0,
            'atk' : 0,
            'def' : 0,
            'eva' : 0, 
            'lck' : 0
        }

    def setstats(self):
        return None

    def getstats(self):
        return stats
