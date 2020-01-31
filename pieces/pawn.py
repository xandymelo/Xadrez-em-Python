from pieces.piece import Piece

class Pawn(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "P" if self.alliance == "Black" else "p"