from tkinter import *
from CellularAutomaton import CellularAutomaton


class GridCanvas(Canvas):
    def __init__(self, master: Tk, rows, cols, grid, res=5):
        super().__init__(master, height=rows * res, width=cols * res, bg='white')
        self.height = rows * res
        self.width = cols * res
        self.rows = rows
        self.cols = cols
        self.res = res
        self.grid = grid
        self.colors = ['white', 'black', 'green', 'red', 'blue', 'pink']

    def update(self):
        super().update()
        self.delete(ALL)
        for i in range(self.cols):
            for j in range(self.rows):
                color = self.colors[self.grid[j][i]]
                #print(color)
                x1 = i * self.res
                y1 = j * self.res
                x2 = (i + 1) * self.res
                y2 = (j + 1) * self.res
                self.create_rectangle(x1, y1, x2, y2, fill=color)
        # checkered grid
        for i in range(self.cols):
            x = i * self.res
            self.create_line(x, 0, x, self.height, fill="#A9A9A9")
        for j in range(self.rows):
            y = j * self.res
            self.create_line(0, y, self.width, y, fill="#A9A9A9")
