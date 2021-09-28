from tkinter import *
from GameOfLife import GameOfLife


class GameOfLifeCanvas(Canvas):
    def __init__(self, master: Tk, game: GameOfLife):
        super().__init__(master, height=game.rows * game.res, width=game.cols * game.res, bg='white')
        self.height = game.rows * game.res
        self.width = game.cols * game.res
        self.game = game

    def update(self):
        super().update()
        self.delete(ALL)
        # cells
        for i in range(self.game.rows):
            for j in range(self.game.cols):
                x1 = i * self.game.res
                y1 = j * self.game.res
                x2 = (i + 1) * self.game.res
                y2 = (j + 1) * self.game.res
                self.create_rectangle(x1, y1, x2, y2,
                                      fill="black" if self.game.cells[i][j] == 1 else "white")
        # checkered grid
        for i in range(self.game.cols):
            x = i * self.game.res
            self.create_line(x, 0, x, self.height, fill="#A9A9A9")
        for j in range(self.game.rows):
            y = j * self.game.res
            self.create_line(0, y, self.width, y, fill="#A9A9A9")
