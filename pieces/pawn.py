from pieces.piece import Piece

class Pawn(Piece):
    
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "P" if self.alliance == "Black" else "p"

    def mov_possiveis(self):
        cor_do_jogador = self.alliance.upper()
        #if "Pretas" in self.gameTiles[self.position]:
            #cor_do_jogador == "PRETAS"
        #elif "Brancas" in self.gameTiles[self.position]:
            #cor_do_jogador == "BRANCAS"
        mov_possiveis = []
        if self.position not in self.ultima_linha:
            mov_possiveis.append(self.position + 8)
        if cor_do_jogador == "PRETAS" or cor_do_jogador == "NEGRAS":
            if "Brancas" in self.gameTiles[self.position + 7] and (self.position not in self.primeira_coluna) and (self.position not in self.ultima_linha):
                if self.position + 7 <= 64:
                    mov_possiveis.append(self.position + 7)
            if "Brancas" in self.gameTiles[self.position + 9] and (self.position not in self.ultima_coluna) and (self.position not in self.ultima_linha):
                if self.position + 9 <= 64:
                    mov_possiveis.append(self.position + 9)
        if cor_do_jogador == "BRANCAS":
            if "Pretas" in self.gameTiles[self.position + 7] and (self.position not in self.primeira_coluna) and (self.position not in self.ultima_linha):
                if self.position + 7 <= 64:
                    mov_possiveis.append(self.position + 7)
            if "Pretas" in self.gameTiles[self.position + 9] and (self.position not in self.ultima_coluna) and (self.position not in self.ultima_linha):
                if self.position + 9 <= 64:
                    mov_possiveis.append(self.position + 9)
        return mov_possiveis