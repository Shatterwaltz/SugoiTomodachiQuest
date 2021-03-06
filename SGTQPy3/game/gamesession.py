import uuid
from game import player
from copy import deepcopy

class GameSession:
    '''
    GameSession is a class to house data relevant to a given game session.
    It is essentially a game state object, with some other data that is relevant to the
    networked nature of the SugoiTomodachiQuest game.
    '''

    def __init__(self, config):
        self.__players = {}                 # hold the player objects, lookup by username
        self.age = 0                        # the lifetime of this game session
        self.__sid = uuid.uuid4()           # the uid of this game session
        self.map = None                     # the map of the current game
        self.mobs = []                      # list of mobs present in the game
        self.deepest = 0                    # the furthest level down in the game
        self.floors = 0                     # the current number of floors in the game
        self.__config = config              # the object representing the games config file
        self.__highscoreplayer = (None,0)   # the player with the highscore and the score

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, val):
        valid = True
        for p in val:
            if type(p) is not player.Player:
                valid = False
        if valid:
            self.__players = val

    def addplayer(self, p):
        if type(p) is player.Player:
            self.__players[p.name] = p

    @property
    def highscoreplayer(self):
        return self.__highscoreplayer

    @highscoreplayer.setter
    def highscoreplayer(self, val):
        valid = True
        if type(val) is not tuple:
            valid = False
        else:
            x,y = val
            if type(x) is not player.Player or type(y) is not int:
                valid = False
        if valid:
            self.__highscoreplayer = val

    @property
    def config(self):
        # return only a copy of the config
        # so that it is read only?
        return deepcopy(self.__config)

    @property
    def sid(self):
        return self.__sid

    @sid.setter
    def sid(self, val):
        if type(val) is uuid.uuid4:
            self.__sid = val

