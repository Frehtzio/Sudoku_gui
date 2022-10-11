
from cgi import print_arguments
import tkinter as tk
from tkinter.constants import FLAT
from screens.HomeScreen import HomeScreen
from backend.backtracking import BackTracking


from style import styles
from tkinter import messagebox
import datetime


class Board(tk.Frame):
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
                
                """if str(self.test[i][j]):
                    self.manager.btn_cells[i][j] = tk.Label(frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                          highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                          text=self.test[i][j]
                                          )"""
                if True:
                    self.manager.btn_cells[i][j] = tk.Entry(frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                          highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                          textvariable=self.board[i][j]
                                          )
                    
                    
                self.manager.btn_cells[i][j].grid(sticky='nsew')
                self.manager.btn_cells[i][j].bind('<Return>', self.correctGrid)
      
    def back(self):
        
        self.clearAll()
        
    def correctGrid(self,event):
    
        board = self.board
        valid = self.valid_board(board)
        if valid:
            for i in range(9):
                for j in range(9):

                    if len(board[i][j].get()) > 1 or board[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                        self.manager.btn_cells[i][j].configure(**styles.STYLEB)
                        board[i][j].set('-1')
                    else:
                        self.manager.user_inputs[str(i)+""+str(j)] = board[i][j].get()
                            
                        
            
            self.solve(board)
        else:
            tk.messagebox.showinfo(
                title = "ERROR",
                message="This sudoku is not valid, there are repetitive numbers or invalid inputs"
            )
            
    def clearAll(self):
        # reset all 
        for i in range(9):
            for j in range(9):
                self.board[i][j].set('')
                try:
                    self.manager.btn_cells[i][j].configure(**styles.STYLEBB)
                except:
                    pass

        self.manager.user_inputs = {}
        self.focus()
        
        self.manager.show_frame(HomeScreen)
        
    def solve(self,board):
        self.backend(board)
       
        self.manager.controller.create_board(datetime.datetime.now(),board,self.manager.user_inputs)
        
        # change of frame
        self.manager.solved_board()
    
    def valid_board(self,puzzle):
        row = {i:set() for i in range(9)}
        col ={i:set() for i in range(9)}
        box = {i:set() for i in range(9)}
        # note if there is a letter or whatever it would considere as empty 
        
        for r in range(9):
            for c in range(9):
                # will give error if a number is biger than 9
                if puzzle[r][c].get().isnumeric():
                    if int(puzzle[r][c].get()) > 9:
                        return False
                    
                
                if not puzzle[r][c].get().isnumeric() in range(1,10):
                    
                    continue
                
                # check row
                if puzzle[r][c].get() in row[r]:
                    return False
                else:
                    row[r].add(puzzle[r][c].get())
                # check col
                if puzzle[r][c].get() in col[c]:
                    return False
                else:
                    col[c].add(puzzle[r][c].get())
                # check box
                if puzzle[r][c].get() in box[(r//3)*3+(c//3)]:
                    return False
                else:
                    box[(r//3)*3+(c//3)].add(puzzle[r][c].get())
                    
        return True
  
                
     
       


    
        