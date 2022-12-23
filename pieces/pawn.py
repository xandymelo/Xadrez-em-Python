from pieces.piece import Piece

class Pawn(Piece):
    
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♙" if self.alliance == "Black" else "♟"

    def possible_mov(self):
        cor_do_jogador = self.alliance.upper()
        #if "Pretas" in self.gameTiles[self.position]:
            #cor_do_jogador == "PRETAS"
        #elif "WHITE" in self.gameTiles[self.position]:
            #cor_do_jogador == "WHITE"
        mov_possiveis = []
        if cor_do_jogador == "BLACK":
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
        if cor_do_jogador == "WHITE":
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
