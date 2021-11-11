from CellularAutomata.model.CellularAutomaton.CellularAutomataModel import CellularAutomaton
from CellularAutomata.util.rules.Rules import Rules
from CellularAutomata.view.GridContainerFrame import CellularAutomatonFrame
from CellularAutomata.util.initialization.Initializer import Initializer


if __name__ == "__main__":
    # random.seed(0)

    rows = 150
    cols = 150
    resolution = 3

    # TODO: make GUI class
    # TODO: Let user choose between all variations and connect all execution to the GUI
    ca = CellularAutomaton(rows, cols)
    ca.set_cells(cells=Initializer.initialize_random(ca))

    eca = CellularAutomaton(rows, cols, elementary=True)
    eca.set_cells(cells=Initializer.initialize_random_row(eca, eca.rows - 1))

    frame = CellularAutomatonFrame(ca, cols, rows, resolution, Rules.OFFSET, rule_idx=0, offset=(1, 0), carry_over=True)
    frame.start_scene()
