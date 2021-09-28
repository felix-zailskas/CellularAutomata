from GameOfLife import GameOfLife
import numpy as np


class GameInitializer:
    @staticmethod
    def initialize_random(game: GameOfLife):
        return np.around(np.random.rand(game.rows, game.cols)).astype(int)

    @staticmethod
    def initialize_vertical_lines(game: GameOfLife):
        cells = np.empty((game.rows, game.cols))
        for i in range(game.rows):
            cells[i] = np.ones(game.cols, dtype=int) if i % 2 == 0 else np.zeros(game.cols, dtype=int)
        return cells

    @staticmethod
    def initialize_horizontal_lines(game: GameOfLife):
        cells = np.empty((game.rows, game.cols))
        for i in range(game.rows):
            for j in range(game.cols):
                cells[i][j] = 1 if (j + 1) % 2 == 0 else 0
        return cells

    @staticmethod
    def initialize_checkered(game: GameOfLife):
        cells = np.empty((game.rows, game.cols))
        for i in range(game.rows):
            for j in range(game.cols):
                cells[i][j] = 1 if (j + i) % 2 == 0 else 0
        return cells

