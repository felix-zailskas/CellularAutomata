from tkinter import *
from GameOfLife import GameOfLife
from GameOfLifeCanvas import GameOfLifeCanvas
import random


master = Tk()

#random.seed(0)

canvas_width = 450
canvas_height = 450
resolution = 10
ratio = 0.7


gol = GameOfLife(canvas_height, canvas_width, resolution)
gol.fill_cells(ratio=ratio)
gol.print_cells()

canvas = GameOfLifeCanvas(master, gol)
canvas.pack()
while True:
    canvas.update()
    gol.update_cells()
    master.update()
