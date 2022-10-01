import random
from ai import AI

class RandomAI(AI):
	def __init__(self):
		pass

	def move(self, board):
		small_grid, big_grid = board.get_state()
		moves = self.get_moves(small_grid, big_grid)
		big_move = random.choice(list(moves.keys()))
		small_move = random.randint(0, len(moves[big_move])-1)
		board.make_move(small_move, big_move)
