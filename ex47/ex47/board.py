from .player import Player

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

	def get_input(self, row: int, col: int) -> Player:
		return self.input_matrix[row][col]
