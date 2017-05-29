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
        self.__health       = (0,0,0)
        self.__armor        = (0,0,0)
        self.__power        = (0,0,0)
        self.__evasion      = (0,0,0)
        self.__accuracy     = (0,0,0)
        self.__speed        = (0,0,0)
        self.__strength     = (0,0,0)
        self.__luck         = (0,0,0)
        self.__resistance   = (0,0,0)

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, val):
        try:
            base, mod = val
            self.__health = (base, mod, base+mod)  
        except ValueError:
            pass

    @property
    def armor(self):
        return self.__armor
    @health.setter
    def armor(self, val):
        try:
            base, mod = val
            self.__armor = (base, mod, base+mod) 
        except ValueError:
            pass

    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, val):
        try:
            base, mod = val
            self.__power = (base, mod, base+mod) 
        except ValueError:
            pass

    @property
    def evasion(self):
        return self.__evasion
    @evasion.setter
    def evasion(self, val):
        try:
            base, mod = val
            self.__evasion = (base, mod, base+mod)
        except ValueError:
            pass

    @property
    def accuracy(self):
        return self.__accuracy
    @accuracy.setter
    def accuracy(self, val):
        try:
            base, mod = val
            self.__accuracy = (base, mod, base+mod)
        except ValueError:
            pass

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, val):
        try:
            base, mod = val
            self.__speed = (base, mod, base+mod)
        except ValueError:
            pass

    @property
    def strength(self):
        return self.__strength
    @strength.setter
    def strength(self, val):
        try:
            base, mod = val
            self.__strength = (base, mod, base+mod)
        except ValueError:
            pass

    @property
    def luck(self):
        return self.__luck
    @luck.setter
    def luck(self, val):
        try:
            base, mod = val
            self.__luck = (base, mod, base+mod)
        except ValueError:
            pass

    @property
    def resistance(self):
        return self.__resistance
    @resistance.setter
    def resistance(self, val):
        base, mod = val
        self.__resistance = (base, mod, base+mod)

    def getallstats(self):
        '''
        returns a dicitonary of the stats
        '''
        return None

