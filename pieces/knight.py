from pieces.piece import Piece
from util import Colors

class Knight(Piece):
    

    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♘" if self.alliance == Colors.BLACK else "♞"

    def possible_mov(self):#Se o cavalo tiver na (primeira coluna + segunda coluna) ele perde os dois movimentos para esquerda, segue a mesma lógica para as 2 ultimas colunas, 2 primeiras linhas e 2 últimas linhas#
        color_of_the_player = self.alliance
        possible_moves = []
        possible_moves.append(self.position + 10)
        possible_moves.append(self.position + 6)
        possible_moves.append(self.position - 6)
        possible_moves.append(self.position - 10)
        possible_moves.append(self.position + 15)
        possible_moves.append(self.position - 15)
        possible_moves.append(self.position + 17)
        possible_moves.append(self.position - 17)
        if self.position in self.primeira_e_segunda_linha:
            possible_moves.remove(self.position - 17)
            possible_moves.remove(self.position - 15)
        if self.position in self.penultima_e_ultima_linha:
            possible_moves.remove(self.position + 15)
            possible_moves.remove(self.position + 17)
        if self.position in self.primeira_e_segunda_coluna:
            possible_moves.remove(self.position - 10)
            possible_moves.remove(self.position + 6)
        if self.position in self.penultima_e_ultima_coluna:
            possible_moves.remove(self.position + 10)
            possible_moves.remove(self.position - 6)
        for c in possible_moves:
            if c > 64 or c < 1:
                possible_moves.remove(c)
        if (color_of_the_player == Colors.BLACK):
            for c in possible_moves:
                if self.gameTiles[c].pieceOnTile.toString().isupper():
                    possible_moves.remove(c)
        if color_of_the_player == Colors.WHITE:
            for c in possible_moves:
                if self.gameTiles[c].pieceOnTile.toString().islower():
                    possible_moves.remove(c)
        return possible_moves