from Rules import Rules
from RuleApplication import RuleApplication
import numpy as np
import random


class GameOfLife:
    def __init__(self, length: int, height: int, res: int):
        self.rows = int(height / res)
        self.cols = int(length / res)
        self.res = res
        self.cells = np.empty([self.rows, self.cols], dtype=int)
        self.is_over = False

    def print_values(self):
        print("Rows: ", self.rows, "Cols:", self.cols)
        print("Cells:")
        for i in range(self.rows):
            print(self.cells[i])

    def print_cells(self):
        for i in range(self.rows):
            print(self.cells[i])

    def fill_cells(self, cells: [[int]] = None, ratio: int = 0.5):
        # fill with given cells
        if cells is not None:
            self.cells = cells
            return
        # fill randomly
        self.cells = np.around(np.random.rand(self.rows, self.cols)).astype(int)

    def update_cells(self, rule: Rules = Rules.CLASSIC):
        self.cells = RuleApplication.apply_rule(self, rule)

    def check_game_over(self, new_cells: [[int]]):
        return (self.cells == new_cells).all()

    def get_live_neighbors(self, center_row: int, center_col: int):
        neighbors = 0
        for i in range(-1, 2):
            if center_row + i < 0 or center_row + i >= self.rows:
                continue
            for j in range(-1, 2):
                if center_col + j < 0 or center_col + j >= self.cols or (i == 0 and j == 0):
                    continue
                neighbors += self.cells[center_row + i][center_col + j]
        return neighbors
