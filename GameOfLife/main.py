from tkinter import *
from CellularAutomaton import CellularAutomaton
from CellularAutomatonCanvas import CellularAutomatonCanvas
from Rules import Rules
from Initializer import Initializer
import random


master = Tk()

#random.seed(0)

rows = 70
cols = 70
resolution = 5
ratio = 0.7
frame_frequency = 60

#TODO: Automaton is only running on a square grid
#TODO Clean up the package situation
#TODO: Let user choose between all variations and connect all execution to the GUI
ca = CellularAutomaton(rows, cols, resolution)
ca.fill_cells(cells=Initializer.initialize_lines(ca), ratio=ratio)

canvas = CellularAutomatonCanvas(master, ca)
canvas.pack()
i = 0
while True:
    if i == 0 and not ca.is_stagnating:
        ca.print_generation()
        canvas.update()
        ca.update_cells(Rules.OFFSET, offset=(0, -1), carry_over=False)
    i = (i + 1) % frame_frequency
    master.update()
