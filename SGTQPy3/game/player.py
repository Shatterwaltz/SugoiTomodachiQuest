from game import character

class Player:
    '''
    Class that holds all info relevant to a player.
    Their Discord username, their character and such.
    '''
    def __init__(self, name):
        self.name = name
        self.__pcharacter = None

    @property
    def pcharacter(self):
        return self.__pcharacter

    @pcharacter.setter
    def pcharacter(self, val):
        valid = True
        if type(val) is not character.Character:
            valid = False
        if valid:
            self.__pcharacter = val
