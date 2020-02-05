from pieces.piece import Piece

class Knight(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "N" if self.alliance == "Black" else "n"

    def possible_mov(self):#Se o cavalo tiver na (primeira coluna + segunda coluna) ele perde os dois movimentos para esquerda, segue a mesma lógica para as 2 ultimas colunas, 2 primeiras linhas e 2 últimas linhas#
        cor_do_jogador = self.alliance.upper()
        #if "Pretas" in self.gameTiles[self.position]:
            #cor_do_jogador == "PRETAS"
        #elif "Brancas" in self.gameTiles[self.position]:
            #cor_do_jogador == "BRANCAS"
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
        elif self.position in self.penultima_e_ultima_linha:
            mov_possiveis.remove(self.position + 15)
            mov_possiveis.remove(self.position + 17)
        elif self.position in self.primeira_e_segunda_coluna:
            mov_possiveis.remove(self.position - 10)
            mov_possiveis.remove(self.position + 6)
        elif self.position in self.penultima_e_ultima_coluna:
            mov_possiveis.remove(self.position + 10)
            mov_possiveis.remove(self.position - 6)
        if (cor_do_jogador == "PRETAS") or (cor_do_jogador == "NEGRAS"):
            for c in mov_possiveis:
                if "Pretas" in c:
                    mov_possiveis.remove(c)
        if cor_do_jogador == "BRANCAS":
            for c in mov_possiveis:
                if "Brancas" in c:
                    mov_possiveis.remove(c)
        return mov_possiveis