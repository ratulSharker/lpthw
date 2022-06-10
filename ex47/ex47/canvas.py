
import os
from .player import Player
from .board import Board


class Canvas(object):

	def __init__(self, board: Board):
		self.board = board
	
	def render(self):
		print(self.get_col_identifier(), end="\n") # column identifier

		for row in range(0, self.board.board_size):
			print(self.get_row_separator(), end="\n") # top of the row
			
			for col in range(0, self.board.board_size):
				input = self.board.get_input(row, col)
				if input == None:
					print("|   |", end="")
				elif input == Player.PLAYER_ONE:
					print("| A |", end="")
				elif input == Player.PLAYER_TWO:
					print("| B |", end="")
			print(f" {row}")
			
		print(self.get_row_separator(), end="\n") # bottom of the row

	def get_row_separator(self) -> str:
		return "+===+" * self.board.board_size
	
	def get_col_identifier(self) -> str:
		str = ""
		for col in range(0, self.board.board_size):
			str += f"  {col}  "
		return str

	def clear(self):
		os.system("cls" if os.name == 'nt' else 'clear')
