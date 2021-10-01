import numpy as np
from FloodFill import flood_fill


def fill_region(grid, row, col):
    flooded_cells = flood_fill(grid, row, col)
    result_cells = np.zeros((grid.shape[0], grid.shape[1]), dtype=int)
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not (row, col) in flooded_cells:
                result_cells[row][col] = 1
    return result_cells