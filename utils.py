import constants
from constants import State

def win(grid, pos, turn):
	row = pos // 3
	col = pos % 3
	
	# Check horizontal, vertical then diagonals
	if grid[row*3 + col] == grid[row*3 + (col+1)%3] == grid[row*3 + (col+2)%3] == turn:
		return "row"
	elif grid[row*3 + col] == grid[((row+1)%3)*3 + col] == grid[((row+2)%3)*3 + col] == turn:
		return "col"
	elif (pos in constants.RIGHT_DIAG) and (grid[row*3 + col] == grid[((row-1)%3)*3 + (col+1)%3] == grid[((row-2)%3)*3 + (col+2)%3] == turn):
		return "/_diag"
	elif (pos in constants.LEFT_DIAG) and (grid[row*3 + col] == grid[((row+1)%3)*3 + (col+1)%3] == grid[((row+2)%3)*3 + (col+2)%3] == turn):
		return "\\_diag"

	return ""

def draw(grid):
	for i in range(9):
		if grid[i] == State.VALID or grid[i] == State.INVALID:
			return False

	return True