from nose.tools import *

from ex47.player import Player
from ex47.board import Board

def tests_board_init():
	board = Board(10)
	eq_(board.board_size, 10)

def tests_take_input_get_input():
	board = Board(3)
	board.take_input(0, 0, Player.PLAYER_ONE)
	board.take_input(1, 1, Player.PLAYER_TWO)

	eq_(board.get_input(0, 0), Player.PLAYER_ONE)
	eq_(board.get_input(0, 1), None)
	eq_(board.get_input(1, 0), None)
	eq_(board.get_input(1, 1), Player.PLAYER_TWO)

def tests_take_input_is_empty():
	board = Board(3)
	board.take_input(0, 0, Player.PLAYER_ONE)
	board.take_input(1, 1, Player.PLAYER_TWO)

	eq_(board.is_empty(0, 0), False)
	eq_(board.is_empty(0, 1), True)
	eq_(board.is_empty(1, 0), True)
	eq_(board.is_empty(1, 1), False)
