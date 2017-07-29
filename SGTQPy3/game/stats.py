from lib import itermixin

    
# stats subclass for custom setter logic
# each stat is a triple representing 
# (base,modified,modifier)
# This will be easy to pull apart anytime
# info about a stat is needed. 
class Stats(itermixin.IterMixin):
    '''
    STATS:
        Health
        Armor
        Power
        Evasion
        Accuracy
        Speed
        Status
        Luck
        Resistance 

    '''

    def __init__(self):
        self.__health       = (0,0)
        self.__armor        = (0,0)
        self.__power        = (0,0)
        self.__evasion      = (0,0)
        self.__accuracy     = (0,0)
        self.__speed        = (0,0)
        self.__strength     = (0,0)
        self.__luck         = (0,0)
        self.__resistance   = (0,0)

    @property
    def health(self):
        return self.__health[0]+self.__health[1]
    @health.setter
    def health(self, val):
        try:
            self.__health = val  
        except ValueError:
            pass

    @property
    def armor(self):
        return self.__armor[0]+self.__armor[1]
    @health.setter
    def armor(self, val):
        try:
            self.__armor=val
        except ValueError:
            pass

    @property
    def power(self):
        return self.__power[0]+self.__power[1]
    @power.setter
    def power(self, val):
        try:
            self.__power = val 
        except ValueError:
            pass

    @property
    def evasion(self):
        return self.__evasion[0]+self.__evasion[1]
    @evasion.setter
    def evasion(self, val):
        try:
            self.__evasion = val
        except ValueError:
            pass

    @property
    def accuracy(self):
        return self.__accuracy[0]+self.__accuracy[1]
    @accuracy.setter
    def accuracy(self, val):
        try:
            self.__accuracy=val
        except ValueError:
            pass

    @property
    def speed(self):
        return self.__speed[0]+ self.__speed[1]
    @speed.setter
    def speed(self, val):
        try:
         self.__speed=val
        except ValueError:
            pass

    @property
    def strength(self):
        return self.__strength[0]+self.__strength[1]
    @strength.setter
    def strength(self, val):
        try:
            self.__strength=val
        except ValueError:
            pass

    @property
    def luck(self):
        return self.__luck[0]+ self.__luck[1]
    @luck.setter
    def luck(self, val):
        try:
             self.__luck=val
        except ValueError:
            pass

    @property
    def resistance(self):
        return self.__resistance[0]+self.__resistance[1]
    @resistance.setter
    def resistance(self, val):
        try:
            self.__resistance=val
        except ValueError:
            pass

    def getallstats(self):
        '''
        returns a dicitonary of the stats
        '''
        return None


