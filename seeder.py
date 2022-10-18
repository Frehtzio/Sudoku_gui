from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models import Board,Unsolved,Solved,full
import datetime

def seeding():
    engine = create_engine(full)
    Session = sessionmaker(bind=engine)
    session = Session()
    board = [
        [-1, -1, -1,   -1, 4, 6,   5, -1, -1],
        [-1,-1,-1,   -1, -1, -1,    9,-1, -1],
        [-1, -1, 6,   -1, -1, 3,   -1, 2, -1],

        [-1, -1, 3,   -1, 8, -1,   -1, -1, -1],
        [-1, -1, -1,   4, -1, 9,   -1, 8, -1],
        [-1, 9, -1,   -1, -1, -1, -1, 6,-1],

        [7, -1, -1,    -1, 9, -1,   -1, -1, 5],
        [2  ,4, -1,    8, 1, -1,   -1, -1, -1],
        [-1, 5, -1,   -1, 3, -1,   -1, -1, -1]
    ]
    solved_board = [
        [3, 8, 2,   9, 4, 6,   5, 1, 7],
        [4, 7, 5,   1, 2, 8,   9, 3, 6],
        [9, 1, 6,   5, 7, 3,   8, 2, 4],

        [1, 6, 3,   2, 8, 7,   4, 5, 9],
        [5, 2, 7,   4, 6, 9,   3, 8, 1],
        [8, 9, 4,   3, 5, 1,   7, 6, 2],

        [7, 3, 8,   6, 9, 2,   1, 4, 5],
        [2 ,4, 9,   8, 1, 5,   6, 7, 3],
        [6, 5, 1,   7, 3, 4,   2, 9, 8]
    ]

    unsolved = [Unsolved(cell_idx =str(r)+","+str(c),cell_text = str(board[r][c])) for r in range(9) for c in range(9)] 
    solved = [Solved(cell_idx = str(r)+","+str(c),cell_text = str(solved_board[r][c])) for r in range(9) for c in range(9)] 

        
    board = Board(board_made = datetime.datetime.now(),unsolved=unsolved,solved=solved) 
        
    session.add(board)
    session.commit()
    