from tkinter import *
from CellularAutomaton import CellularAutomaton
from CellularAutomatonCanvas import CellularAutomatonCanvas
from Rules import Rules
from Initializer import Initializer
from Presets import Presets
import random


master = Tk()

#random.seed(0)

rows = 80
cols = 80
resolution = 3
frame_frequency = 1

#TODO: make GUI class
#TODO Clean up the package situation
#TODO: Let user choose between all variations and connect all execution to the GUI
ca = CellularAutomaton(rows, cols)
ca.set_cells(cells=Initializer.initialize_random(ca))

eca = CellularAutomaton(rows, cols, elementary=True)
eca.set_cells(cells=Initializer.initialize_random_row(eca, eca.rows - 1))

canvas = CellularAutomatonCanvas(master, ca, resolution)
canvas.pack()
i = 0
while True:
    if i == 0 and not ca.is_stagnating:
        ca.print_generation()
        canvas.update()
        ca.update_cells(Rules.MAJORITY)
    i = (i + 1) % frame_frequency
    master.update()
