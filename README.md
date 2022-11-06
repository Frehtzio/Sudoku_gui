# Sudoku solver GUI

Sudoku solver is a GUI that solves sudoku puzzles and saves the solved sudoku puzzle so you can later play or delete them from memory.

## CS50
>This was my final project for conclude the CS50 Introduction to Computer Sciense course.

## Features
- [SQLAlchemy](https://www.sqlalchemy.org/)
## Explaining the project
| <img src="Screenshots/Screenshot from 2022-11-06 18-58-19.png" width="400" height ="200">  |
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
if the database is empty the program will not word you will need to run models.py and seeder.py

## Explaning the important folders/files
### Main file
main will run the file manager.
### manager file
manager controls everything it will handle the frame changes using the screens folder and it will use the database using the controller file.
### screens
screens contain all the frames to change the screen.
### components
components contain the childs frames that are used by the parent frames.
### Backend
In the backend, there is backtracking, which is the algorithm used by the program to solve sudoku puzzles.




