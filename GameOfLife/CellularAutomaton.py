from Rules import Rules
from RuleApplication import RuleApplication
import numpy as np
import random


class CellularAutomaton:
    def __init__(self, rows: int, cols: int, res: int):
        self.rows = rows
        self.cols = cols
        self.res = res
        self.is_stagnating = False
        self.cells = np.empty([self.rows, self.cols], dtype=int)
        self.generation = 0

    def print_values(self):
        print("Rows: ", self.rows, "Cols:", self.cols)
        print("Cells:")
        for i in range(self.rows):
            print(self.cells[i])

    def print_cells(self):
        for i in range(self.rows):
            print(self.cells[i])

    def print_generation(self):
        print("Current Generation: ", self.generation)

    def fill_cells(self, cells: [[int]] = None, ratio: int = 0.5):
        # fill with given cells
        if cells is not None:
            self.cells = cells
            return
        # fill randomly
        self.cells = np.around(np.random.rand(self.rows, self.cols)).astype(int)

    def update_cells(self, rule: Rules = Rules.GAME_OF_LIFE, rule_idx=0, offset=(1, 0), carry_over=True):
        new_cells = RuleApplication.apply_rule(self, rule, rule_idx=rule_idx, offset=offset, carry_over=carry_over)
        if self.check_stagnating(new_cells):
            self.is_stagnating = True
            print(f"Final Position reached after {self.generation} generations.")
        else:
            self.is_stagnating = False
            self.cells = new_cells
            self.generation += 1

    def check_stagnating(self, new_cells: [[int]]):
        return (self.cells == new_cells).all()

    def get_live_neighbors(self, center_row: int, center_col: int):
        #TODO make this numpy
        neighbors = 0
        for i in range(-1, 2):
            if center_row + i < 0 or center_row + i >= self.rows:
                continue
            for j in range(-1, 2):
                if center_col + j < 0 or center_col + j >= self.cols:
                    continue
                neighbors += self.cells[center_row + i][center_col + j]
        return neighbors
