
import enum


class Player(enum.Enum):
	PLAYER_ONE = 1
	PLAYER_TWO = 2

	def __str__(self) -> str:
		if self == Player.PLAYER_ONE:
			return "A"
		else:
			return "B"
