
import tkinter as tk
from tkinter.constants import FLAT
from components.Board import Board
from backtracking.backtracking import BackTracking
from screens.HomeScreen import HomeScreen

from style import styles
from tkinter import messagebox


class GameBoard(tk.Frame):
    def __init__(self,parent,manager,board):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.backend = BackTracking
        self.boss = Board
        self.board = board
       
        
    def init_widget(self):
            for r in range(3):
                for c in range(3):
                    self.grid_columnconfigure(c,weight=1)
                    self.grid_rowconfigure(c,weight=1)
                    
                    self.manager.blocks[r][c] = tk.Frame(self,bd=2,highlightbackground='light blue',
                                        highlightcolor='light blue', highlightthickness=1)
                    self.manager.blocks[r][c].grid(row=r, column=c, sticky='nsew')
                    self.manager.blocks[r][c].grid_rowconfigure(0,weight=1)
                    self.manager.blocks[r][c].grid_columnconfigure(0,weight=1)
                    self.manager.blocks[r][c].grid_rowconfigure(1,weight=1)
                    self.manager.blocks[r][c].grid_columnconfigure(1,weight=1)
                    self.manager.blocks[r][c].grid_rowconfigure(2,weight=1)
                    self.manager.blocks[r][c].grid_columnconfigure(2,weight=1)
                
            
            for r in range(9):
                for c in range(9):
            # Add cell to the block
            # Add a frame so that the cell can form a square
                    self.frm_cell = tk.Frame(self.manager.blocks[r // 3][c // 3])
                    self.frm_cell.grid(row=(r % 3), column=(c % 3), sticky='nsew')
                    self.frm_cell.rowconfigure(0, minsize=50, weight=1)
                    self.frm_cell.columnconfigure(0, minsize=50, weight=1)
                    
                
                    if len(self.board[r][c].get()) > 0:
                        self.manager.btn_cells[r][c] = tk.Label(self.frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            text=self.board[r][c].get()
                                            )
                        
                    else:
                        self.manager.btn_cells[r][c] = tk.Entry(self.frm_cell, width = 2, **styles.STYLEB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            textvariable=self.board[r][c]
                                            )
                        
                        
                    self.manager.btn_cells[r][c].grid(sticky='nsew')
                    self.manager.btn_cells[r][c].bind('<Return>', self.check)
        
      
    def update_options(self,new):
        for r in range(9):
            for c in range(9):
                if new[r][c].get() == "-1":
                    new[r][c].set('')
        self.board = new
        self.init_widget()
    
    def check(self,event):
        board = self.board
        valid = self.valid_board(board)
        if valid == 1 :
            
            tk.messagebox.showinfo(
                title = "Congratulations",
                message="You solved this Sudoku"
            )
            self.manager.show_frame(HomeScreen)
            
        elif valid == 0:
            tk.messagebox.showinfo(
                title = "Error",
                message="This sudoku is not valid, there are repetitive numbers"
            )
        elif valid == 2:
            tk.messagebox.showinfo(
                title = "Error",
                message="there is a number bigger than 9"
            )
        else:
            tk.messagebox.showinfo(
                title = "Error",
                message="This sudoku is not completed"
            )
            

    def valid_board(self,puzzle):
        row = {i:set() for i in range(9)}
        col ={i:set() for i in range(9)}
        box = {i:set() for i in range(9)}
        # note if there is a letter or whatever it would considere as empty 
        # return 0 if sudoku is not valid
        # return 1 if is completle valid
        # return 2 if numbers if bigger than 9
        # return 3 if sudoku is not completed
        
        for r in range(9):
            for c in range(9):
                # will give error if a number is biger than 9
                if puzzle[r][c].get().isnumeric():
                    if int(puzzle[r][c].get()) > 9:
                        return 2
                    
                # if is not numeric it will consider a 0
                if not puzzle[r][c].get().isnumeric() in range(1,10):
                    continue
                
                # check row
                if puzzle[r][c].get() in row[r]:
                    return 0
                else:
                    row[r].add(puzzle[r][c].get())
                # check col
                if puzzle[r][c].get() in col[c]:
                    return 0
                else:
                    col[c].add(puzzle[r][c].get())
                # check box
                if puzzle[r][c].get() in box[(r//3)*3+(c//3)]:
                    return 0
                else:
                    box[(r//3)*3+(c//3)].add(puzzle[r][c].get())
                    
        for v in row.values():
            if len(v) != 9:
                return 3
        return 1
            
    
        
        
        
        
        
        
        
   