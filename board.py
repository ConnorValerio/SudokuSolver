__author__ = "Connor Valerio"

from cell import Cell
from stack import Stack
import sys


class Board():

    def __init__(self, cells):
        self.cells = cells
        self.solve_count = 0
        self.prev_solve_count = 0
        self.fail_safe_count = 0

        # set cell neighbours
        for cell in self.cells:
            self.set_row_col_neighbours(cell)
            self.set_square_neighbours(cell)

    def solve(self):

        # find possible values for cells without a value
        for cell in self.cells:
            if(cell.get_val() == 0):
                self.find_poss_vals(cell)

        # 81 cells to solve
        while(self.solve_count < 81):

            # fail safe to prevent infinite loop
            if(self.handle_fail_safe()):
                print("FAILSAFE: The Sudoku puzzle cannot be solved logically.")
                self.brute_force()
                sys.exit()
                return

            for cell in self.cells:

                # cells with values:
                if(cell.get_val() != 0):
                    # increment count if cell has value
                    if(cell.is_solved() == False):
                        cell.set_solved()
                        self.increment_solve_count()
                # cells without values:
                else:
                    # check all possible values
                    self.resolve_poss_vals(cell)

    def find_poss_vals(self, cell):

        # get cell neighbours
        col_neighbours = cell.get_col_neighbours()
        row_neighbours = cell.get_row_neighbours()
        square_neighbours = cell.get_square_neighbours()

        # values 1-9
        for val in range(1, 10):
            if(not self.is_in_x(cell, row_neighbours, val) and
                    not self.is_in_x(cell, col_neighbours, val) and
               not self.is_in_x(cell, square_neighbours, val)):
                cell.add_poss_val(val)

    # x can be row, column or square neighbours
    def is_in_x(self, cell, neighbours, val):
        for neighbour in neighbours:
            if neighbour.get_val() == val:
                return True
        return False

    def resolve_poss_vals(self, cell):

        # get cell neighbours
        col_neighbours = cell.get_col_neighbours()
        row_neighbours = cell.get_row_neighbours()
        square_neighbours = cell.get_square_neighbours()

        # remove stale possible values
        for val in cell.get_poss_vals():
            # check if possible value is now in the row, column or square neighbours of this cell
            if(self.is_in_x(cell, row_neighbours, val)
                    or self.is_in_x(cell, col_neighbours, val)
                    or self.is_in_x(cell, square_neighbours, val)):
                cell.remove_poss_val(val)

        poss_vals = cell.get_poss_vals()

        # if a cell has only one possible value, set it
        if(len(poss_vals) == 1):
            cell.set_val(poss_vals[0])
            return

        # loop through new possible values and
        # compare possible values with other cells
        # in the same coloumn, row and square
        for val in poss_vals:
            if(self.is_only_cell_with_poss_val(cell, val)):
                cell.set_val(val)
                return

    # checks if this cell is the only cell in either:
    # the column, row or square that has a particular possible value
    def is_only_cell_with_poss_val(self, cell, val):

        # get neighbours
        col_neighbours = cell.get_col_neighbours()
        row_neighbours = cell.get_row_neighbours()
        square_neighbours = cell.get_square_neighbours()

        # flags
        only_col_cell = self.compare_to_neighbours(col_neighbours, val)
        only_row_cell = self.compare_to_neighbours(row_neighbours, val)
        only_square_cell = self.compare_to_neighbours(square_neighbours, val)

        # check all the flags
        if(only_col_cell or only_row_cell or only_square_cell):
            return True
        else:
            return False

    # returns true if no neighbour has the possible value
    def compare_to_neighbours(self, neighbours, val):
        for neighbour in neighbours:
            # only compare with neighbours without values
            if(neighbour.get_val() == 0):
                neighbour_poss_vals = neighbour.get_poss_vals()
                if(val in neighbour_poss_vals):
                    return False
        return True

    # sets row and column neighbours of each cell
    def set_row_col_neighbours(self, cell):

        col_neighbours = []
        row_neighbours = []

        cell_col = cell.get_col()
        cell_row = cell.get_row()

        for c in self.cells:
            c_col = c.get_col()
            c_row = c.get_row()
            # is current cell - skip
            if(c.is_equal_to(cell)):
                continue
            # found col neighbour
            if(c_col == cell_col):
                col_neighbours.append(c)
                continue
            # found row neighbour
            if(c_row == cell_row):
                row_neighbours.append(c)
                continue

        cell.set_row_neighbours(row_neighbours)
        cell.set_col_neighbours(col_neighbours)

    # sets square neighbours of each cell
    def set_square_neighbours(self, cell):

        square_neighbours = []
        # find bounds of cell rows/columns to be in same square
        row_min = self.get_min_bound(cell.get_row())
        row_max = self.get_max_bound(cell.get_row())
        col_min = self.get_min_bound(cell.get_col())
        col_max = self.get_max_bound(cell.get_col())

        for c in self.cells:
            c_row = c.get_row()
            c_col = c.get_col()

            # is current cell - skip
            if(c.is_equal_to(cell)):
                continue

            if((c_row > row_min and c_row <= row_max) and (c_col > col_min and c_col <= col_max)):
                square_neighbours.append(c)

        cell.set_square_neighbours(square_neighbours)

    def get_min_bound(self, val):
        min_bound = val

        if(min_bound % 3 == 0):
            min_bound -= 3
        else:
            while(min_bound % 3 != 0):
                min_bound -= 1

        return min_bound

    def get_max_bound(self, val):
        max_bound = val

        while(max_bound % 3 != 0):
            max_bound += 1

        return max_bound

    def handle_fail_safe(self):

        if(self.solve_count != self.prev_solve_count):
            self.fail_safe_count = 0
            self.prev_solve_count = self.solve_count
        else:
            self.fail_safe_count += 1

        if(self.fail_safe_count == 3):
            return True
        return False

    def increment_solve_count(self):
        self.solve_count += 1

    def printBoard(self):
        count = 1
        print("\n  PRINTING SUDOKU:\n  ---------------------\n")

        for cell in self.cells:
            # push print away from screen edge
            if(count % 9 == 1):
                print("  ", end="")
            # handle column separation
            if(count % 3 == 0 and count % 9 != 0):
                end = " | "
            else:
                end = " "
            # print cell value
            print(cell.get_val(), end=end)
            # handle row separation
            if(count % 9 == 0):
                print("\n", end="")
            if(count % 27 == 0):
                print("  ---------------------")
            count += 1

    def brute_force(self):
        print("Starting DFS Brute Force...")

        root = self
        stack = Stack()
        stack.push(root)

        while(not stack.isEmpty()):

            # print("Stack size: {}".format(stack.size()))

            current_board = stack.pop()
            # current_board.printBoard()

            # if the goal state has been found
            if(current_board.is_complete_and_valid()):
                print("complete")
                current_board.printBoard()
                return

            next_states = current_board.get_next_states()
            for board in next_states:
                if(board.is_valid()):
                    stack.push(board)

        print("The stack is empty, a solution has not been found.")

    def is_complete_and_valid(self):

        # complete sudoku should have every cell filled
        for cell in self.cells:
            if(cell.get_val() == 0):
                return False

        # complete sudoku should have valid rows, columns and squares
        if(not self.is_valid()):
            return False

        return True

    # used to check if the rows, columns and squares follow sudoku constraints
    def is_valid(self):
        if(self.has_valid_rows() and self.has_valid_cols() and self.has_valid_squares()):
            return True

    def has_valid_rows(self):

        for row in range(1, 10):

            cells_to_check = []
            for cell in self.cells:
                if(cell.get_row() == row):
                    cells_to_check.append(cell)

            # check the row for duplicate values
            if(self.has_duplicate_values(cells_to_check)):
                return False

        return True

    def has_valid_cols(self):

        for col in range(1, 10):

            cells_to_check = []
            for cell in self.cells:
                if(cell.get_col() == col):
                    cells_to_check.append(cell)

            # check the column for duplicate values
            if(self.has_duplicate_values(cells_to_check)):
                return False

        return True

    def has_valid_squares(self):
        # to implement
        return True

    # checks if cells have unique values
    def has_duplicate_values(self, cells_to_check):

        values_seen = []

        for cell in cells_to_check:
            val = cell.get_val()
            if(val != 0):
                if(val not in values_seen):
                    values_seen.append(val)
                else:
                    return True
        return False

    def get_next_states(self):

        # array of boards
        next_states = []

        for cell in self.cells:
            if(cell.get_val() == 0):
                for val in range(1, 10):
                    next_states.append(self.clone_and_replace_x(cell, val))
                break

        return next_states

    def clone_and_replace_x(self, cell, val):
        row_pos = cell.get_row()
        col_pos = cell.get_col()
        cloned_cells = []

        for c in self.cells:
            if(c.get_row() == row_pos and c.get_col() == col_pos):
                cloned_cells.append(Cell(row_pos, col_pos, val))
            else:
                cloned_cells.append(c.clone())

        return Board(cloned_cells)
