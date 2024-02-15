from random import shuffle


class Cell():

    def __init__(self, around_mines, mine, fl_open: bool = False) -> None:
        self.around_mines = around_mines
        self.mine = mine  # True / False
        self.fl_open = fl_open


class GamePole:

    def __init__(self, N: int, M: int) -> None:
        """n - количество ячеек, m - кол-во бомб"""
        self.n = N
        self.m = M
        self.pole = []
        self.init()

    def is_mines_around(self, x, y):
        if x - 1 >= 0 and y - 1 >= 0 and x + 1 <= self.n - 1 and y + 1 <= self.n - 1:
            return self.pole[x - 1][y - 1: y + 2].count('*') + self.pole[x][y - 1].count('*') + self.pole[x][y + 1].count(
                '*') + self.pole[x + 1][
                       y - 1: y + 2].count(
                '*')
        # сверка границ:
        elif x == 0 and 1 <= y <= self.n - 2:
            return self.pole[x][y - 1].count('*') + self.pole[x][y + 1].count('*') + self.pole[x + 1][y - 1: y + 2].count(
                '*')
        elif x == self.n - 1 and 1 <= y <= self.n - 2:
            return self.pole[x - 1][y - 1: y + 2].count('*') + self.pole[x][y - 1].count('*') + self.pole[x][y + 1].count(
                '*')
        elif 1 <= x <= self.n - 2 and y == 0:
            return self.pole[x - 1][:2].count('*') + self.pole[x][y + 1].count('*') + self.pole[x + 1][:y + 2].count('*')
        elif 1 <= x <= self.n - 2 and y == self.n - 1:
            return self.pole[x - 1][self.n - 2:].count('*') + self.pole[x][self.n - 2].count('*') + \
                self.pole[x + 1][self.n - 2:].count('*')
        # сверка четырех углов:
        elif x == 0 and y == 0:
            return self.pole[x][y + 1].count('*') + self.pole[x + 1][:y + 2].count('*')
        elif x == 0 and y == self.n - 1:
            return self.pole[x][self.n - 2].count('*') + self.pole[x + 1][self.n - 2:].count('*')
        elif x == self.n - 1 and y == 0:
            return self.pole[x - 1][:2].count('*') + self.pole[x][1].count('*')
        elif x == self.n - 1 and y == self.n - 1:
            return self.pole[x - 1][self.n - 2:].count('*') + self.pole[x][self.n - 2].count('*')

    def show(self) -> None:
        for x in range(self.n):
            for y in range(self.n):
                if self.pole[x][y].mine:
                    print('*', end=' ') if y != self.n - 1 else print('* ', end='')
                else:
                    print(self.pole[x][y].around_mines, end=' ') if y != self.n - 1 else print(self.pole[x][y].around_mines, end='')
            print()

    def init(self):
        self.temp_lst = ['*' for _ in range(self.m)] + ['#' for _ in range(self.n * self.n - self.m)]
        shuffle(self.temp_lst)
        self.pole = [self.temp_lst[_: _ + self.n] for _ in range(0, self.n * self.n, self.n)]
        self.temp_lst.clear()
        self.pole = [
            [Cell(self.is_mines_around(x, y), self.pole[x][y] == '*') for y in range(self.n)] for x
            in
            range(self.n)]


pole_game = GamePole(10, 12)
pole_game.show()