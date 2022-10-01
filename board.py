import sys, pygame
import constants
from constants import State
from utils import win, draw

class Board:
	def __init__(self, size):
		pygame.init()
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption('Ultimate Tic-Tac-Toe')
		self.size = self.W, self.H = size

	def init(self, first):
		self.screen.fill(constants.WHITE)

		# Draw main 4 bold lines
		for i in range(1,3):
			pygame.draw.line(self.screen, constants.BLACK, ((self.W*i)//3, 0), ((self.W*i)//3, self.H), 5)
			pygame.draw.line(self.screen, constants.BLACK, (0, (self.H*i)//3), (self.W, (self.H*i)//3), 5)

		# Draw mini lines
		lst = [1, 2, 4, 5, 7, 8]
		for i in lst:
			pygame.draw.line(self.screen, constants.BLACK, ((self.W*i)//9, 0), ((self.W*i)//9, self.H), 1)
			pygame.draw.line(self.screen, constants.BLACK, (0, (self.H*i)//9), (self.W, (self.H*i)//9), 1)

		self.turn = State.X if first else State.O
		self.big_grid = [State.VALID for _ in range(9)]
		self.small_grid = [[State.VALID for _ in range(9)] for _ in range(9)]
		self.winner = State.VALID

		pygame.display.flip()

	def process_clicks(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			x, y = pygame.mouse.get_pos()
			small_grid, big_grid = self._get_grid(x, y)
			self.make_move(small_grid, big_grid)
			
	def make_move(self, small_grid, big_grid):
		if self.big_grid[big_grid] == State.VALID and self.small_grid[big_grid][small_grid] == State.VALID:
			x = (big_grid%3 * self.W//3) + (small_grid%3 * self.W//9)
			y = (big_grid//3 * self.H//3) + (small_grid//3 * self.H//9)

			if self.turn == State.X:
				pygame.draw.line(self.screen, constants.X_COL, (x+constants.OFFSET, y+constants.OFFSET), (x+(self.W//9)-constants.OFFSET, y+(self.H//9)-constants.OFFSET), 2)
				pygame.draw.line(self.screen, constants.X_COL, (x+constants.OFFSET, y+(self.H//9)-constants.OFFSET), (x+(self.W//9)-constants.OFFSET, y+constants.OFFSET), 2)
			else:
				pygame.draw.circle(self.screen, constants.O_COL, (x+(self.W//18), y+(self.H//18)), (self.W//18)-constants.OFFSET, 2)

			self._update_board(small_grid, big_grid)
			if win(self.big_grid, big_grid, self.turn):
				self.winner = self.turn
			elif draw(self.big_grid):
				self.winner = State.DRAW

			self.turn = State.X if self.turn == State.O else State.O
			pygame.display.flip()

	def endgame(self):
		font1 = pygame.font.Font('freesansbold.ttf', 64)
		text1 = font1.render('Game Over!', True, constants.BLACK, constants.WHITE)
		textRect1 = text1.get_rect()

		if self.winner == State.X:
			winner = "X"
		elif self.winner == State.O:
			winner = "O"
		else:
			winner = "No one"

		font2 = pygame.font.Font('freesansbold.ttf', 25)
		text2 = font2.render(winner + ' won the game', True, constants.BLACK, constants.WHITE)
		textRect2 = text2.get_rect()

		self.screen.blit(text1, (self.W//2 - textRect1.width//2, self.H//2 - textRect1.height//2 - 23))
		self.screen.blit(text2, (self.W//2 - textRect2.width//2, self.H//2 - textRect2.height//2 + 23))
		pygame.display.flip()

	def get_state(self):
		return self.small_grid, self.big_grid

	def isrunning(self):
		return self.winner == State.VALID or self.winner == State.INVALID

	def AI_turn(self):
		return self.turn == State.O

	def _update_board(self, small_grid, big_grid):
		self.small_grid[big_grid][small_grid] = self.turn

		# Check if a certain big_grid is won
		win_status = win(self.small_grid[big_grid], small_grid, self.turn)
		if win_status:
			self._draw_win(win_status, small_grid, big_grid)
			self.big_grid[big_grid] = self.turn

		# Check if the big_grid is drawn
		elif draw(self.small_grid[big_grid]):
			self.big_grid[big_grid] = State.DRAW

		# Limit play to only the big grid selected by the small grid
		if self.big_grid[small_grid] == State.VALID or self.big_grid[small_grid] == State.INVALID:
			for i in range(9):
				if i == small_grid:
					self.big_grid[i] = State.VALID
				elif self.big_grid[i] == State.X or self.big_grid[i] == State.O or self.big_grid[i] == State.DRAW:
					continue
				else:
					self.big_grid[i] = State.INVALID

		# If the big grid is won, the other player can play at any big grid
		else:
			for i in range(9):
				if self.big_grid[i] == State.X or self.big_grid[i] == State.O or self.big_grid[i] == State.DRAW:
					continue
				else:
					self.big_grid[i] = State.VALID

	def _get_grid(self, x, y):
		row = y // (self.W // 9)
		column = x // (self.H // 9)
		small_grid = (row%3)*3 + column%3
		big_grid = (row//3)*3 + column//3
		return small_grid, big_grid

	def _draw_win(self, win, small_grid, big_grid):
		x = (big_grid%3 * self.W//3) + (small_grid%3 * self.W//9)
		y = (big_grid//3 * self.H//3) + (small_grid//3 * self.H//9)
		color = constants.X_COL if self.turn == State.X else constants.O_COL
		offset = constants.OFFSET//2

		if win == "row":
			x -= small_grid%3 * self.W//9
			y += self.H // 18
			pygame.draw.line(self.screen, color, (x+offset, y), (x+(self.W//3)-offset, y), 4)
		elif win == "col":
			y -= (small_grid//3 * self.H//9)
			x += self.W // 18
			pygame.draw.line(self.screen, color, (x, y+offset), (x, y+(self.H//3)-offset), 4)
		elif win == "/_diag":
			x -= small_grid%3 * self.W//9
			y -= small_grid//3 * self.H//9
			pygame.draw.line(self.screen, color, (x+offset, y+(self.H//3)-offset), (x+(self.W//3)-offset, y+offset), 4)
		else:
			x -= small_grid%3 * self.W//9
			y -= small_grid//3 * self.H//9
			pygame.draw.line(self.screen, color, (x+offset, y+offset), (x+(self.W//3)-offset, y+(self.H//3)-offset), 4)

