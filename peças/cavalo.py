from peças.peça import Piece

class knight(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "N" if self.alliance == "Black" else "n"