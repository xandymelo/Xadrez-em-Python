from pieces.piece import Piece
from boards.utilMove import util
from util import Colors

class King(Piece):

    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♔" if self.alliance == Colors.BLACK else "♚"
    
    def possible_mov(self):
        ut = util()
        cor_do_jogador = self.alliance
        mov_possiveis = []
        mov_possiveis.append(self.position + 8)
        mov_possiveis.append(self.position - 8)
        mov_possiveis.append(self.position + 7)
        mov_possiveis.append(self.position - 7)
        mov_possiveis.append(self.position + 1)
        mov_possiveis.append(self.position - 1)
        mov_possiveis.append(self.position + 9)
        mov_possiveis.append(self.position - 9)
        if self.position in self.primeira_linha:
            mov_possiveis.remove(self.position - 8)
            mov_possiveis.remove(self.position - 7)
            mov_possiveis.remove(self.position - 9)
        if self.position in self.ultima_linha:
            mov_possiveis.remove(self.position + 7)
            mov_possiveis.remove(self.position + 8)
            mov_possiveis.remove(self.position + 9)
        if self.position in self.primeira_coluna:
            mov_possiveis.remove(self.position - 1)
            if self.position + 7 in mov_possiveis:
                mov_possiveis.remove(self.position + 7)
            if self.position - 9 in mov_possiveis:
                mov_possiveis.remove(self.position - 9)
        if self.position in self.ultima_coluna:
            mov_possiveis.remove(self.position + 1)
            if self.position + 9 in mov_possiveis:
                mov_possiveis.remove(self.position + 9)
            if self.position - 7 in mov_possiveis:
                mov_possiveis.remove(self.position - 7)

        remover = []
        if cor_do_jogador == Colors.WHITE:
            for c in range(len(mov_possiveis)):
                if ut.peca_ameacada(mov_possiveis[c],cor_do_jogador) or self.gameTiles[mov_possiveis[c]].pieceOnTile.toString().islower():
                    remover.append(mov_possiveis[c])
        if cor_do_jogador == Colors.BLACK:
            for c in range(len(mov_possiveis)):
                if ut.peca_ameacada(mov_possiveis[c],cor_do_jogador) or self.gameTiles[mov_possiveis[c]].pieceOnTile.toString().isupper():
                    remover.append(mov_possiveis[c])
        for c in remover:
            mov_possiveis.remove(c)
        return mov_possiveis
        