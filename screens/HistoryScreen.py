import tkinter as tk
from style import styles
from components.MainMenu import MainMenu
from components.SelectionOption import SelectOption
#
class HistoryScreen(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        self.configure(background=styles.BACKGROUND)
        self.manager = manager 
        self.option_list = self.manager.get_board_test()
        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text="Select the board that you want delete",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )

        tk.Label(
            self,
            text="Press 'Esc' to leave to go back ",
            justify=tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        self.options = SelectOption(
            self,
            self.manager,
            self.option_list
        ) 
        self.options.pack(
            **styles.PaCK
        
        )
        tk.Button(
            self,
            text="Press here",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            **styles.STYLE,
            command=lambda: self.manager.select_to_delete()
        ).pack(
            **styles.PACK   
        )

