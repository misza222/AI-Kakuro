# Kakuro
## as an example of search and constraint propagation

### Game rules

See [wikipedia](https://en.wikipedia.org/wiki/Kakuro) for details

### Kakuro AI agent

This demonstrates use of search and constraint propagation.

### TODO:

  1. optimize traversing through options

     When constraint_propagation method get's stuck in solving the board, we need to traverse through available options and try to solve that problem.

     Currently we choose options by random. We should perhaps choose the box with the shortest list of options.

  1. Add new constraints and propagation steps

    * naked twins

### Environment

 * python 3
