from pieces.piece import Piece

class Knight(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "N" if self.alliance == "Black" else "n"