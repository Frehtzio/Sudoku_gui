from readline import read_init_file
import tkinter as tk
from tokenize import String


class BackTracking():
    def __init__(self,board):
        self.board = board
        self.answer= self.solve_sudoku(self.board)
        
    def find_next_empty(self,puzzle):
        # find row,col from the puzzle with number -1 
        # return row,col if found if not return (None,None)

        for r in range(9):
            for c in range(9):
                if puzzle[r][c].get() == "-1":
                    return r,c
        return None,None

    def is_valid(self,puzzle,guess,row,col):
        # figure out if is valid 
        # return true if valid else False
        row_vals = puzzle[row]
        for each in row_vals:
            if guess == each.get():
                return False
        
        # now the columns
        
        col_vals= [puzzle[i][col] for i in range(9)]
        for each in col_vals:
            if guess == each.get():
              return False
        
        # and then the square
        # 3x3
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        
        
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if puzzle[r][c].get() == guess:
                    return False
                
        return True
        
    def solve_sudoku(self,puzzle):
        # solve sudoku using backtracking 
        # our puzzle is a list of list
        # return wheter if solution exist 
        # mutates puzzle to be a solution (if solution exist)
        
        # step 1_ choose somewhere on the puzzle to m
            # stet 3 check if is valid ake a move
        row,col = self.find_next_empty(puzzle)
        # step 1.1 if none the whe are done
        if row == None:
            return True
        
        # step 2 make gues (put number) 1,9
        for guess in range(1,10):
            if self.is_valid(puzzle,str(guess),row,col):
                # if true then mutate the puzzle
                puzzle[row][col].set(guess)
                # step 4 recursive call 
                if self.solve_sudoku(puzzle):
                    return True
                
            # step 5 if not valid OR if our guess does not solve the puzzle, then we need to 
            # backtrack and try a new number
           
            puzzle[row][col].set("-1")
            
            
        # step 6 if none of the number we try are the is unsolvable
        return False





        