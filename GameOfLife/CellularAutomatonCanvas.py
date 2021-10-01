from tkinter import *
from CellularAutomaton import CellularAutomaton


class CellularAutomatonCanvas(Canvas):
    def __init__(self, master: Tk, automaton: CellularAutomaton, res=5):
        super().__init__(master, height=automaton.rows * res, width=automaton.cols * res, bg='white')
        self.height = automaton.rows * res
        self.width = automaton.cols * res
        self.res = res
        self.automaton = automaton

    def update(self):
        super().update()
        self.delete(ALL)
        # cells
        for i in range(self.automaton.cols):
            for j in range(self.automaton.rows):
                x1 = i * self.res
                y1 = j * self.res
                x2 = (i + 1) * self.res
                y2 = (j + 1) * self.res
                self.create_rectangle(x1, y1, x2, y2,
                                      fill="black" if self.automaton.cells[j][i] == 1 else "white")
        # checkered grid
        for i in range(self.automaton.cols):
            x = i * self.res
            self.create_line(x, 0, x, self.height, fill="#A9A9A9")
        for j in range(self.automaton.rows):
            y = j * self.res
            self.create_line(0, y, self.width, y, fill="#A9A9A9")
