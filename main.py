import time
import pygame
from board import Board, State
from random_ai import RandomAI

SIZE = (640, 640)

if __name__ == "__main__":
	first = True
	board = Board(SIZE)
	board.init(first=first)
	ai = RandomAI()

	running = True

	while running:
		if board.AI_turn():
			ai.move(board)
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
