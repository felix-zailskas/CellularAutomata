from tkinter import *
from GameOfLife import GameOfLife
from GameOfLifeCanvas import GameOfLifeCanvas
from Rules import Rules
from GameInitializer import GameInitializer
import random


master = Tk()

#random.seed(0)

canvas_width = 500
canvas_height = 500
resolution = 10
ratio = 0.7
frame_frequency = 600


gol = GameOfLife(canvas_height, canvas_width, resolution)
gol.fill_cells(cells=GameInitializer.initialize_checkered(gol), ratio=ratio)

canvas = GameOfLifeCanvas(master, gol)
canvas.pack()
i = 0
while True:
    if i == 0:
        canvas.update()
        gol.update_cells(Rules.PULSATE)
    i = (i + 1) % frame_frequency
    master.update()
