import enum
import os
from typing import Tuple

# Tic-Tac-Toe Game

class Player(enum.Enum):
	PLAYER_ONE = 1
	PLAYER_TWO = 2

	def __str__(self) -> str:
		if self == Player.PLAYER_ONE:
			return "A"
		else:
			return "B"

class Board(object):

	def __init__(self, board_size: int):
		self.board_size = board_size
		self.input_matrix = [[None]*board_size for i in range(0, board_size)]

	def is_empty(self, row: int, col: int) -> bool:
		if row >= self.board_size or col >= self.board_size:
			raise Exception("Row or Col size cannot be greater than the board size")
		
		return True if self.input_matrix[row][col] == None else False
	
	def take_input(self, row: int, col: int, player: Player):
		try:
			if self.is_empty(row, col):
				self.input_matrix[row][col] = player
			else:
				print("Given input is already occupied")
		except Exception as err:
			print(err)

class Canvas(object):

	def __init__(self, board: Board):
		self.board = board
	
	def render(self):
		print(self.get_col_identifier(), end="\n") # column identifier

		for row in range(0, self.board.board_size):
			print(self.get_row_separator(), end="\n") # top of the row
			
			for col in range(0, self.board.board_size):
				input = self.board.input_matrix[row][col]
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

class WinnerCalculator(object):

	def __init__(self, board: Board):
		self.board = board

	def calculate(self) -> Player:
		return None

class Engine(object):

	def __init__(self, board_size: int):
		self.board = Board(board_size)
		self.canvas = Canvas(self.board)
		self.winner_calculator = WinnerCalculator(self.board)
		self.next_player_turn = Player.PLAYER_ONE # make it random
	
	def play(self):
		while self.winner_calculator.calculate() == None:
			self.canvas.clear()
			self.canvas.render()
			row, col = self.prompt_row_col_for_next_player()
			self.board.take_input(row, col, self.next_player_turn)
			self.switch_player()
			self.canvas.render()

	def switch_player(self):
		if self.next_player_turn == Player.PLAYER_ONE:
			self.next_player_turn = Player.PLAYER_TWO
		else:
			self.next_player_turn = Player.PLAYER_ONE

	def prompt_row_col_for_next_player(self) -> Tuple[int, int]:		
		print(f"Input for Player {self.next_player_turn}")

		# TODO: take row and column at once
		col = int(input(f"Enter the col number  (0 ~ {self.board.board_size - 1}) > "))
		row = int(input(f"Enter the row number  (0 ~ {self.board.board_size - 1}) > "))
		return (row, col)

board_size: int = int(input("Please enter the board size > "))
engine = Engine(board_size)
engine.play()