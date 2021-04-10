from constants import *
from stand import Stand


def draw_tie():
    pass


class Game:
    def __init__(self):
        self.turn_col = 1  # 1 is black, 2 is red
        self.stand = Stand()
        self.turn_num = 1
        self.finished = False

    def change_turn(self):
        if self.turn_col == 1:
            self.turn_col = 2
        else:
            self.turn_col = 1

    def check_next_open(self, col):
        col = int(col)
        stand = self.stand
        result = 0
        for row in range(ROWS):
            if stand.checkers[row][col] == 0:
                result = row
            else:
                if result == 0 and stand.checkers[0][col] != 0:
                    return -1
        return result

    def check_same_color(self, row, col):
        if self.stand.checkers[row][col] != self.turn_col:
            return False
        else:
            return True

    def check_win_straight(self, row, col):
        left = col - 1
        up = row - 1
        right = col + 1
        down = row + 1
        horizontal = vertical = 1
        while left >= 0:
            if self.check_same_color(row, left):
                horizontal += 1
                left -= 1
            else:
                break
        while right <= 6:
            if self.check_same_color(row, right):
                horizontal += 1
                right += 1
            else:
                break
        while up >= 0:
            if self.check_same_color(up, col):
                vertical -= 1
                up -= 1
            else:
                break
        while down <= 5:
            if self.check_same_color(down, col):
                vertical += 1
                down += 1
            else:
                break
        if horizontal >= 4 or vertical >= 4:
            return True

    def check_win_diagonal(self, row, col):
        diagonal0 = diagonal1 = 1
        left = col - 1
        up = row - 1
        right = col + 1
        down = row + 1

        while left >= 0 and up >= 0:
            if self.check_same_color(up, left):
                diagonal0 += 1
                left -= 1
                up -= 1
            else:
                break

        while right <= 6 and down <= 5:
            if self.check_same_color(down, right):
                diagonal0 += 1
                right += 1
                down += 1
            else:
                break

        left = col - 1
        up = row - 1
        right = col + 1
        down = row + 1

        while right <= 6 and up >= 0:
            if self.check_same_color(up, right):
                diagonal1 += 1
                right += 1
                up -= 1
            else:
                break

        while left >= 0 and down <= 5:
            if self.check_same_color(down, left):
                diagonal1 += 1
                left -= 1
                down += 1
            else:
                break
        if diagonal0 >= 4 or diagonal1 >= 4:
            return True

    def check_win(self, row, col):
        if self.check_win_straight(row, col) or self.check_win_diagonal(row, col):
            return True
        return False

    def drop_checkers(self, pos):
        x, y = pos
        if SIDE_SPACE < x < WIDTH - SIDE_SPACE:
            col = ((x - SIDE_SPACE) // SECTION_WIDTH)
            row = self.check_next_open(col)
            if row != -1:
                self.stand.checkers[row][int(col)] = self.turn_col
                self.turn_num += 1
                if self.turn_num > 42:
                    return True
                elif self.turn_num >= 7 and self.check_win(row, int(col)):
                    return True
                else:
                    self.change_turn()
        return False

    def reset(self):
        self.turn_col = 1
        self.turn_num = 1
        self.stand.checkers = []
        self.finished = False
        for i in range(ROWS):
            self.stand.checkers.append([0, 0, 0, 0, 0, 0, 0])
