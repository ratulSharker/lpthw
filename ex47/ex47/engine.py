from .board import Board
from .canvas import Canvas
from .winner_calculator import WinnerCalculator
from .player import Player
from typing import Tuple

class Engine(object):

	def __init__(self, board_size: int):
		self.board = Board(board_size)
		self.canvas = Canvas(self.board)
		self.winner_calculator = WinnerCalculator(self.board)
		self.next_player_turn = Player.PLAYER_ONE # make it random
	
	def play(self):
		winner_player : Player = self.winner_calculator.calculate()
		game_tie = False
		while winner_player  == None and game_tie == False:
			self.canvas.clear()
			self.canvas.render()
			row, col = self.prompt_row_col_for_next_player() # re-think, how can this be tested ?

			self.board.take_input(row, col, self.next_player_turn)
			self.switch_player()
			self.canvas.render()

			winner_player = self.winner_calculator.calculate()
			game_tie = self.winner_calculator.calculate_is_game_tie()
		
		if game_tie:
			print("Game Tie")
		else:
			print(f"Player {winner_player} has win")

	def switch_player(self):
		if self.next_player_turn == Player.PLAYER_ONE:
			self.next_player_turn = Player.PLAYER_TWO
		else:
			self.next_player_turn = Player.PLAYER_ONE

	def prompt_row_col_for_next_player(self) -> Tuple[int, int]:		
		print(f"Input for Player {self.next_player_turn}")

		col = int(input(f"Enter the col number  (0 ~ {self.board.board_size - 1}) > "))
		row = int(input(f"Enter the row number  (0 ~ {self.board.board_size - 1}) > "))
		return (row, col)
