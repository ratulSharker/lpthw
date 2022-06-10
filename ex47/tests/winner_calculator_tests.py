from nose.tools import *

from ex47.board import Board
from ex47.player import Player
from ex47.winner_calculator import WinnerCalculator

def test_row_wise_winner():
	calculator = init_winner_calculator_for_board_3_by_3()
	board = calculator.board

	# `A`, `A`, ` `
	# ` `, ` `, ` `
	# ` `, ` `, ` `
	board.take_input(0, 0, Player.PLAYER_ONE)
	board.take_input(0, 1, Player.PLAYER_ONE)

	eq_(calculator.calculate_row_wise_winner(0), None)
	eq_(calculator.calculate_row_wise_winner(1), None)
	eq_(calculator.calculate_row_wise_winner(2), None)

	# `A`, `A`, ` `
	# ` `, `A`, ` `
	# ` `, ` `, `A`
	board.take_input(1, 1, Player.PLAYER_ONE)
	board.take_input(2, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_row_wise_winner(0), None)
	eq_(calculator.calculate_row_wise_winner(1), None)
	eq_(calculator.calculate_row_wise_winner(2), None)

	# `A`, `A`, `A`
	# ` `, `A`, ` `
	# ` `, ` `, `A`
	board.take_input(0, 2, Player.PLAYER_ONE)
	
	eq_(calculator.calculate_row_wise_winner(0), Player.PLAYER_ONE)
	eq_(calculator.calculate_row_wise_winner(1), None)
	eq_(calculator.calculate_row_wise_winner(2), None)
	
def test_col_wise_winner():
	calculator = init_winner_calculator_for_board_3_by_3()
	board = calculator.board

	# ` `, ` `, `A`
	# ` `, ` `, `A`
	# ` `, ` `, ` `
	board.take_input(0, 2, Player.PLAYER_ONE)
	board.take_input(1, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_col_wise_winner(0), None)
	eq_(calculator.calculate_col_wise_winner(1), None)
	eq_(calculator.calculate_col_wise_winner(2), None)

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# `A`, ` `, ` `
	board.take_input(1, 1, Player.PLAYER_ONE)
	board.take_input(2, 0, Player.PLAYER_ONE)

	eq_(calculator.calculate_col_wise_winner(0), None)
	eq_(calculator.calculate_col_wise_winner(1), None)
	eq_(calculator.calculate_col_wise_winner(2), None)

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# `A`, ` `, `A`
	board.take_input(2, 2, Player.PLAYER_ONE)
	
	eq_(calculator.calculate_col_wise_winner(0), None)
	eq_(calculator.calculate_col_wise_winner(1), None)
	eq_(calculator.calculate_col_wise_winner(2), Player.PLAYER_ONE)

def test_first_diagonal_winner():
	calculator = init_winner_calculator_for_board_3_by_3()
	board = calculator.board

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, ` `
	board.take_input(0, 2, Player.PLAYER_ONE)
	board.take_input(1, 1, Player.PLAYER_ONE)
	board.take_input(1, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_first_diagonal_winner(), None)

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, `A`
	board.take_input(2, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_first_diagonal_winner(), None)


	# `A`, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, `A`
	board.take_input(0, 0, Player.PLAYER_ONE)

	eq_(calculator.calculate_first_diagonal_winner(), Player.PLAYER_ONE)

def test_second_diagonal_winner():
	calculator = init_winner_calculator_for_board_3_by_3()
	board = calculator.board

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, ` `
	board.take_input(0, 2, Player.PLAYER_ONE)
	board.take_input(1, 1, Player.PLAYER_ONE)
	board.take_input(1, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_second_diagonal_winner(), None)

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, `A`
	board.take_input(2, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_second_diagonal_winner(), None)


	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# `A`, ` `, `A`
	board.take_input(2, 0, Player.PLAYER_ONE)

	eq_(calculator.calculate_second_diagonal_winner(), Player.PLAYER_ONE)

def test_calculate_is_game_tie():
	calculator = init_winner_calculator_for_board_3_by_3()
	board = calculator.board

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, ` `
	board.take_input(0, 2, Player.PLAYER_ONE)
	board.take_input(1, 1, Player.PLAYER_ONE)
	board.take_input(1, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate_is_game_tie(), False)

	# `B`, `B`, `A`
	# ` `, `A`, `A`
	# ` `, ` `, `B`
	board.take_input(0, 0, Player.PLAYER_TWO)
	board.take_input(0, 1, Player.PLAYER_TWO)
	board.take_input(2, 2, Player.PLAYER_TWO)

	eq_(calculator.calculate_is_game_tie(), False)

	# `B`, `B`, `A`
	# `A`, `A`, `A`
	# `B`, `A`, `B`
	board.take_input(1, 0, Player.PLAYER_ONE)
	board.take_input(2, 0, Player.PLAYER_TWO)
	board.take_input(2, 1, Player.PLAYER_ONE)

	# It may seems, should return false, but we are 
	# designed to call this function, if nobody wins
	eq_(calculator.calculate_is_game_tie(), True)

def test_winner_calculator_calculate():
	calculator = init_winner_calculator_for_board_3_by_3()
	board = calculator.board

	# ` `, ` `, `A`
	# ` `, `A`, `A`
	# ` `, ` `, ` `
	board.take_input(0, 2, Player.PLAYER_ONE)
	board.take_input(1, 1, Player.PLAYER_ONE)
	board.take_input(1, 2, Player.PLAYER_ONE)

	eq_(calculator.calculate(), None)

	# `B`, `B`, `A`
	# ` `, `A`, `A`
	# ` `, ` `, `B`
	board.take_input(0, 0, Player.PLAYER_TWO)
	board.take_input(0, 1, Player.PLAYER_TWO)
	board.take_input(2, 2, Player.PLAYER_TWO)

	eq_(calculator.calculate(), None)

	# `B`, `B`, `A`
	# `A`, `A`, `A`
	# `B`, `A`, `B`
	board.take_input(1, 0, Player.PLAYER_ONE)
	board.take_input(2, 0, Player.PLAYER_TWO)
	board.take_input(2, 1, Player.PLAYER_ONE)

	eq_(calculator.calculate(), Player.PLAYER_ONE)

	# incorporate more scenarios


def init_winner_calculator_for_board_3_by_3():
	return WinnerCalculator(Board(3))