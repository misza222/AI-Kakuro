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
     Currently we choose options by random. We should perhaps choose the box with the shortest list of options? Any other ideas for optimization at this stage?

  1. Add new constraints and propagation steps

    * naked twins

    ... more ideas [here](https://en.wikipedia.org/wiki/Kakuro#Solving_techniques)

  1. Validate initial parameters - simple checks to see if the board is complete, if all the boxes are accounted for at the initialization etc.

  1. ... and finally see smaller TODOs in code

### Environment

 * python 3.x

### Contributing

Feel free to join in and contribute. Simply fork and when you've added something create a pull request describing what was done, add some tests if necessary and perhaps an example if you wish. For details of this git workflow see [github help page](https://github.com/processing/processing/wiki/Contributing-to-Processing-with-Pull-Requests)
