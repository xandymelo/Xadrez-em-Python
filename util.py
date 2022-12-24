from enum import Enum

class Colors(Enum):
    WHITE = 1
    BLACK = 2
class MoveTypes(Enum):
    MINOR_CASTLING = 1
    MAJOR_CASTLING = 2
class MoveStatus(Enum):
    VALID_MOVE = 1
    INVALID_MOVE = 2