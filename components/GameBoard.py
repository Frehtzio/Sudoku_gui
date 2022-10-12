from cgi import print_arguments
import tkinter as tk
from tkinter.constants import FLAT
from components.Board import Board
from backend.backtracking import BackTracking
from screens.HomeScreen import HomeScreen

from style import styles
from tkinter import messagebox
# [["-1" for x in range(9)] for x in range(9)]

class GameBoard(tk.Frame):
    def __init__(self,parent,manager,board):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.backend = BackTracking
        
        
        # note self.board is self.manager.saved_numbers
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
                                            textvariable=self.board[r][c]
                                            )
                    else:
                        self.manager.btn_cells[r][c] = tk.Entry(self.frm_cell, width = 2, **styles.STYLEB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            textvariable=self.board[r][c].get()
                                            )
                        
                        
                    self.manager.btn_cells[r][c].grid(sticky='nsew')
        
                
        
        
        
        
      
      
    def update_options(self,new):
        for r in range(9):
            for c in range(9):
                if new[r][c].get() == "-1":
                    new[r][c].set('')
        self.board = new
        self.init_widget()
    
        
        
        
        
        
        
        
   