import numpy as np


class GridContainer:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.cells = np.empty([self.rows, self.cols], dtype=int)

    def print_values(self):
        print("Rows: ", self.rows, "Cols:", self.cols)

    def print_cells(self):
        print("[")
        for i in range(self.rows):
            print("[", end="")
            for j in range(self.cols):
                print(self.cells[i][j], end="", sep="")
                if j < self.cols - 1:
                    print(", ", end="")
            print("]", end="")
            if j < self.cols - 1:
                print(",")
        print("\n]")

    def get_neighbors(self, row, col):
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if row < self.rows - 1:
            neighbors.append((row + 1, col))
        if col < self.cols - 1:
            neighbors.append((row, col + 1))
        return neighbors