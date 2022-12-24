from enum import Enum

class Colors(Enum):
    WHITE = 1
    BLACK = 2
class MoveTypes(Enum):
    MINOR_CASTLING = 1
    MAJOR_CASTLING = 2
class Status(Enum):
    VALID = 1
    INVALID = 2