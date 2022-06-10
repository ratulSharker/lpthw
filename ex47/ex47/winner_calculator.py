from ex47.board import Board
from ex47.player import Player


class WinnerCalculator(object):

	def __init__(self, board: Board):
		self.board = board

	def calculate(self) -> Player:
		for row_or_col in range(0, self.board.board_size):

			row_result = self.calculate_row_wise_winner(row_or_col)
			if row_result != None:
				return row_result

			col_result = self.calculate_col_wise_winner(row_or_col)
			if col_result != None:
				return col_result

			first_diagonal_result = self.calculate_first_diagonal_winner()
			if first_diagonal_result != None:
				return first_diagonal_result
			
			second_diagonal_result = self.calculate_second_diagonal_winner()
			if second_diagonal_result != None:
				return second_diagonal_result

		return None

	def calculate_row_wise_winner(self, row: int) -> Player:
		board_size = self.board.board_size
		col_0_row_x_player_input = self.board.get_input(row, 0)

		if col_0_row_x_player_input == None:
			return None

		for col in range(1, board_size):
			if self.board.get_input(row, col) != col_0_row_x_player_input:
				return None

		return col_0_row_x_player_input
	
	def calculate_col_wise_winner(self, col) -> Player:
		board_size = self.board.board_size
		col_x_row_0_player_input = self.board.get_input(0, col)

		if col_x_row_0_player_input == None:
			return None

		for row in range(1, board_size):
			if self.board.get_input(row, col) != col_x_row_0_player_input:
				return None

		return col_x_row_0_player_input

	def calculate_first_diagonal_winner(self) -> Player:
		col_0_row_0_player = self.board.get_input(0, 0)

		if col_0_row_0_player == None:
			return None
		
		for row_col in range(1, self.board.board_size):
			col_x_row_x_player = self.board.get_input(row_col, row_col)

			if col_0_row_0_player != col_x_row_x_player:
				return None
		
		return col_0_row_0_player
	
	def calculate_second_diagonal_winner(self) -> Player:
		last_row_index = self.board.board_size - 1
		col_0_row_last_player = self.board.get_input(last_row_index, 0)

		if col_0_row_last_player == None:
			return None

		for index in range(1, self.board.board_size):
			col = index
			row = last_row_index - index
			col_0_row_x_player = self.board.get_input(row, col)

			if col_0_row_last_player != col_0_row_x_player:
				return None

		return col_0_row_last_player

	def calculate_is_game_tie(self) -> bool:
		# Very trivial implementation of saying draw
		for row in range(0, self.board.board_size):
			for col in range(0, self.board.board_size):
				player_input = self.board.get_input(row, col)
				if player_input == None:
					return False
		return True
