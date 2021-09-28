from Rules import Rules
import random


class GameOfLife:
    def __init__(self, lenght: int, height: int, res: int):
        self.rows = int(height / res)
        self.cols = int(lenght / res)
        self.res = res
        self.cells = [[0 for j in range(self.cols)] for i in range(self.rows)]
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
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j] = int(random.random() > ratio)

    def update_cells(self, rule: Rules = Rules.CLASSIC):
        if rule == Rules.CLASSIC:
            new_cells = self.apply_classic_rules()
        #self.is_over = self.check_game_over(new_cells)
        self.cells = new_cells

    def check_game_over(self, new_cells: [[int]]):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j] != new_cells[i][j]:
                    return False
        return True

    def apply_classic_rules(self):
        new_cells = [[0 for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                live_neighbors = self.get_live_neighbors(i, j)
                print("Cell ", i ,",",j , " ", live_neighbors, "Alive: ", self.cells[i][j])
                if self.cells[i][j] == 1:
                    # Rule 1, 3: Alive cell with >3 or <2 neighbors dies
                    if live_neighbors > 3 or live_neighbors < 2:
                        print("Dies")
                        new_cells[i][j] = 0
                        continue
                    # Rule 2: Alive cell with 2 or 3 neighbors stays alive
                    print("Lives")
                    new_cells[i][j] = 1
                # Rule 4: Dead cells with 3 alive neighbors becomes alive
                elif live_neighbors == 3:
                    print("Revive")
                    new_cells[i][j] = 1
                else:
                    print("Stays dead")
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
