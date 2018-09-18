__author__ = "Connor Valerio"


class Cell:

    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.poss_vals = []
        self.col_neighbours = []
        self.row_neighbours = []
        self.square_neighbours = []
        self.solved = False

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def get_poss_vals(self):
        return self.poss_vals

    def add_poss_val(self, val):
        self.poss_vals.append(val)

    def remove_poss_val(self, val):
        self.poss_vals.remove(val)

    def get_col_neighbours(self):
        return self.col_neighbours

    def set_col_neighbours(self, neighbours):
        self.col_neighbours = neighbours

    def get_row_neighbours(self):
        return self.row_neighbours

    def set_row_neighbours(self, neighbours):
        self.row_neighbours = neighbours

    def get_square_neighbours(self):
        return self.square_neighbours

    def set_square_neighbours(self, neighbours):
        self.square_neighbours = neighbours

    def is_solved(self):
        return self.solved

    def set_solved(self):
        self.solved = True

    def is_equal_to(self, cell):
        if(self.row == cell.get_row() and self.col == cell.get_col()):
            return True
        return False

    def clone(self):

        row = self.row
        col = self.col
        val = self.val

        row_neighbours = self.row_neighbours
        col_neighbours = self.col_neighbours
        square_neighbours = self.square_neighbours

        cell = Cell(row, col, val)
        cell.set_row_neighbours(row_neighbours)
        cell.set_col_neighbours(col_neighbours)
        cell.set_square_neighbours(square_neighbours)

        return cell
