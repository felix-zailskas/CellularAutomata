from CellularAutomaton import CellularAutomaton
import numpy as np


class Initializer:
    @staticmethod
    def initialize_with_preset(automaton:CellularAutomaton, preset):
        assert automaton.rows >= preset.shape[0] and automaton.cols >= preset.shape[1]
        cells = np.zeros((automaton.rows, automaton.cols))
        cells[:preset.shape[0], :preset.shape[1]] = preset
        return cells

    @staticmethod
    def initialize_random(automaton: CellularAutomaton):
        return np.around(np.random.rand(automaton.rows, automaton.cols)).astype(int)

    @staticmethod
    def initialize_random_row(automaton: CellularAutomaton, row):
        cells = np.zeros((automaton.rows, automaton.cols))
        cells[row] = np.around(np.random.rand(automaton.cols)).astype(int)
        return cells

    @staticmethod
    def initialize_cell(automaton: CellularAutomaton, row, col):
        cells = np.zeros((automaton.rows, automaton.cols))
        cells[row][col] = 1
        return cells

    @staticmethod
    def initialize_lines(automaton: CellularAutomaton, horizontal=True, vertical=False):
        cells = np.empty((automaton.rows, automaton.cols))
        for i in range(automaton.rows):
            if vertical:
                cells[i] = np.ones(automaton.cols, dtype=int) if i % 2 == 0 else np.zeros(automaton.cols, dtype=int)
            if horizontal:
                for j in range(automaton.cols):
                    cells[i][j] = 1 if (j + 1) % 2 == 0 else cells[i][j]
        return cells

    @staticmethod
    def initialize_checkered(automaton: CellularAutomaton):
        cells = np.empty((automaton.rows, automaton.cols))
        for i in range(automaton.rows):
            for j in range(automaton.cols):
                cells[i][j] = 1 if (j + i) % 2 == 0 else 0
        return cells

