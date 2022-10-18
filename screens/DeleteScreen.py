
import tkinter as tk
from components.LabelBoard import LabelBoard
from style import styles

from components.MainMenu import MainMenu

class DeleteScreen(tk.Frame):
    def __init__(self,parent,manager):
        super().__init__(parent)
        
        self.manager = manager
        self.head = tk.StringVar()
        self.info = tk.StringVar()
        self.head.set("Delete Board from history")
        self.info.set("Press '4' to delete ")
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()
        
    def init_widgets(self):
      
        tk.Label(
            self,
            textvariable=self.head,
            justify=tk.CENTER,
    
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
        tk.Label(
            self,
            textvariable=self.info,
            justify=tk.CENTER,
  
            **styles.STYLE
        ).pack(
            **styles.PACK
        )
      
        
        self.label = LabelBoard(self,
              self.manager,self.manager.saved_numbers,self.manager.user_inputs)
        self.label.pack(**styles.PACK)
        
        
        