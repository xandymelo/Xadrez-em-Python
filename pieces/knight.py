from pieces.piece import Piece

class Knight(Piece):
    

    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♘" if self.alliance == "Black" else "♞"

    def possible_mov(self):#Se o cavalo tiver na (primeira coluna + segunda coluna) ele perde os dois movimentos para esquerda, segue a mesma lógica para as 2 ultimas colunas, 2 primeiras linhas e 2 últimas linhas#
        cor_do_jogador = self.alliance.upper()
        mov_possiveis = []
        mov_possiveis.append(self.position + 10)
        mov_possiveis.append(self.position + 6)
        mov_possiveis.append(self.position - 6)
        mov_possiveis.append(self.position - 10)
        mov_possiveis.append(self.position + 15)
        mov_possiveis.append(self.position - 15)
        mov_possiveis.append(self.position + 17)
        mov_possiveis.append(self.position - 17)
        if self.position in self.primeira_e_segunda_linha:
            mov_possiveis.remove(self.position - 17)
            mov_possiveis.remove(self.position - 15)
        if self.position in self.penultima_e_ultima_linha:
            mov_possiveis.remove(self.position + 15)
            mov_possiveis.remove(self.position + 17)
        if self.position in self.primeira_e_segunda_coluna:
            mov_possiveis.remove(self.position - 10)
            mov_possiveis.remove(self.position + 6)
        if self.position in self.penultima_e_ultima_coluna:
            mov_possiveis.remove(self.position + 10)
            mov_possiveis.remove(self.position - 6)
        for c in mov_possiveis:
            if c > 64 or c < 1:
                mov_possiveis.remove(c)
        if (cor_do_jogador == "BLACK"):
            for c in mov_possiveis:
                if self.gameTiles[c].pieceOnTile.toString().isupper():
                    mov_possiveis.remove(c)
        if cor_do_jogador == "WHITE":
            for c in mov_possiveis:
                if self.gameTiles[c].pieceOnTile.toString().islower():
                    mov_possiveis.remove(c)
        return mov_possiveis