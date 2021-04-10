from constants import *


class Stand:
    def __init__(self):
        self.checkers = []
        for i in range(ROWS):
            self.checkers.append([0, 0, 0, 0, 0, 0, 0])
