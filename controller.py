
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models import Solved, Unsolved,Board,full
from sqlite3 import ProgrammingError
import tkinter as tk

class Controller:
    def __init__(self):
        engine = create_engine(full)
        
        Session = sessionmaker(bind=engine)
        self.session = Session()
        

    def create_board(self,board_made,solved,unsolved):
        
        solve = []
        for i in solved:
            for s in i:
                solve.append(s.get())
        iter_solved = iter(solve)
        
        lista = [[tk.StringVar() for x in range(1,10)] for x in range(1,10)] 
        for key,value in unsolved.items():

            r,c = int(key[0]),int(key[1])
            lista[r][c].set(str(value))
          

        unsolve = []
        for r in range(9):
            for c in range(9):
                if len(lista[r][c].get()) > 0:
                    unsolve.append(lista[r][c].get())
                else:
                    unsolve.append("-1")
        
        iter_unsolved = iter(unsolve)

        unsolved = [Unsolved(cell_idx =str(r)+","+str(c),cell_text = next(iter_unsolved)) for r in range(1,10) for c in range(1,10)] 
        solved = [Solved(cell_idx = str(r)+","+str(c),cell_text = str(next(iter_solved))) for r in range(1,10) for c in range(1,10)] 
      
        new_board = Board(board_made = board_made,unsolved=unsolved,solved=solved)
        self.session.add(new_board)
        self.session.commit()
            
            
    
    def get_board_date(self):
        boards = self.session.query().with_entities(Board.board_made).all()
        #print(boards)
        board_date = [board[0] for board in boards]
        return board_date[::-1]
    
    def get_board_play(self,board_made):
        board = self.session.query(Board).filter(Board.board_made == board_made).first() 
        return board.unsolved
    
    
   

"""
if __name__ == "__main__":
    c = Controller()
    c.get_test_names()"""
            
        
        
    
    
