import numpy as np
from CellularAutomata.model.CellularAutomaton.CellularAutomataModel import CellularAutomaton
from CellularAutomata.util.initialization.Initializer import Initializer
from CellularAutomata.util.rules.Rules import Rules
from CellularAutomata.util.filling.RegionFiller import RegionFiller
from CellularAutomata.util.filling.FloodFill import flood_fill
import random


class Maze:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.start = (0, 0)
        self.goal = (0, 0)
        self.cells = np.empty([self.rows, self.cols], dtype=int)
        self.reachable = None

    def print_values(self):
        print("Rows: ", self.rows, "Cols:", self.cols)
        print(f"Start: {self.start}", f"Goal: {self.goal}")

    def print_cells(self):
        for i in range(self.rows):
            print("[", end="")
            for j in range(self.cols):
                print(self.cells[i][j], end="", sep="")
                if j < self.cols - 1:
                    print(", ", end="")
            print("],")

    def initialize(self, cells=None):
        if cells is not None:
            self.cells = np.array(cells)
            for row in range(self.cells.shape[0]):
                for col in range(self.cells.shape[1]):
                    if self.cells[row][col] == 2:
                        self.start = (row, col)
                    if self.cells[row][col] == 3:
                        self.goal = (row, col)
            return
        # Initialize with CA and Flood Fill
        ca = CellularAutomaton(self.rows, self.cols)
        ca.set_cells(Initializer.initialize_random(ca))
        # Fill CA with Majority rule as estimate of the map
        ca.become_stagnant(Rules.MAJORITY)
        # Fill all unreachable spots
        self.reachable = flood_fill(ca.cells, 0, 0)
        self.cells = RegionFiller.fill_region(ca.cells, 0, 0, flood_c=self.reachable)

    def initialize_start_goal(self):
        assert self.reachable is not None
        self.start = random.choice(self.reachable)
        self.goal = random.choice(self.reachable)
        self.cells[self.start[1]][self.start[0]] = 2
        self.cells[self.goal[1]][self.goal[0]] = 3

    def set_start(self, x, y):
        self.start = (x, y)
        self.cells[y][x] = 1

    def set_goal(self, x, y):
        self.goal = (x, y)
        self.cells[y][x] = 2

    def a_star(self):

        def distance(goal, pos):
            return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])

        def reconstruct_path(came_from, current):
            def is_in(list, item):
                for row in list:
                    for ob in row:
                        if ob == item:
                            return True
                return False
            total_path = [current]
            first = True
            while first or is_in(came_from, current):
                first = False
                print(came_from[current[0]][current[1]])
                current = came_from[current[0]][current[1]]
                if current is None:
                    return total_path
                self.cells[current[0]][current[1]] = 4
                total_path.insert(0, current)
            return total_path

        open_set = [self.start]
        closed_set = []

        g_score = [[np.inf for _ in range(self.cols)] for _ in range(self.rows)]
        g_score[self.start[0]][self.start[1]] = 0

        came_from = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        f_score = [[np.inf for _ in range(self.cols)] for _ in range(self.rows)]
        f_score[self.start[0]][self.start[1]] = distance(self.goal, self.start)

        while len(open_set) > 0:
            open_set.sort(key=lambda node: f_score[node[0]][node[1]])
            curr_tuple = open_set[0]
            curr_pos = curr_tuple

            # goal found
            if self.goal == curr_pos:
                return reconstruct_path(came_from, curr_tuple)

            open_set = open_set[1:]
            closed_set.append(curr_tuple)
            # loop over all valid neighbors
            neighbors = self.get_neighbors(curr_pos[0], curr_pos[1])
            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue
                row = neighbor[0]
                col = neighbor[1]
                score = g_score[curr_pos[0]][curr_pos[1]] + 1
                print(row, col)
                if score < g_score[row][col]:
                    came_from[row][col] = curr_tuple
                    g_score[row][col] = score
                    f_score[row][col] = g_score[row][col] + distance(self.goal, neighbor)
                    if neighbor not in open_set:
                        open_set.append(neighbor)
        print("No path found")

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

