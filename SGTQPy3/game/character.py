from game import stats
from game import gear
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
        self.__gear = [gear.Gear(140), gear.Gear(140), gear.Gear(140), gear.Gear(140), gear.Gear(140)]
        
        #Effects will have (stat, mod, duration)
        self.__effects=[]
        self.refreshMods()
    @property
    def stats(self):
        return self.__stats
    @stats.setter
    def stats(self, val):
        self.__stats = val

    @property
    def gear(self):
        return self.__gear
    @gear.setter
    #Set gear piece into the correct slot, overwriting the original.
    #Call refreshMods to update the modifiers to each stat. 
    def gear(self, val):
        self.__gear[val.gearType]=val
        refreshMods()
        
    #For each stat, loop through all gear pieces and add the
    #values of mods that affect the current stat. 
    #repeat for currently active effects. 
    def refreshMods(self):
        for curStat in self.__stats.__dict__:
            tmp=0;
            for gearPiece in self.__gear:
                for mod in gearPiece.mods:
                    if mod[0]==curStat:
                        tmp+=mod[1]
                for effect in self.__effects:
                    if effect[0]==curStat:
                        tmp+=effect[1]
        #TODO: Still gotta set tmp as the mod of curstat
        #Probably have to change stat get property to return 
        #whole tuple instead of just the sum. 
        #Change how iterating through stats so can
        #reference and modify current stat.


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
                base, mod, modified = self.stats.__dict__[stat]
                newMod = int(1 + random.random() * pool)
                pool = pool - newMod
                newMod = newMod + mod
                newStat = (base, newMod, base+newMod) 
                self.stats.__dict__[stat] = newStat

    def applyStats(self, stats):
        '''
        apply modifier to the stats of the character
        it is assumed that only the mod value of the incoming
        stats object will be used.
        '''
        for stat, val in stats:
            _,newMod,_ = val
            base, prevMod, modified = self.stats.__dict__[stat]
            newStat = (base, newMod,base+newMod)
            self.stats.__dict__[stat] = newStat
            

