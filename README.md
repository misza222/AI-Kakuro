# Kakuro
## as an example of search and constraint propagation

### Game rules

See [wikipedia](https://en.wikipedia.org/wiki/Kakuro) for details

### Kakuro AI agent

This demonstrates use of search and constraint propagation.

### Code

Code is broken down into few files, and the **board.py** is the mostim iportant of those. It holds all the logic within Board class.
**game.py** is there simply to create and "run" the board.

For an example of how to use the came, see **game.py**

### TODO:

  1. optimize traversing through options

     When constraint_propagation method get's stuck in solving the board, we need to traverse through available options and try to solve that problem.

     Currently we choose options by random. We should perhaps choose the box with the shortest list of options.

  1. Add new constraints and propagation steps

    * naked twins

  1. Validate initial parameters - simple checks to see if the board is complete, if all the boxes are accounted for etc.

  1. ... and finally see smaller TODOs in code

### Environment

 * python 3
