import tkinter as tk
from style import styles
from screens.HomeScreen import HomeScreen
from screens.BoardScreen import BoardScreen 
from screens.SolvedScreen import SolvedScreen
from screens.SelectBoard import SelectBoard
from screens.PlayBoard import PlayBoard
from backend.backtracking import BackTracking


from controller import Controller


class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Sudoku Solver")
        self.blocks = [[None for x in range(3)] for x in range(3)] 
        self.btn_cells = [[None for x in range(9)] for x in range(9)]
        self.saved_numbers = [[tk.StringVar() for x in range(1,10)] for x in range(1,10)] 
        self.user_inputs = {}
        self.selected_board = ""
        self.board_to_play =""
        
        
        self.backend = BackTracking
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
        pantallas = (HomeScreen,BoardScreen,PlayBoard,SolvedScreen,SelectBoard)
        
        
        for F in pantallas:
            frame = F(self.container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky=tk.NSEW)
            
        self.show_frame(HomeScreen)
        
        
    def show_frame(self,container):
            
        frame = self.frames[container]
        frame.tkraise()
        
    # change of frame
    def board_play(self):
        new_options = self.get_board_test()
        self.frames[SelectBoard].options.update_options(new_options)
        self.show_frame(SelectBoard)
        
    def empty_board(self):
        
        self.bind('<Escape>', lambda e: self.clearAll())
        #self.frames[BoardScreen].board.init()
        self.show_frame(BoardScreen)
   
    
    def solved_board(self):
        self.bind('<Escape>', lambda e: self.clearAll())
        self.frames[SolvedScreen].label.init_widgets()
        self.show_frame(SolvedScreen)
    
    def select_to_execute(self):
        self.bind('<Escape>', lambda e: self.clearAll())
        self.selected_board = self.frames[SelectBoard].options.selected.get()
        if len(self.selected_board) != 0:
            self.focus()        
            self.board_to_play = self.get_board()
            
            self.frames[PlayBoard].board.update_options(self.board_to_play)
            self.show_frame(PlayBoard)

 
    # BBDD base of datos
    
    def get_board_test(self):
        return self.controller.get_board_date()
    
    def add_board(self,test_name,quesiton_text,question_choices,correct_choice):
        self.controller.add_question(test_name,quesiton_text,question_choices,correct_choice)
        
    
    def get_board(self):
        # para luego 
        if self.selected_board != "":
            board = self.controller.get_board_play(self.selected_board)
            a = [b.cell_text for b in board]
            iter_a = iter(a)
            lista = [[tk.StringVar() for x in range(1,10)] for x in range(1,10)] 
            for r in range(9):
                for c in range(9):
                    lista[r][c].set(next(iter_a))
            return lista
            
            
    def clearAll(self):
        # reset all 
        for i in range(9):
            for j in range(9):
                self.saved_numbers[i][j].set('')
                try:
                    self.btn_cells[i][j].configure(**styles.STYLEBB)
                except:
                    pass

        self.user_inputs = {}
        self.focus()
    
        self.show_frame(HomeScreen)
        
            
            
    

        
    

 
        
        
