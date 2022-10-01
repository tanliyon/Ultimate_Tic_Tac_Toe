from ai import AI
from constants import State
import copy
import numpy as np
import random

class MinimaxAI(AI):
	def __init__(self, depth):
		self.depth = depth
		self.initial_val = None

	def move(self, board):
		small_grid, big_grid = board.get_state()
		_, best_move = self.branch(small_grid, big_grid, True, self.depth)
		small_move, big_move = best_move
		board.make_move(small_move, big_move)

	def branch(self, small_grid, big_grid, mx, depth):
		if depth == 0:
			value = self.evaluate(small_grid, big_grid)
			return value, None

		moves = self.get_moves(small_grid, big_grid)
		turn = State.O if mx else State.X
		minmax_val = None
		best_move = None

		for (big_move, lst) in moves.items():
			for small_move in lst:
				print(minmax_val, best_move)
				big_grid_cpy = copy.deepcopy(big_grid)
				small_grid_cpy = copy.deepcopy(small_grid)
				winner = self.make_move(small_move, big_move, small_grid_cpy, big_grid_cpy, turn)
				if winner:
					value = self.evaluate(small_grid_cpy, big_grid_cpy)
					minmax_val, best_move = self.update(minmax_val, best_move, value, (small_move, big_move), mx)
					return minmax_val, best_move
				else:
					value, _ = self.branch(small_grid_cpy, big_grid_cpy, not mx, depth-1)
					minmax_val, best_move = self.update(minmax_val, best_move, value, (small_move, big_move), mx)

		if minmax_val == self.initial_val:
			big_move = random.choice(list(moves.keys()))
			small_move = random.randint(0, len(moves[big_move])-1)
			best_move = (small_move, big_move)

		return minmax_val, best_move

	def update(self, minmax_val, best_move, value, move, mx):
		if minmax_val == None:
			self.initial_val = value
			minmax_val = value
			best_move = move
			return minmax_val, best_move

		if mx and value > minmax_val:
			minmax_val = value
			best_move = move

		elif not mx and value < minmax_val:
			minmax_val = value
			best_move = move

		return minmax_val, best_move

