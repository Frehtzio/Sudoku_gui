
from cgi import print_arguments
from mimetypes import init
import tkinter as tk
from tkinter.constants import FLAT
from screens.HomeScreen import HomeScreen
from backtracking.backtracking import BackTracking


from style import styles
from tkinter import messagebox


class LabelBoard(tk.Frame):
    # main diference between this and Board.py
    # is the value of self.board , the Label insted of Entry , the text instead of textvariable and the functions calls
    def __init__(self,parent,manager,board,user_inputs):
        super().__init__(parent)
        self.parent = parent
        self.manager = manager
        self.board = board
        self.solved = None
        self.user_inputs = user_inputs
        
        self.init_widgets()
        
        
        
    def init_widgets(self):
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

                frm_cell = tk.Frame(self.manager.blocks[i // 3][j // 3])
                frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
                frm_cell.rowconfigure(0, minsize=50, weight=1)
                frm_cell.columnconfigure(0, minsize=50, weight=1)
                
                if self.manager.btn_cells[i][j].cget("fg") == "#0066FF":
                    
                    self.manager.btn_cells[i][j] = tk.Label(frm_cell, width = 2, **styles.STYLEB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            textvariable=self.board[i][j]
                                            )
                else:
                    
                    self.manager.btn_cells[i][j] = tk.Label(frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            textvariable=self.board[i][j]
                                            )
                    
                self.manager.btn_cells[i][j].grid(sticky='nsew')
                
    def history_widget(self):
        
        
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
                frm_cell = tk.Frame(self.manager.blocks[i // 3][j // 3])
                frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
                frm_cell.rowconfigure(0, minsize=50, weight=1)
                frm_cell.columnconfigure(0, minsize=50, weight=1)
          
                if self.board[i][j].get() == self.solved[i][j].get():
                     self.manager.btn_cells[i][j] = tk.Label(frm_cell, width = 2, **styles.STYLEBB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            textvariable=self.solved[i][j]
                                            )
                else:
                    
                    self.manager.btn_cells[i][j] = tk.Label(frm_cell, width = 2, **styles.STYLEB,  cursor = 'arrow', borderwidth = 1,
                                            highlightcolor = 'black', highlightthickness = 1, highlightbackground = 'black',justify='center',
                                            textvariable=self.solved[i][j]
                                            )
                    
                self.manager.btn_cells[i][j].grid(sticky='nsew')
               
        self.btn_funcid = self.manager.bind('4',lambda e :  self.kill())
        
    
    def delete(self,unsolved,solved):
        for r in range(9):
            for c in range(9):
                if unsolved[r][c].get() == "-1":
                    unsolved[r][c].set('')
        self.board = unsolved
        self.solved = solved
        self.history_widget()
        
    def kill(self):
        # this would delete only self.btn_funcid
        self.manager.unbind("<Return>", self.btn_funcid)
        
        self.manager.delete_board(self.manager.selected_board)
        self.manager.show_frame(HomeScreen)