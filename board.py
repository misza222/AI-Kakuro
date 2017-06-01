import copy
from utils import *

class Board:
    """
        Terminology:
            * box  : is a single field on a board
            * unit : is a vertical or horizontal group of boxes that have to sum up to the
                     value from the constraints, and the target sum itself
    """
    def __init__(self, size, constraints):
        if size > 9:
            raise BoardException('Board too large. Please use boards of up to 9 in size.')
        self.size = size
        self.constraints = constraints # TODO: remove constraints as it is obsolete and change initial solutions creation
        self.units = self.create_units(size, constraints)

    def create_units(self, size, constraints):
        units = []
        # go throught user provided constraints and translate it into units with constraints attached to them
        for constraint_box in constraints.keys():
            if constraints[constraint_box]:
                row, column = list(constraint_box)
                for direction in constraints[constraint_box].keys():
                    unit = []

                    if direction == 'down':
                        unit = {'elements':
                                    [box_row + column for box_row in list(alpha)[list(alpha).index(row) + 1:self.size]]}
                    elif direction == 'right':
                        unit = {'elements':
                                [row + str(box_column) for box_column in range(int(column) + 1, self.size + 1)]}
                    else:
                        raise BoardException("Unimplemented direction ", direction)
                    unit['sum'] = constraints[constraint_box][direction]
                    units.append(unit)

        return units

    def create_initial_solutions(self, size):
        board_elems = self.cross(alpha_range(size), range(1, size + 1))
        available_elements = "".join([str(i) for i in range(1, size + 1)])
        return {elem: available_elements for elem in board_elems if elem not in self.constraints}

    def cross(self, A, B):
        return [a+str(b) for a in A for b in B]

    def draw(self, solutions):
        return "Size ", self.size, " Constraints: ", self.constraints, " Solutions: ", solutions

    def is_solved(self, board):
        # do all boxes have a single value?
        if not all(len(board[box]) == 1 for box in board.keys()):
            return False

        for unit in self.units:
            # do all units sum correctly?
            if not unit['sum'] == sum([int(board[element]) for element in unit['elements']]):
                return False
            # do all units have unique values?
            if not len(unit['elements']) == len(set([board[element] for element in unit['elements']])):
                return False

        return True

    def constraint_propagation(self, board):
        board = self.constraint_remove_single_value_from_peers(board)
        board = self.constraint_naked_twins(board)
        return board

    def constraint_naked_twins(self, board):
        return board

    def constraint_remove_single_value_from_peers(self, board):
        """
        Algorithm:
            For all the units, go through all the boxes, and if any box is
            solved (there is just one value in it), remove that value from
            all it's peers
        """
        for unit in self.units:
            for box in unit['elements']:
                if len(board[box]) == 1:
                    for peer in unit['elements']:
                        if peer != box:
                            board[peer] = board[peer].replace(board[box], '')

        return board

    def traverse_through_options(self, board):
        # find a box with shortest options
        for box in board.keys():
            if len(board[box]) > 1:
                optional_boards = []
                for option in board[box]:
                    board_cp = copy.copy(board)
                    board_cp[box] = option
                    optional_boards.append(board_cp)

                return optional_boards

        return []

    def search(self, board):
        prev_board = board
        board = self.constraint_propagation(board)

        while prev_board != board:
            prev_board = board
            board = self.constraint_propagation(board)

        if self.is_solved(board):
            return board

        for i, optional_board in enumerate(self.traverse_through_options(board)):
            search_board = self.search(optional_board)

            if search_board and self.is_solved(search_board):
                return search_board

        return False

    def solve(self):
        solutions = self.create_initial_solutions(self.size)
        return self.search(solutions)
