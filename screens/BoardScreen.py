
import tkinter as tk
from components.Board import Board
from style import styles

from components.MainMenu import MainMenu

class BoardScreen(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent,)
        
        self.manager = manager
        self.head = tk.StringVar()
        self.info = tk.StringVar()
        self.head.set("Press 'Enter' once you done")
        self.info.set("Range between(1,9) if not it will considere empty")
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()
        
    def init_widgets(self):
        tk.Label(
            self,
            textvariable=self.head,
            justify=tk.CENTER,
            # letras
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        tk.Label(
            self,
            textvariable=self.info,
            justify=tk.CENTER,
            # letras
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        # creat table 9x9
        
        self.board = Board(self,
              self.manager,self.manager.saved_numbers)
        self.board.pack(**styles.PACK)
        
        
        
        
