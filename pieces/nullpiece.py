
class NullPiece():
    
    alliance = None
    position = None
    
    def __init__(self, position = None, alliance = None):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "-"
    def possible_mov(self):
        return []