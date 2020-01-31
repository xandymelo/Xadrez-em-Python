from pieces.piece import Piece

class Queen(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "Q" if self.alliance == "Black" else "q"