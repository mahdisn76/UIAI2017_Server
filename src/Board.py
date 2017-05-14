from src.Cell import Cell
# from src.Checker import Checker
from random import randint

def command_validate(command):
    return True


class Board:
    def __init__(self, s):
        self.cells = {}
        self.player1_cells = []
        self.player2_cells = []
        # self.emptyCells = {}
        for i in range(0, 8):
            for j in range(0, 3):
                tmp = Cell(i, j)
                self.cells[(i,j)] = tmp
                # self.emptyCells[(i,j)]= tmp


    def __str__(self):
        l = []
        for i in range(0,3):
            for j in range(0,8):
                l.append(self.cells[(j,i)])
        return str(l)

    def get_neigbors(self, cell):
        if cell.neigbors:
            return cell.neigbors
        cell.neigbors = []
        y = cell.get_pos().gety()
        x = cell.get_pos().getx()
        if y < 2:
            cell.neigbors.append(self.cells[(x,y + 1)])
        elif y > 0:
            cell.neigbors.append(self.cells[(x,y - 1)])
        cell.neigbors.append(self.cells[((x + 1) % 8,y)])
        cell.neigbors.append(self.cells[((x - 1) % 8,y)])
        return cell.neigbors

    def is_line(self, cell):
        y = cell.get_pos().gety()
        x = cell.get_pos().getx()
        if self.cells[(x,0)].get_checker() == self.cells[(x,1)].get_checker() and self.cells[(x,0)].get_checker() == self.cells[(x,2)].get_checker():
            return True

        for i in range((x-2) % 8, x+1):
            if self.cells[(i, y)].get_checker() == self.cells[(i+1, y)].get_checker() and self.cells[
                (i, y)].get_checker() == self.cells[(i+2, y)].get_checker():
                return True
        return False

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
        pass
        # if player.inhandcheckernumber > 0:
        #     index = randint(0, self.emptyCells.count())
        #     self.emptyCells[index].set_checker()
    def random_pop(self,player):
        pass

    def update(self,command, param1, param2, player):
        dest = None
        try:
            if not command_validate(command, param1, param2):
                raise ("wrong command")
            if command == "put": #__________________push___________________
                x = param1[0]
                y = param1[1]

                if player["inhand"] == 0 or self.cells[(x,y)].get_checker() is not None:
                    raise ("wrong command")
                else:
                    self.cells[(x,y)].set_checker(player)
                    dest = self.cells[(x,y)]
                # del self.emptyCells[x,y]



            elif command == "mov": #move
                x1 = param1[0]
                y1 = param1[1]
                x2 = param1[2]
                y2 = param1[3]

                if (x2,y2) in self.get_neigbors(self.cells[(x1, y1)]) and \
                        self.cells[(x1, y1)].get_checker() == player and \
                        self.cells[(x1, y1)].get_checker() is None:
                    self.cells[(x1, y1)].set_checker(None)
                    self.cells[(x2, y2)].set_checker(player)
                    dest = self.cells[(x1, y1)]
                else:
                    raise ("wrong command")
        except Exception as e:
            print(e.message)
            dest = self.random_work()

        return dest




