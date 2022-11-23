import math,random
from cell import Cell

class Board:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

    '''

    # width
    # height
    # screen
    # difficulty
    
    
    '''
    Constructor for the Board class.
    screen is a window from PyGame.
    difficulty is a variable to indicate if the user chose easy, medium, or hard.
    '''
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        pass


    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes. Draws every cell on this board.
    def draw(self): 
        pass
 
    
    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.
    def select(self, row, col):
        pass


    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col) of the cell which was clicked. Otherwise, this function returns None.
    def click(self, x, y):
        pass


    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are filled by themselves.
    def clear(self):
        pass


    # Sets the sketched value of the current selected cell equal to user entered value. It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        pass


    # Sets the value of the current selected cell equal to user entered value. Called when the user presses the Enter key.
    def place_number(self, value):  
        pass


    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
    def reset_to_original(self):
        pass


    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        pass


    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        pass


    #Finds an empty cell and returns its row and col as a tuple (x, y).
    def find_empty(self):
        pass


    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        pass

        