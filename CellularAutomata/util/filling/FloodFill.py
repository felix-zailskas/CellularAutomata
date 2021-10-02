import numpy as np
import queue
'''
https://en.wikipedia.org/wiki/Flood_fill

Flood-fill (node):
  1. Set Q to the empty queue or stack.
  2. Add node to the end of Q.
  3. While Q is not empty:
  4.   Set n equal to the first element of Q.
  5.   Remove first element from Q.
  6.   If n is Inside:
         Set the n
         Add the node to the west of n to the end of Q.
         Add the node to the east of n to the end of Q.
         Add the node to the north of n to the end of Q.
         Add the node to the south of n to the end of Q.
  7. Continue looping until Q is exhausted.
  8. Return.
'''


def flood_fill(grid, row, col):
    """
    Fills the unreachable spaces in a 2D grid, given a starting point.
    Reachable spots are coded as 0.
    Unreachable spots are coded as 1.
    :param grid: 2D array containing 0 or 1
    :param col: Starting column for the algorithm
    :param row: Starting row for the algorithm
    :return: A List of all (y,x) pairs that are unreachable
    """
    q = queue.Queue()
    q.put((row, col))
    grid_copy = np.array(grid)
    filled = []
    while not q.empty():
        y, x = q.get()
        if y < 0 or x < 0 or y >= grid.shape[0] or x >= grid.shape[1]:
            continue
        # cell is free
        if grid_copy[y][x] == 0:
            # mark as visited
            grid_copy[y][x] = 2
            # add to filled
            filled.append((y, x))
            # add all neighbors that have not been visited
            q.put((y + 1, x))
            q.put((y - 1, x))
            q.put((y, x + 1))
            q.put((y, x - 1))
        elif grid_copy[y][x] == 1:
            # mark as visited
            grid_copy[y][x] = 2
    return filled
