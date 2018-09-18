# SudokuSolver

The logical part of the algorithm checks whether a cell has a value, if it does not, it finds all possible values for that cell. It then tries to eliminate possibilities based on the possibilities of other cells in it's row, column or square. I.e. if the cell at (1,1) has the possibility of being a 3 or a 4, and the only other free cell in the row (say, at (1, 6)) has the possibility of being a '4'. The current cell must be a '3', and hence eventually the other cell in the row will be given the value '4'.

NOTE: The logic behind this algorithm will not be able to solve all sudoku puzzles.

Due to this restriction, a fail-safe has been implemented. If after 3 loops of the cells, the solve count has not been increased, the program will resort to using depth-first search to try and brute force a solution.

HOW IT WORKS
------------

The current board (up to where the logic failed) is pushed onto the stack. While the stack is not empty, the top board is popped from the stack and is checked for completion and validation. If the sudoku is not solved, the current board's next possible states are calculated and pushed onto the stack.

The next states of the sudoku board are calculated as follows:

- A no-value cell with the fewest possibilities is found.
- For each possibility of that cell, a new board is created replacing said cell, with its possible value. This is done using 'clone_and_replace_x()'.

Inside the cloning method, each cell is cloned individually from the current board. When the cell at the position of the cell being replaced is found, a new cell is created with the passed possible value.

Before returning the cloned board with the cell at position x,y replaced, each cell's new possible values must be calculated. This is to prevent the algorithm from trying values that are going to be invalid.




