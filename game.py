from board import *

class Game:
    def __init__(self, size, constraints):
        self.board = Board(size, constraints)

    def draw(self, solutions):
        print(self.board.draw(solutions))

    def run(self):
        solved = self.board.solve()
        if solved:
            return solved
        else:
            raise UnsolvableException("")
