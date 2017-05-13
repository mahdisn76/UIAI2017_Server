from src.Pos import Pos
from src.Checker import Checker

class Cell:
    def __init__(self, x, y, c):
        self.__pos = Pos(x, y)
        self.__checker = 0
        if c != 'e':
            self.__checker = Checker(x, y, c)

    def __init__(self):
        self.__pos = Pos(0, 0)
        self.__checker = 0

    def get_checker(self):
        return self.__checker

    def get_pos(self):
        return self.__pos

    def set_pos(self, newPos):
        self.__pos = newPos

    def set_checker(self, newChecker):
        self.__checker = newChecker
