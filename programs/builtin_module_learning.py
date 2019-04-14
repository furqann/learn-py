#  Exercise for using builtin module of python
import random


class Dice:

    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


board_game = Dice()
print(board_game.roll())