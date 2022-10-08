import tkinter as tk
from style import styles
from screens.HomeScreen import HomeScreen
from screens.BoardScreen import BoardScreen

from controller import Controller


class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Sudoku Solver")
        self.blocks = [[None for x in range(3)] for x in range(3)] 
        self.btn_cells = [[None for x in range(9)] for x in range(9)]
        self.saved_numbers = [[tk.StringVar() for x in range(1,10)] for x in range(1,10)] 
        self.controller = Controller()
        self.container = tk.Frame(self)
        self.container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        self.container.configure(
            background=styles.BACKGROUND
        )
        self.container.grid_columnconfigure(0,weight=1)
        self.container.grid_rowconfigure(0,weight=1)
        
        self.frames = {}
        pantallas = (HomeScreen,BoardScreen)
        
        
        for F in pantallas:
            frame = F(self.container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky=tk.NSEW)
            
        self.show_frame(HomeScreen)
        
        
    def show_frame(self,container):
        
            
        frame = self.frames[container]
        frame.tkraise()
        
    # change of frame
    def empty_board(self):
        self.show_frame(BoardScreen)
        
   
    
    

 
        
        
