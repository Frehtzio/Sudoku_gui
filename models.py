
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean
import os

absolute_path = os.path.abspath(__file__)
full = "sqlite:///"+os.path.dirname(absolute_path)+"/database/tests.db"

base = declarative_base()

class Solved(base):
    __tablename__ = "solved"
    solved_id = Column(Integer,primary_key=True)
    cell_idx = Column(String(10))
    cell_text = Column(String(10))
    board_id =Column(Integer,ForeignKey("board.board_id",ondelete="CASCADE"))
    
    def __repr__(self) -> str:
        return f"solved board with the porpuse to see or delete the board"
    
    
    
class Unsolved(base):
    __tablename__ = "unsolved"
    unsolved_id = Column(Integer,primary_key=True)
    cell_idx = Column(String(10))
    cell_text = Column(String(10))
    board_id =Column(Integer,ForeignKey("board.board_id",ondelete="CASCADE"))
    
    def __repr__(self) -> str:
        return f"a board with few numbers"

class Board(base):
    __tablename__ = "board"
    board_id = Column(Integer,primary_key=True)
    board_made = Column(DateTime)
    unsolved = relationship("Unsolved",cascade="all,delete",backref=backref("board"))
    solved = relationship("Solved",cascade="all,delete",backref=backref("board"))
    
    def __repr__(self) -> str:
        return f"Board object: board_id: {self.board_id}.board_made: {self.board_made}"
    
    
    
    
if __name__ == "__main__":
    engine = create_engine(full,echo=True)
    base.metadata.create_all(engine)
   
    