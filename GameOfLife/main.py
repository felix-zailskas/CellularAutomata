from tkinter import *
from CellularAutomaton import CellularAutomaton
from CellularAutomatonCanvas import CellularAutomatonCanvas
from Rules import Rules
from Initializer import Initializer
from Presets import Presets
import random


master = Tk()

#random.seed(0)

rows = 60
cols = 30
resolution = 5
frame_frequency = 1

#TODO Clean up the package situation
#TODO: Let user choose between all variations and connect all execution to the GUI
ca = CellularAutomaton(rows, cols, resolution)
ca.fill_cells(cells=Initializer.initialize_with_preset(ca, Presets.Guns.SIMKIN, pos=(20, 20)))

eca = CellularAutomaton(rows, cols, resolution, elementary=True)
eca.fill_cells(cells=Initializer.initialize_random_row(eca, eca.rows - 1))

canvas = CellularAutomatonCanvas(master, ca)
canvas.pack()
i = 0
while True:
    if i == 0 and not ca.is_stagnating:
        ca.print_generation()
        canvas.update()
        ca.update_cells(Rules.GAME_OF_LIFE)
    i = (i + 1) % frame_frequency
    master.update()
