from enum import Enum

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
X_COL = (88, 169, 245)
O_COL = (245, 88, 88)
OFFSET = 10
RIGHT_DIAG = (2, 4, 6)
LEFT_DIAG = (0, 4, 8)

class State(Enum):
	X = 1
	O = -1
	VALID = 0
	INVALID = 2
	DRAW = 3