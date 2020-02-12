from pieces.piece import Piece


class King(Piece):

    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "K" if self.alliance == "Black" else "k"
    
    def possible_mov(self):
        cor_do_jogador = self.alliance.upper()
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

        if (cor_do_jogador == "BLACK"):
            for c in mov_possiveis:
                if (c in self.todos_os_movimentos_possiveis("White")) or (self.gameTiles[c].pieceOnTile.toString().isupper()):
                    mov_possiveis.remove(c)
        if cor_do_jogador == "WHITE":
            for c in mov_possiveis:
                if (c in self.todos_os_movimentos_possiveis("Black")) or (self.gameTiles[c].pieceOnTile.toString().islower()):
                    mov_possiveis.remove(c)
        return mov_possiveis
        