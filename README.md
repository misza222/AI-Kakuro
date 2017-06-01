# Kakuro
## as an example of search and constraint propagation

### Game rules

See [wikipedia](https://en.wikipedia.org/wiki/Kakuro) for details

### Kakuro AI agent

This demonstrates use of search and constraint propagation.

### Code

Code is broken down into 2 files:

  * **board.py** where all the logic lives,
  * **game.py** is just for board creation and has some usage examples.

### Running the code

See **game.py** for a few examples.


```
constraints = {'A1':{'right': 3, 'down': 3}, 'B2': None, 'B3': None, 'C2': None, 'C3': None}
g = Game(size, constraints)
solved = g.run()
```

If you look at the wikipedia page [explaining Kakuro](https://en.wikipedia.org/wiki/Kakuro) those constraints should be intuitive. It includes clues (sums of elements in the adjacent row or column) and "black" fields (fields that should not be filled; indicated with ```None```).

### TODO:

  1. Create a more complex example and test. Perhaps we could replicate [this one](https://upload.wikimedia.org/wikipedia/commons/7/72/Kakuro_black_box_solution.svg)

  1. optimize traversing through options

     When constraint_propagation method get's stuck in solving the board, we need to traverse through available options and try to solve that problem.
     Currently we choose options by random. We should perhaps choose the box with the shortest list of options? Any other ideas for optimization at this stage?

  1. Add new constraints and propagation steps

    * naked twins

    ... more ideas [here](https://en.wikipedia.org/wiki/Kakuro#Solving_techniques)

  1. Validate initial parameters - simple checks to see if the board is complete, if all the boxes are accounted for at the initialization etc.

  1. ... and finally see smaller TODOs in code

  1. Board visualization - ideas what to use are welcome

### Environment

 * python 3.x

### Contributing

Feel free to join in and contribute. Simply fork and when you've added something create a pull request describing what was done, add some tests if necessary and perhaps an example if you wish. For details of this git workflow see [github help page](https://github.com/processing/processing/wiki/Contributing-to-Processing-with-Pull-Requests)
