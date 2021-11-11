from operator import add
from CellularAutomata.model.GridContainer import GridContainer
from CellularAutomata.model.CellularAutomaton import CellularAutomataModel
from CellularAutomata.util.rules.Rules import Rules
import pygame
import time

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (122, 122, 122)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRID_COLORS = [WHITE, BLACK, GREEN, BLUE, RED]
CONTROL_PANE_BACKGROUND_COLOR = (80, 80, 80)

# Constants
CONTROL_PANE_WIDTH = 200


class CellularAutomatonFrame:
    def __init__(self, grid_container: CellularAutomataModel, res: int):
        self.grid_container = grid_container
        self.width = grid_container.cols * res + CONTROL_PANE_WIDTH
        self.height = grid_container.rows * res
        self.res = res

    def start_scene(self):
        pygame.init()
        pygame.display.set_caption('Cellular Automaton')
        pygame.font.init()
        display = pygame.display.set_mode((self.width, self.height))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            grid = self.grid_container.cells
            cols = self.grid_container.cols
            rows = self.grid_container.rows
            # clear display
            display.fill(GRAY)

            self.draw_cells(cols, rows, grid, display)
            self.draw_grid(cols, rows, display)
            self.draw_control_pane(display)
            
            self.grid_container.update_cells(rule=Rules.OFFSET, rule_idx=33, offset=(1, 0), carry_over=True)
            pygame.display.update()
            time.sleep(0.01)

    def draw_control_pane(self, display):
        control_pane_rect = (self.grid_container.cols * self.res, 0, self.width, self.height)
        pygame.draw.rect(display, CONTROL_PANE_BACKGROUND_COLOR, control_pane_rect)

    def draw_cells(self, cols, rows, grid, display):
        for i in range(cols):
            for j in range(rows):
                try:
                    color = GRID_COLORS[int(grid[j][i])]
                except IndexError:
                    color = RED
                    print(f"Index not in color array!{int(grid[j][i]) = } at {j = } {i = }")
                x1 = i * self.res
                y1 = j * self.res
                x2 = (i + 1) * self.res
                y2 = (j + 1) * self.res
                pygame.draw.rect(display, color, (x1, y1, x2, y2))

    def draw_grid(self, cols, rows, display):
        for i in range(cols):
            x = i * self.res
            pygame.draw.line(display, GRAY, (x, 0), (x, self.height))
        for j in range(rows):
            y = j * self.res
            pygame.draw.line(display, GRAY, (0, y), (self.width, y))