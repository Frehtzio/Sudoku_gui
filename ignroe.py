
from cgi import print_arguments
import tkinter as tk
from tkinter.constants import FLAT
from screens.HomeScreen import HomeScreen
from backend.backtracking import BackTracking


from style import styles
from tkinter import messagebox


class GameBoard(tk.Frame):
    def __init__(self,parent,manager,board,test=[["-1" for x in range(9)] for x in range(9)]):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.test = test
        self.backend = BackTracking
        
        # note self.board is self.manager.saved_numbers
        self.board = board
        
        self.back()
        self.manager.bind('<Escape>', lambda e: self.back())
        for i in range(3):
            for j in range(3):
                self.grid_columnconfigure(j,weight=1)
                self.grid_rowconfigure(i,weight=1)
                
                self.manager.blocks[i][j] = tk.Frame(self,bd=2,highlightbackground='light blue',
                                    highlightcolor='light blue', highlightthickness=1)
                self.manager.blocks[i][j].grid(row=i, column=j, sticky='nsew')
                self.manager.blocks[i][j].grid_rowconfigure(0,weight=1)
                self.manager.blocks[i][j].grid_columnconfigure(0,weight=1)
                self.manager.blocks[i][j].grid_rowconfigure(1,weight=1)
                self.manager.blocks[i][j].grid_columnconfigure(1,weight=1)
                self.manager.blocks[i][j].grid_rowconfigure(2,weight=1)
                self.manager.blocks[i][j].grid_columnconfigure(2,weight=1)
               
        
        for i in range(9):
            for j in range(9):
        # Add cell to the block
        # Add a frame so that the cell can form a square
                frm_cell = tk.Frame(self.manager.blocks[i // 3][j // 3])
                frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
                frm_cell.rowconfigure(0, minsize=50, weight=1)
               
                frm_cell.columnconfigure(0, minsize=50, weight=1)
               
                if len(self.test[i][j]):
                    
                    self.manager.btn_cells[i][j] = tk.Label(frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                          highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                          text=self.test[i][j]
                                          )
                else:
                    self.manager.btn_cells[i][j] = tk.Entry(frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                          highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                          textvariable=self.board[i][j]
                                          )
                    
                    
                self.manager.btn_cells[i][j].grid(sticky='nsew')
                self.manager.btn_cells[i][j].bind('<Return>', self.correctGrid)
      
      
      
      
      
