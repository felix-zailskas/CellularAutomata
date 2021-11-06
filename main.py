from tkinter import *
from CellularAutomata.model.CellularAutomaton.CellularAutomataModel import CellularAutomaton
from CellularAutomata.GUI.GridCanvas import GridCanvas
from CellularAutomata.util.rules.Rules import Rules
from CellularAutomata.util.initialization.Initializer import Initializer


master = Tk()

#random.seed(0)

rows = 50
cols = 50
resolution = 5
frame_frequency = 1

#TODO: make GUI class
#TODO Clean up the package situation
#TODO: Let user choose between all variations and connect all execution to the GUI
ca = CellularAutomaton(rows, cols)
ca.set_cells(cells=Initializer.initialize_random(ca))

eca = CellularAutomaton(rows, cols, elementary=True)
eca.set_cells(cells=Initializer.initialize_random_row(eca, eca.rows - 1))

canvas = GridCanvas(master, ca.rows, ca.cols, ca.cells, resolution)
canvas.pack()
i = 0
while True:
    if i == 0 and not ca.is_stagnating:
        ca.print_generation()
        canvas.update(ca.cells)
        ca.update_cells(Rules.MAJORITY, offset=(1,0))
    i = (i + 1) % frame_frequency
    master.update()
