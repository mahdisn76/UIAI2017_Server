from socket import *
import thread
from Game import Game


if __name__ == '__main__':
    game = Game("eeeeeeeeeeeeeeeeeeeeeeee")
    if (game.start_server()):
        game.start()