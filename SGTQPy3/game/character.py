from game import stats
import copy
import random

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
        self.exp = 0
        self.__stats = stats.Stats()
        
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, val):
        self.__stats = val

    def genStats(self, baseStats):
        '''
        @arg base -> stats.Stats
        base is nullable
        Generate the players stats. Base can be given to use as the class base stats.
        Every base class has the same base stat pool of 5 points to assign on top of the base stats
        for the given class
        E.g.
            base pool of 40 plus additional 5 to randomly dist
            rougue:
                health:     (5, 2, 7)
                armor:      (4, 0, 4)
                power:      (3, 1, 4)
                evasion:    (6, 3, 9)
                accuracy:   (4, 0, 4)
                speed:      (6, 0, 6)
                strength:   (3, 0, 3)
                luck:       (4, 0, 4)
                resistance: (5, 0, 5)
                
                base total = 40
                total = 45
        This is the same base stat pool of all classes, but the bases are hand distributed, while the
        5 point "variance pool" is randomly distributed over the stats.
        '''
        if baseStats is None:
            # Handle this case somehow
            None
        else:
            self.stats = copy.deepcopy(baseStats)
            pool = 5
            while pool > 0:
                stat = random.choice(list(self.stats.__dict__))
                print(stat)
                base, mod, modified = self.stats.__dict__[stat]
                newMod = int(1 + random.random() * pool)
                print(newMod)
                pool = pool - newMod
                newMod = newMod + mod
                newStat = (base, newMod, base+newMod) 
                self.stats.__dict__[stat] = newStat
                
                

                



