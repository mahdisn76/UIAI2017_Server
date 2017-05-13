from src.Cell import Cell
from src.Checker import Checker
from random import randint

def command_validate(command):
    return True


class Board:
    def __init__(self, s):
        self.cells = []
        self.player1_cells = []
        self.player2_cells = []
        self.emptyCells = []
        for i in range(0, 8):
            for j in range(0, 3):
                tmp = Cell(i, j, 'e')
                self.cells.append(tmp)
                self.emptyCells.append(tmp)

    def get_neigbors(self, x, y):
        self.__neigbors = []
        if y < 2:
            self.__neigbors.append(self.__cells[x][y + 1])
        if y > 0:
            self.__neigbors.append(self.__cells[x][y - 1])
        self.__neigbors.append(self.__cells[(x + 1) % 8][y])
        self.__neigbors.append(self.__cells[(x - 1 + 8) % 8][y])
        return self.__neigbors

    def get_lines(self, x, y):
        self.__ans = []
        self.__tmp = []
        for i in range(0, 3):
            self.__tmp.append(self.__cells[x][i])
            self.__ans.append(self.__tmp)
        self.__tmp.clear()
        if x % 2 == 1 :
            self.__tmp.append(self.__cells[x-1][y])
            self.__tmp.append(self.__cells[(x + 1) % 8][y])
            self.__tmp.append(self.__cells[x][y])
        else:
            for i in range(0, 3):
                self.__tmp.append(self.__cells[(x + i) % 8][y])
            self.__ans.append(self.__tmp)
            self.__tmp.clear()

            for i in range(0, 3):
                self.__tmp.append(self.__cells[(x - i + 8) % 8][y])
            self.__ans.append(self.__tmp)
            self.__tmp.clear()

        return self.__ans


    def random_work(self,player):
        if player.inhandcheckernumber > 0:
            index = randint(0, self.emptyCells.count())
            self.emptyCells[index].set_checker()


    def update(self,command,player):
        if not command_validate(command):
            print("wrong command")
            self.random_work()
            return
        if command.substring(0,2) == "pu": #__________________push___________________
            x = 0 #take out from command
            y = 0 #take out from command

            if player.inhandcheckernumber == 0 or self.cells[x][y].get_checker() != 0:
                print("wrong command")
                self.random_work()
                return

            self.cells[x][y].set_checker(Checker(x, y, player))
            self.emptyCells.remove(self.cells[x][y])



        elif command.substring(0, 2) == "mo": #move
            x1 = 0  #source point            # take out from command string
            y1 = 0
            x2 = 0  #dest point
            y2 = 0

            if self.get_neigbors(x1, y1).__contains__(self.cells[x2][y2]) and self.cells[x1][y1].get_checker() != 0 and self.cells[x1][y1].get_checker().get_owner() == player and self.cells[x2][y2].get_checker() == 0:
                self.cells[x1][y1].set_checker(Checker(x2, y2, player))

            else:
                self.random_work()
                print("wrong command")

