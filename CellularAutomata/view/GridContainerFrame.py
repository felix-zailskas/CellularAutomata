from operator import add
from CellularAutomata.model.GridContainer import GridContainer
from CellularAutomata.model.CellularAutomaton import CellularAutomataModel
from CellularAutomata.util.rules.Rules import Rules
import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (122, 122, 122)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRID_COLORS = [WHITE, BLACK, GREEN, BLUE, RED]


class CellularAutomatonFrame:
    def __init__(self, grid_container: CellularAutomataModel, width: int, height: int, res: int,
                 rule: Rules = Rules.GAME_OF_LIFE,
                 rule_idx=0, offset=(1, 0), carry_over=True):
        self.grid_container = grid_container
        self.width = width * res
        self.height = height * res
        self.rule = rule
        self.rule_idx = rule_idx
        self.offset = offset
        self.carry_over = carry_over
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
            # drawing cells
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
            # checkered grid
            for i in range(cols):
                x = i * self.res
                pygame.draw.line(display, GRAY, (x, 0), (x, self.height))
            for j in range(rows):
                y = j * self.res
                pygame.draw.line(display, GRAY, (0, y), (self.width, y))
            
            self.grid_container.update_cells(rule=self.rule, rule_idx=self.rule_idx, offset=self.offset, carry_over=self.carry_over)
            pygame.display.update()
            time.sleep(0.01)
