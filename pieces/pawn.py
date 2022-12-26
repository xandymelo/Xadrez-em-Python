from pieces.piece import Piece
from util import Colors

class Pawn(Piece):
    
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♙" if self.alliance == Colors.BLACK else "♟"

    def possible_mov(self):
        color_of_the_player = self.alliance
        mov_possiveis = []
        if color_of_the_player == Colors.BLACK:
            if self.position not in self.ultima_linha:
                mov_possiveis.append(self.position + 8)
            if self.position in self.segunda_linha:
                mov_possiveis.append(self.position + 16)
            if self.gameTiles[self.position + 7].pieceOnTile.toString().islower() and (self.position not in self.primeira_coluna) and (self.position not in self.ultima_linha):
                if self.position + 7 <= 64:
                    mov_possiveis.append(self.position + 7)
            if self.gameTiles[self.position + 9].pieceOnTile.toString().islower() and (self.position not in self.ultima_coluna) and (self.position not in self.ultima_linha):
                if self.position + 9 <= 64:
                    mov_possiveis.append(self.position + 9)
        if color_of_the_player == Colors.WHITE:
            if self.position not in self.primeira_linha:
                mov_possiveis.append(self.position - 8)
            if self.position in self.penultima_linha:
                mov_possiveis.append(self.position - 16)
            if self.gameTiles[self.position - 7].pieceOnTile.toString().isupper() and (self.position not in self.primeira_coluna) and (self.position not in self.ultima_linha):
                if self.position + 7 <= 64:
                    mov_possiveis.append(self.position - 7)
            if self.gameTiles[self.position - 9].pieceOnTile.toString().isupper() and (self.position not in self.ultima_coluna) and (self.position not in self.ultima_linha):
                if self.position + 9 <= 64:
                    mov_possiveis.append(self.position - 9)
        return mov_possiveis
