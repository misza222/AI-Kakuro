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

if __name__ == "__main__":
    g = Game(3, {'A1':{'right': 3, 'down': 3}, 'B2': None, 'B3': None, 'C2': None, 'C3': None})
    solved = g.run()
    g.draw(solved)

    g = Game(2, {'A1':{'right': 1, 'down': 1}, 'B2': None})
    solved = g.run()
    g.draw(solved)

    g = Game(4, {'A1':{'right': 6, 'down': 7}, 'B2': None, 'B3': None, 'B4': None, 'C2': None, 'C3': None, 'C4': None, 'D2': None, 'D3': None, 'D4': None})
    solved = g.run()
    g.draw(solved)
