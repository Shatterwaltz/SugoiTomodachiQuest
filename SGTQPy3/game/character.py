from lib import itermixin

class Character(itermixin.IterMixin):
    '''
    Character class, NPCs, players, and mobs inherit this class
    
    STATS:
        Health:     HP
        Armor:      AR
        Power:      PW
        Evasion:    EV
        Accuracy:   AC
        Speed:      SP
        Status:     ST
        Luck:       LK

    '''

    # stats subclass for custom setter logic
    # each stat is a triple representing 
    # (base,modified,modifier)
    # This will be easy to pull apart anytime
    # info about a stat is needed. 
    class Stats(itermixin.IterMixin):
        def __init__(self):
            self.__health       = (0,0,0)
            self.__armor        = (0,0,0)
            self.__power        = (0,0,0)
            self.__evasion      = (0,0,0)
            self.__accuracy     = (0,0,0)
            self.__speed        = (0,0,0)
            self.__strength     = (0,0,0)
            self.__luck         = (0,0,0)
            self.__resitance    = (0,0,0)

        @property
        def health(self):
            return self.__health
        @health.setter
        def health(self, val):
            try:
                self.__health = int(val)
            except ValueError:
                pass

        @property
        def armor(self):
            return self.__health
        @health.setter
        def armor(self, val):
            try:
                self.__health = int(val)
            except ValueError:
                pass

        @property
        def power(self):
            return self.__power
        @power.setter
        def power(self, val):
            try:
                self.__power = int(val)
            except ValueError:
                pass

        @property
        def evasion(self):
            return self.__evasion
        @evasion.setter
        def evasion(self, val):
            try:
                self.__evasion = int(val)
            except ValueError:
                pass

        @property
        def accuracy(self):
            return self.__accuracy
        @accuracy.setter
        def accuracy(self, val):
            try:
                self.__accuracy = int(val)
            except ValueError:
                pass

        @property
        def speed(self):
            return self.__speed
        @speed.setter
        def speed(self, val):
            try:
                self.__speed = int(val)
            except ValueError:
                pass

        @property
        def strength(self):
            return self.__strength
        @strength.setter
        def strength(self, val):
            try:
                self.__strength = int(val)
            except ValueError:
                pass

        @property
        def luck(self):
            return self.__luck
        @luck.setter
        def luck(self, val):
            try:
                self.__luck = int(val)
            except ValueError:
                pass

        def getallstats(self):
            return None

    
    def __init__(self, desc, ctype, did):	
        self.name = ''
        self.desc = ''
        self.ctype = '' # the type of character this is
        self.did = 0 #discord id, 0 is for non player characters
        self.pos = (0,0) # map room position
        self.awake = False
        self.__stats = self.Stats()
        
    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, val):
        if val is self.Stats:
            self.__state = val
        else:
            pass

