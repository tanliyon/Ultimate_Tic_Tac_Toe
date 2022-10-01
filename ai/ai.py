from utils.constants import State
from utils import win, draw

class AI:
	def __init__(self):
		pass

	def move(self, board):
		pass

	def get_moves(self, small_grid, big_grid):
		moves = {}

		for i in range(9):
			if big_grid[i] == State.VALID:
				moves[i] = []
				for j in range(9):
					if small_grid[i][j] == State.VALID:
						moves[i].append(j)

		return moves

	def make_move(self, small_move, big_move, small_grid, big_grid, turn):
		if big_grid[big_move] == State.VALID and small_grid[big_move][small_move] == State.VALID:

			small_grid[big_move][small_move] = turn

			# Check if a certain big_grid is won
			if win(small_grid[big_move], small_move, turn):
				big_grid[big_move] = turn

			# Check if the big_grid is drawn
			elif draw(small_grid[big_move]):
				big_grid[big_move] = State.DRAW

			# Limit play to only the big grid selected by the small grid
			if big_grid[small_move] == State.VALID or big_grid[small_move] == State.INVALID:
				for i in range(9):
					if i == small_move:
						big_grid[i] = State.VALID
					elif big_grid[i] == State.X or big_grid[i] == State.O or big_grid[i] == State.DRAW:
						continue
					else:
						big_grid[i] = State.INVALID

			# If the big grid is won, the other player can play at any big grid
			else:
				for i in range(9):
					if big_grid[i] == State.X or big_grid[i] == State.O or big_grid[i] == State.DRAW:
						continue
					else:
						big_grid[i] = State.VALID

			if win(big_grid, big_move, turn):
				big_grid[big_move] = turn
				return turn
			elif draw(big_grid):
				big_grid[big_move] = State.DRAW
				return State.DRAW
			else:
				return None

		else:
			print(big_grid)
			print(small_grid[big_move])
			print(big_move, small_move)
			raise ValueError("Invalid move")

	def evaluate(self, small_grid, big_grid):
		value = 0
		corner = [0, 2, 6, 8]
		center = 4

		for i in range(9):
			if big_grid[i] == State.O:
				if i == center:
					value += 10
				elif i in corner:
					value += 7
				else:
					value += 3
			elif big_grid[i] == State.X:
				if i == center:
					value -= 10
				elif i in corner:
					value -= 7
				else:
					value -= 3

		return value




