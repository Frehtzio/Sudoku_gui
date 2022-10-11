import tkinter as tk
from tkinter.constants import FLAT
from style import styles


class MainMenu(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background=styles.BACKGROUND
        )
        self.init_widgets()
        
        
    def init_widgets(self):
        tk.Button(
            self,
            text="Play",
            command=lambda:self.manager.board_play(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
        
        tk.Button(
            self,
            text="Sudoku Solver",
            command=lambda:self.manager.empty_board(),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )
    
        
        tk.Button(
            self,
            text="Delete a Sudoku",
            command=lambda:print("Eliminar"),
            **styles.STYLE,
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT
        ).pack(
            **styles.PACK
        )