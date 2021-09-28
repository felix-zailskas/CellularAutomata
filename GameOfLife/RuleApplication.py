import numpy as np
from Rules import Rules


class RuleApplication:
    @staticmethod
    def apply_rule(game, rule: Rules):
        if rule == Rules.CLASSIC:
            return RuleApplication.apply_classic_rules(game)
        if rule == Rules.DOWNROLL:
            return RuleApplication.apply_downroll_rules(game)
        if rule == Rules.SIDEROLL:
            return RuleApplication.apply_sideroll_rules(game)
        if rule == Rules.PULSATE:
            return RuleApplication.apply_pulsate_rules(game)

    @staticmethod
    def apply_classic_rules(game):
        # TODO: rule seems to be not working: cells jump between alive and dead
        new_cells = np.empty([game.rows, game.cols])
        for i in range(game.rows):
            for j in range(game.cols):
                live_neighbors = game.get_live_neighbors(i, j)
                if game.cells[i][j] == 1:
                    # Rule 1, 3: Alive cell with >3 or <2 neighbors dies
                    if live_neighbors > 3 or live_neighbors < 2:
                        new_cells[i][j] = 0
                        continue
                    # Rule 2: Alive cell with 2 or 3 neighbors stays alive
                    new_cells[i][j] = 1
                # Rule 4: Dead cells with 3 alive neighbors becomes alive
                elif live_neighbors == 3:
                    new_cells[i][j] = 1
        return new_cells

    @staticmethod
    def apply_downroll_rules(game):
        new_cells = np.empty([game.rows, game.cols])
        for i in range(game.rows):
            for j in range(game.cols):
                new_cells[i][(j + 1) % game.cols] = game.cells[i][j]
        return new_cells

    @staticmethod
    def apply_sideroll_rules(game):
        new_cells = np.empty([game.rows, game.cols])
        for i in range(game.rows):
            for j in range(game.cols):
                new_cells[(i + 1) % game.rows][j] = game.cells[i][j]
        return new_cells

    @staticmethod
    def apply_pulsate_rules(game):
        new_cells = np.empty([game.rows, game.cols])
        for i in range(game.rows):
            for j in range(game.cols):
                new_cells[i][j] = abs(game.cells[i][j] - 1)
        return new_cells
