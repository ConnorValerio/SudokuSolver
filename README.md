# SudokuSolver

Algorithm checks whether a cell has a value, if it does not, it finds all possible values for that cell. It then tries to eliminate possibilities based on the possibilities of other cells in it's row, column or grid. I.e. if the cell at (1,1) has the possibility of being a 3 or a 4, and the only other free cell in the row (say, at (1, 6)) has the possibility of being a '4'. The current cell must be a '3', and hence eventually the other cell in the row will be given the value '4'.

NOTE: The logic behind this algorithm will not be able to solve all sudoku puzzles. It does not look for patterns such as 'unique candidate', i.e. in the following scenario:

0 0 4 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
=====================
0 0 0 | 0 0 0 | 0 0 0
0 4 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
=====================
5 0 0 | 0 0 0 | 0 0 0
* 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 4 | 0 0 0

The cell at position * obviously has to be a 4. However, the algorithm will only compare possible values with other cells in it's row, column or cell, and hence, if not enough information is available, the algorithm will be unable to deduce a value for a cell.

Due to this restriction, a fail-safe has been implemented. If after 3 loops of the cells, the solve count has not been increased, the program will be terminated. 
