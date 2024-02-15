"""Implementation of Saper game"""

import random

class Cell:
    """
    This class represents a cell of the playing field
    """

    def __init__(self, mine:bool=False, around_mines:int=0, fl_open:bool=False):
        """
        Initialize a cell of the playing field
        :param around_mines: number of mines around the cell
        (initional value is 0)
        :param mine: is this cell a mine(True/False)
        :param: fl_open: Is the cell open(True/False).
        All cells are closed at the beginning of the game(False)
        """

        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    """
    A class for managing the playing field
    """

    def change_around_mines_value(self) -> None:
        """
        Changes around_mines attribute
        of the Cell's instances
        """
        for row_ind, row in enumerate(self.pole):
            for cell_ind, cell in enumerate(row):
                cell.around_mines = self.around_mines_func(row_ind, cell_ind)


    def __init__(self, N:int, M:int):
        """
        Creates a new playing field with size N by N cells
        Создаёт новое игровое поле размером N x N клеток.
        :param N: length of one playing field's side
        :param M: total number of mines
        """
        self.N = N
        self.M = M
        self.pole = self.init()
        # add right_coord and left_coord
        self.change_around_mines_value()


    def init(self):
        """
        Creates a playing field with
        a new arrangement of self.M mines randomly
        """

        mines_coords = self.create_mins()
        # Cell(row, col) in mines_coords returns True/False
        pole = [[Cell((row, col) in mines_coords, 0) for col in range(self.N)] for row in range(self.N)]

        return pole


    def show(self, pole) -> None:
        """
        Displays a playing field in the form
        of a table of numbers of open cells
        in the console.
        It displays '#' if a cell is not opened
        """
        for row in pole:
            for cell in row:
                print(('#', cell.around_mines)[cell.fl_open], end=' ')
            print()


    def create_mins(self) -> tuple:
        """
        Creates a tuple with
        mines coordinates
        """
        mines = []
        coords = list(range(self.N))
        M = self.M
        while M:
            mine = (random.choice(coords), random.choice(coords))
            if mine not in mines:
                mines.append(mine)
                M -= 1

        return tuple(mines)


    def around_mines_func(self, right_coord:int, left_coord:int) -> int:
        """
        Returns number of mines around the mine.
        :param right_coord: index of pole's row
        :param left_coord: index of pole's column

        pole's elements we need to check:
        a b c
        d e f
        g h i

        a - (right_coord - 1, left_coord - 1)
        b - (right_coord - 1, left_coord)
        c - (right_coord - 1, left_coord + 1)
        d - (right_coord, left_coord - 1)
        e - (right_coord, left_coord)
        f - (right_coord, left_coord + 1)
        g - (right_coord + 1, left_coord - 1)
        h - (right_coord + 1, left_coord)
        i - (right_coord + 1, left_coord + 1)
        """

        mines_number = 0  # number of mines around the cell
        valid_indexes = range(self.N)
        coords = (
            (right_coord - 1, left_coord - 1),
            (right_coord - 1, left_coord),
            (right_coord - 1, left_coord + 1),
            (right_coord, left_coord - 1),
            (right_coord, left_coord + 1),
            (right_coord + 1, left_coord - 1),
            (right_coord + 1, left_coord),
            (right_coord + 1, left_coord + 1)
        )

        for r_coord, l_coord in coords:
            if r_coord in valid_indexes and l_coord in valid_indexes:
                mines_number += self.pole[r_coord][l_coord].mine

        return mines_number


pole_game = GamePole(10, 12)
pole_game.show()