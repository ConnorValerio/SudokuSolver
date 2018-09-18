__author__ = "Connor Valerio"

from board import Board
from cell import Cell

# visual of sudoku board

"""
EMPTY TEMPLATE:

row_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
row_9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

"""
# Easy
row_1 = [3, 6, 0, 0, 7, 1, 2, 0, 0]
row_2 = [0, 5, 0, 0, 0, 0, 1, 8, 0]
row_3 = [0, 0, 9, 2, 0, 4, 7, 0, 0]
row_4 = [0, 0, 0, 0, 1, 3, 0, 2, 8]
row_5 = [4, 0, 0, 5, 0, 2, 0, 0, 9]
row_6 = [2, 7, 0, 4, 6, 0, 0, 0, 0]
row_7 = [0, 0, 5, 3, 0, 8, 9, 0, 0]
row_8 = [0, 8, 3, 0, 0, 0, 0, 6, 0]
row_9 = [0, 0, 7, 6, 9, 0, 0, 4, 3]
"""

# Hard
row_1 = [1, 0, 0, 0, 7, 0, 0, 3, 0]
row_2 = [8, 3, 0, 6, 0, 0, 0, 0, 0]
row_3 = [0, 0, 2, 9, 0, 0, 6, 0, 8]
row_4 = [6, 0, 0, 0, 0, 4, 9, 0, 7]
row_5 = [0, 9, 0, 0, 0, 0, 0, 5, 0]
row_6 = [3, 0, 7, 5, 0, 0, 0, 0, 4]
row_7 = [2, 0, 3, 0, 0, 9, 1, 0, 0]
row_8 = [0, 0, 0, 0, 0, 2, 0, 4, 3]
row_9 = [0, 4, 0, 0, 8, 0, 0, 0, 9]

"""
row_1 = [1, 6, 9, 0, 7, 0, 4, 3, 0]
row_2 = [8, 3, 4, 6, 0, 0, 7, 9, 0]
row_3 = [0, 0, 2, 9, 4, 3, 6, 1, 8]
row_4 = [6, 0, 0, 0, 3, 4, 9, 0, 7]
row_5 = [4, 9, 8, 0, 0, 0, 3, 5, 1]
row_6 = [3, 0, 7, 5, 9, 0, 0, 6, 4]
row_7 = [2, 0, 3, 4, 5, 9, 1, 0, 6]
row_8 = [9, 0, 0, 0, 0, 2, 0, 4, 3]
row_9 = [0, 4, 0, 3, 8, 0, 0, 0, 9]
"""

"""
row_1 = [0, 0, 1, 7, 0, 0, 3, 4, 0]
row_2 = [0, 8, 0, 0, 4, 0, 0, 0, 6]
row_3 = [0, 0, 0, 0, 5, 0, 2, 8, 0]
row_4 = [0, 0, 0, 2, 0, 0, 0, 1, 8]
row_5 = [0, 6, 0, 0, 0, 0, 0, 2, 0]
row_6 = [1, 3, 0, 0, 0, 7, 0, 0, 0]
row_7 = [0, 2, 5, 0, 1, 0, 0, 0, 0]
row_8 = [6, 0, 0, 0, 7, 0, 0, 9, 0]
row_9 = [0, 1, 7, 0, 0, 9, 8, 0, 0]
"""

# store values in list
values = []

values.extend(row_1)
values.extend(row_2)
values.extend(row_3)
values.extend(row_4)
values.extend(row_5)
values.extend(row_6)
values.extend(row_7)
values.extend(row_8)
values.extend(row_9)

# create a Cell object for each value
cells = []

index = 0
for row in range(1, 10):
    for col in range(1, 10):
        cells.extend([Cell(row, col, values[index])])
        index += 1

board = Board(cells)
board.solve()
