from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models import Board,Unsolved,Solved,full
import datetime

if __name__ == "__main__":
    engine = create_engine(full)
    Session = sessionmaker(bind=engine)
    session = Session()
    

    unsolved = [Unsolved(cell_idx =str(r)+","+str(c),cell_text = str(-1)) for r in range(1,10) for c in range(1,10)] 
    solved = [Solved(cell_idx = str(r)+","+str(c),cell_text = str(r+c)) for r in range(1,10) for c in range(1,10)] 

        
    board = Board(board_made = datetime.datetime.now(),unsolved=unsolved,solved=solved) 
        
    session.add(board)
    session.commit()
    