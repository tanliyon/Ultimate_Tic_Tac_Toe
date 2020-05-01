import random

class RandomAI():
	def __init__(self):
		pass

	def move(self, board):
		moves = board.get_moves()
		big_grid = random.choice(list(moves.keys()))
		small_grid = random.randint(0, len(moves[big_grid])-1)
		board.make_move(small_grid, big_grid)
