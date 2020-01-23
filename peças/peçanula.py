from peças.peça import Piece

class NullPiece(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, alliance = None, position = None):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "-"