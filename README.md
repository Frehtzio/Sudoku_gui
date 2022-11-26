# Sudoku solver GUI

Sudoku solver is a GUI that solves sudoku puzzles and saves the solved sudoku puzzle so you can later play or delete them from memory.

## CS50
>This was my final project for conclude the CS50 Introduction to Computer Sciense course.

## Features
- [SQLAlchemy](https://www.sqlalchemy.org/)
## Explaining the project
| <img src="Screenshots/Screenshot from 2022-11-06 18-58-19.png" width="400">  |
### Play 
It will show you a list of dates to choose to play a table that you have in the database.
### Solve Sudoku 
Solves valid sudokus, if they are not well-formed an error message appears depending on the error that there is,
once a valid sudoku has been entered, the backtracking will begin, and then the frame will be changed, showing the solved table, the numbers
fixed will be black and non-fixed will be blue.
### Delete a sudoku
It will show you a list of dates to choose from to remove it from the database.
### Note
All the data are store in database/tests.db
if the database is empty the program will not work, you will need to run models.py and seeder.py

## Explaning the important folders/files
### Main file
main will run the file manager.
### manager file
manager controls everything it will handle the frame changes using the screens folder and it will use the database using the controller file.
### screens
screens contain all the frames to change the screen.
### components
components contain the childs frames that are used by the parent frames.
### Backtracking
In the Backtracking, there is a algorithm used by the program to solve sudoku puzzles.
## Sqlachemy and sqlite3:

I needed three tables for my database:

- First, table board. Where I put, id_board, board_made, notice that id_board must be a primary key here.

-Second, table solved. I put solved_id, cell_idx, cell_text, board_id,unsolved_id is a primary key,cell_idx is the position of a 9*9 (roc,column),cell_text,
is the value of the cell,board_id is the foreign key of id_board

-Three, is the same as second but with few changes

## Demonstration on youtube


