from Rules import Rules
from RuleApplication import RuleApplication
import numpy as np
import random


class CellularAutomaton:
    def __init__(self, rows: int, cols: int, elementary=False):
        self.rows = rows
        self.cols = cols
        self.is_stagnating = False
        self.is_elementary = elementary
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

    def set_cells(self, cells: [[int]] = None):
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

    def copy(self):
        copy = CellularAutomaton(self.rows, self.cols, elementary=self.is_elementary)
        copy.set_cells(self.cells)
        return copy

    def become_stagnant(self, rule: Rules):
        while not self.is_stagnating:
            self.update_cells(rule)

    def check_stagnating(self, new_cells: [[int]]):
        if self.is_elementary:
            return np.array_equal(self.cells[self.rows - 1], new_cells[self.rows - 1])
        return np.array_equal(self.cells, new_cells)

    def get_live_neighbors(self, center_row: int, center_col: int):
        row_neg_off = -1 + (center_row == 0)
        row_pos_off = 1 + (center_row != self.rows - 1)
        col_neg_off = -1 + (center_col == 0)
        col_pos_off = 1 + (center_col != self.cols - 1)
        return np.sum(self.cells[center_row + row_neg_off:center_row + row_pos_off,
                     center_col + col_neg_off:center_col + col_pos_off]) - self.cells[center_row, center_col]

    def get_row_neighbors(self, center_row: int, center_col: int):
        pattern = ''
        for j in range(-1, 2):
            if center_col + j < 0 or center_col + j >= self.cols:
                pattern += '0'
                continue
            pattern += str(int(self.cells[center_row][center_col + j]))
        return pattern
