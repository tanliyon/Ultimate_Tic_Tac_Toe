import time
import pygame
from board import Board
from utils.constants import State
from ai.random_ai import RandomAI
from ai.minimax_ai import MinimaxAI

SIZE = (640, 640)

if __name__ == "__main__":
	first = True
	board = Board(SIZE)
	board.init(first=first)
	rand_ai = RandomAI()
	minimax_ai = MinimaxAI(4)

	running = True

	while running:
		if board.AI_turn() and board.isrunning():
			minimax_ai.move(board)
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running=False
				elif event.type == pygame.KEYDOWN and not board.isrunning():
					board.init(first)

				board.process_clicks(event)

			if not board.isrunning():
				first = not first
				board.endgame()

		time.sleep(0.1)

	pygame.quit()
