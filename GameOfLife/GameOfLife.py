from Rules import Rules
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
        if rule == Rules.CLASSIC:
            new_cells = self.apply_classic_rules()
        if rule == Rules.DOWNROLL:
            new_cells = self.apply_downroll_rules()
        if rule == Rules.SIDEROLL:
            new_cells = self.apply_sideroll_rules()
        #self.is_over = self.check_game_over(new_cells)
        self.cells = new_cells

    def check_game_over(self, new_cells: [[int]]):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j] != new_cells[i][j]:
                    return False
        return True

    def apply_classic_rules(self):
        new_cells = np.empty([self.rows, self.cols])
        for i in range(self.rows):
            for j in range(self.cols):
                live_neighbors = self.get_live_neighbors(i, j)
                if self.cells[i][j] == 1:
                    # Rule 1, 3: Alive cell with >3 or <2 neighbors dies
                    if live_neighbors > 3 or live_neighbors < 2:
                        new_cells[i][j] = 0
                        continue
                    # Rule 2: Alive cell with 2 or 3 neighbors stays alive
                    new_cells[i][j] = 1
                # Rule 4: Dead cells with 3 alive neighbors becomes alive
                elif live_neighbors == 3:
                    new_cells[i][j] = 1
        return new_cells

    def apply_downroll_rules(self):
        new_cells = np.empty([self.rows, self.cols])
        for i in range(self.rows):
            for j in range(self.cols):
                new_cells[i][(j + 1) % self.cols] = self.cells[i][j]
        return new_cells

    def apply_sideroll_rules(self):
        new_cells = np.empty([self.rows, self.cols])
        for i in range(self.rows):
            for j in range(self.cols):
                new_cells[(i + 1) % self.rows][j] = self.cells[i][j]
        return new_cells

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
