from pieces.piece import Piece


class King(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "K" if self.alliance == "Black" else "k"
    
    def mov_possiveis(self):
        cor_do_jogador = ""
        if "Pretas" in self.gameTiles[self.position]:
            cor_do_jogador == "PRETAS"
        elif "Brancas" in self.gameTiles[self.position]:
            cor_do_jogador == "BRANCAS"
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
        elif self.position in self.ultima_linha:
            mov_possiveis.remove(self.position + 7)
            mov_possiveis.remove(self.position + 8)
            mov_possiveis.remove(self.position + 9)
        elif self.position in self.primeira_coluna:
            mov_possiveis.remove(self.position - 1)
        if self.position + 7 in mov_possiveis:
            mov_possiveis.remove(self.position + 7)
        if self.position - 9 in mov_possiveis:
            mov_possiveis.remove(self.position - 9)
        elif self.position in self.ultima_coluna:
            if self.position + 9 in mov_possiveis:
                mov_possiveis.remove(self.position + 9)
            mov_possiveis.remove(self.position + 1)
        if self.position - 7 in mov_possiveis:
            mov_possiveis.remove(self.position - 7)

        if (cor_do_jogador == "PRETAS") or (cor_do_jogador == "NEGRAS"):
            for c in mov_possiveis:
                if c in self.todos_os_movimentos_possiveis("Brancas"):
                    mov_possiveis.remove(c)
                if "Pretas" in self.gameTiles[c]:
                    mov_possiveis.remove(c)
        if cor_do_jogador == "BRANCAS":
            for c in mov_possiveis:
                if c in self.todos_os_movimentos_possiveis("Pretas"):
                    mov_possiveis.remove(c)
                if "Brancas" in self.gameTiles[c]:
                    mov_possiveis.remove(c)
        return mov_possiveis
        