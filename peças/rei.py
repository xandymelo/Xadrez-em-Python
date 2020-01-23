from peças.peça import Piece

class king(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "K" if self.alliance == "Black" else "k"
    