from CellularAutomata.util.filling.FloodFill import flood_fill
import numpy as np

test_arr = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0]
])

result_arr = np.zeros((test_arr.shape[0], test_arr.shape[1]), dtype=int)

flooded_cells = flood_fill(test_arr, 0, 0)
print("The flooded cells:")
print(flooded_cells)
print("Expected:")
print("[(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]")

# This part works
for row in range(test_arr.shape[0]):
    for col in range(test_arr.shape[1]):
        print(row, col)
        if not (row, col) in flooded_cells:
            result_arr[row][col] = 1

print("Original:")
for row in test_arr:
    print(row)

print("Result:")
for row in result_arr:
    print(row)
