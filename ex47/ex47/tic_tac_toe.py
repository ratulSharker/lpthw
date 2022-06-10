from .engine import Engine

# Tic-Tac-Toe Game
board_size: int = int(input("Please enter the board size > "))
engine = Engine(board_size)
engine.play()