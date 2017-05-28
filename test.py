import unittest

from game import *
from board import *

class TestBoardMethods(unittest.TestCase):

    def test_is_solved(self):
        constraints = {'A1':{'right': 3, 'down': 3}, 'B2': None, 'B3': None, 'C2': None, 'C3': None}
        b = Board(3, constraints)

        solutions = b.create_initial_solutions(3)

        solutions['A2'] = '1'
        solutions['A3'] = '2'
        solutions['B1'] = '1'
        solutions['C1'] = '2'

        self.assertTrue(b.is_solved(solutions))

    def test_is_solved_returns_false_for_initial_board_stage(self):
        constraints = {'A1':{'right': 3, 'down': 3}, 'B2': None, 'B3': None, 'C2': None, 'C3': None}
        b = Board(3, constraints)

        solutions = b.create_initial_solutions(3)

        self.assertFalse(b.is_solved(solutions))

    def test_traverse_through_options(self):
        constraints = {'A1':{'right': 3, 'down': 3}, 'B2': None, 'B3': None, 'C2': None, 'C3': None}
        b = Board(3, constraints)

        solutions = b.create_initial_solutions(3)

        options = b.traverse_through_options(solutions)
        self.assertEqual(len(options), 3)

        for optional_board in options:
            self.assertNotEqual(solutions, optional_board)

    def test_constraint_remove_single_value_from_peers(self):
        constraints = {'A1':{'right': 3, 'down': 3}, 'B2': None, 'B3': None, 'C2': None, 'C3': None}
        b = Board(3, constraints)

        solutions = b.create_initial_solutions(3)
        solutions['A2'] = '1'
        solutions['C1'] = '2'

        expected = copy.copy(solutions)
        expected['A3'] = '23'
        expected['B1'] = '13'

        reduced = b.constraint_remove_single_value_from_peers(solutions)

        self.assertEqual(reduced, expected)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBoardMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
