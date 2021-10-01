import numpy as np
from Rules import Rules


class RuleApplication:
    @staticmethod
    def apply_rule(automaton, rule: Rules, rule_idx=0, offset=(1, 0), carry_over=True, majority=5):
        if rule == Rules.GAME_OF_LIFE:
            return RuleApplication.apply_game_of_life_rule(automaton)
        if rule == Rules.PULSATE:
            return RuleApplication.apply_pulsate_rule(automaton)
        if rule == Rules.MAJORITY:
            return RuleApplication.apply_majority_rule(automaton, majority=majority)
        if rule == Rules.ELEMENTARY:
            return RuleApplication.apply_elementary_rule(automaton, rule_idx)
        if rule == Rules.OFFSET:
            return RuleApplication.apply_offset_rule(automaton, offset, carry_over=carry_over)

    @staticmethod
    def apply_game_of_life_rule(automaton):
        new_cells = np.empty([automaton.rows, automaton.cols])
        for i in range(automaton.rows):
            for j in range(automaton.cols):
                live_neighbors = automaton.get_live_neighbors(i, j)
                if automaton.cells[i][j] == 1:
                    # Rule 1, 3: Alive cell with >3 or <2 neighbors dies
                    if live_neighbors > 3 or live_neighbors < 2:
                        new_cells[i][j] = 0
                        continue
                # Rule 4: Dead cells with 3 alive neighbors becomes alive
                elif live_neighbors == 3:
                    new_cells[i][j] = 1
                    continue
                new_cells[i][j] = automaton.cells[i][j]
        return new_cells

    @staticmethod
    def apply_offset_rule(automaton, offset: (int, int), carry_over=True):
        x_off, y_off = offset
        if x_off == 0 and y_off == 0:
            return automaton.cells
        new_cells = np.empty([automaton.rows, automaton.cols])
        for i in range(automaton.cols):
            for j in range(automaton.rows):
                if (j == 0 and y_off < 0) or\
                        (j == automaton.rows - 1 and y_off > 0):
                    new_cells[(j + y_off) % automaton.rows][i] = 0 if not carry_over else automaton.cells[j][i]
                    continue
                if (i == 0 and x_off < 0) or\
                        (i == automaton.cols - 1 and x_off > 0)\
                        and not carry_over:
                    new_cells[j][(i + x_off) % automaton.cols] = 0 if not carry_over else automaton.cells[j][i]
                    continue
                new_cells[(j + y_off) % automaton.rows][(i + x_off) % automaton.cols] = automaton.cells[j][i]
        return new_cells

    @staticmethod
    def apply_pulsate_rule(automaton):
        new_cells = np.empty([automaton.rows, automaton.cols])
        for i in range(automaton.rows):
            for j in range(automaton.cols):
                new_cells[i][j] = abs(automaton.cells[i][j] - 1)
        return new_cells

    @staticmethod
    def apply_majority_rule(automaton, majority):
        new_cells = np.empty([automaton.rows, automaton.cols])
        for i in range(automaton.rows):
            for j in range(automaton.cols):
                live_neighbors = automaton.get_live_neighbors(i, j)
                new_cells[i][j] = 1 if live_neighbors + automaton.cells[i][j] >= majority else 0
        return new_cells

    @staticmethod
    def apply_elementary_rule(automaton, rule_idx):
        new_cells = RuleApplication.apply_offset_rule(automaton, (0, -1), carry_over=False)
        rule = list(str(bin(rule_idx))[2:].rjust(8, '0'))
        for j in range(automaton.cols):
            neighbor_pattern = automaton.get_row_neighbors(automaton.rows - 1, j)
            rule_to_apply = int(neighbor_pattern, 2)
            new_cells[automaton.rows - 1][j] = int(rule[len(rule) - rule_to_apply - 1])
        return new_cells
