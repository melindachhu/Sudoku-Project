import math,random

class Cell:
    value
    row
    col
    screen

    # Constuctor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        pass

    # setter
    def set_cell_value(self, value):
        this.value = value
        pass


    # setter for sketched value
    def set_sketched_value(self, value):
        this.screen = value
        pass

    
    def draw(self):
        '''
        Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed. Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected.
        '''
 