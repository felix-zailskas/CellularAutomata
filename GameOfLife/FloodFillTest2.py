import RegionFiller
from CellularAutomaton import CellularAutomaton
from CellularAutomatonCanvas import CellularAutomatonCanvas
from Initializer import Initializer
from Rules import Rules
from tkinter import *


master = Tk()
rows = 100
cols = 100
resolution = 5

# initializing the CA
filled_ca = CellularAutomaton(rows, cols)
filled_ca.set_cells(Initializer.initialize_random(filled_ca))
# Fill CA with Majority rule as estimate of the map
filled_ca.become_stagnant(Rules.MAJORITY)
majority_ca = filled_ca.copy()
# Fill all unreachable spots
filled_ca.set_cells(RegionFiller.fill_region(filled_ca.cells, 0, 0))

c1 = CellularAutomatonCanvas(master, filled_ca, resolution)
c2 = CellularAutomatonCanvas(master, majority_ca, resolution)

c1.pack(side="left", fill="both", expand=True)
c2.pack(side="right", fill="both", expand=True)
c1.update()
c2.update()
mainloop()
