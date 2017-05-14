from src.Board import Board
from socket import *
import thread


def simplelinesplit(sock):
    data = ""
    try:
        while True:
            data += sock.recv(1)
            if len(data) > 0 and data[-1] == '\n':
                break
    except:
        pass
    finally:
        return data


class Game:
    cycle_count = 100
    BUFF = 1024
    HOST = '127.0.0.1'  # must be input parameter @TODO
    PORT = 9999  # must be input parameter @TODO


    def __init__(self,s, port=9999):
        self.board = Board(s)
        self.round = 0
        self.current_player = 0
        self.players = [None, None]

    def parse_command(self, command_str):
        try:
            command, param = command_str.split(' ')
            c = command[0]
            param2 = None
            if len(command >=3):
                i,j = command[2].split(',')
                param2 = (i,j)

            if c == 'put':
                i1,j1 = command[1].split(',')

                return c,(int(i1),int(j1)), param2
            elif c == 'mov':
                i1,j1,i2,j2 = command[1].split(',')
                return c,(int(i1),int(j1),int(i2),int(j2)), param2
        except:
            raise Exception("Invalid Command")


    def send_board(self):
        ret = ['e' if item == None else 'm' if item == self.players[self.current_player] else 'o' for item in self.board]
        self.players[self.current_player]["sock"].send(str(self.board) + '\n')

    def start_server(self):
        ADDR = (self.HOST, self.PORT)
        serversock = socket(AF_INET, SOCK_STREAM)
        serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serversock.bind(ADDR)
        serversock.listen(5)
        while 1:
            print 'waiting for Player...'
            clientsock, addr = serversock.accept()
            print '...connected from:', addr
            # try:
            data = simplelinesplit(clientsock)
            data = data.replace('\n', '').replace('\r', '')
            cmd, name = data.split(' ')
            if cmd != "REGISTER":
                raise Exception("INVALID COMMAND")

            self.players[self.current_player] = {"name": name, "inhand": 12, 'sock': clientsock, 'index': self.current_player}
            self.current_player +=1

            if self.current_player >= 2:
                print "%s and %s joned. ready to start" % (self.players[0],self.players[1])
                return True
            # except:
            #     raise Exception(" Cannot Register")





    def start(self):
        self.current_player = 0
        for self.round in range(1,self.cycle_count):
            self.send_board()
            command_str = simplelinesplit(self.players[self.current_player]["sock"])
            command, param1, param2 = self.parse_command(command_str)
            dest = self.board.update(command=command, param1=param1, player=self.player)
            if self.board.is_line(dest):
                try:
                    if self.players[(self.current_player + 1) % 2]["inhand"] > 0:
                        self.players[(self.current_player + 1) % 2]["inhand"] -= 1
                    else:
                        x = param2[0]
                        y = param2[1]
                        if self.board.cells[(x,y)].get_checker() == self.players[(self.current_player + 1) % 2]:
                            self.board.cells[(x, y)].set_checker(None)
                except:
                    self.board.random_pop(self.players[(self.current_player + 1) % 2])


            self.current_player = (self.current_player + 1) % 2

