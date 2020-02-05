from pieces.piece import Piece

class Rook(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "R" if self.alliance == "Black" else "r"

    def mov_possiveis(self):
        cor_do_jogador = self.alliance.upper()
        #if "Pretas" in self.gameTiles[self.position]:
            #cor_do_jogador = "PRETAS"
        #elif "Brancas" in self.gameTiles[self.position]:
            #cor_do_jogador = "BRANCAS"
        #HD = horizontal direita#
        mov_possiveis_HD = [x for x in range (self.position + 1, 65)]
        while len (mov_possiveis_HD) > 8 - (self.position % 8):
            mov_possiveis_HD.pop ()
        mov_possiveis_HD = self.remover_movimentos_invalidos_diagonal_superior(cor_do_jogador,mov_possiveis_HD)
        #HE = horizontal esquerda#
        mov_possiveis_HE = [x for x in range (self.position, 0, -1)]
        while len (mov_possiveis_HE) > ((self.position) % 8):
            mov_possiveis_HE.pop ()
        mov_possiveis_HE.remove (self.position)
        mov_possiveis_HE = self.remover_movimentos_invalidos_diagonal_inferior(cor_do_jogador,mov_possiveis_HE)
        #VS = Vertical Superior#
        mov_possiveis_VS = [x for x in range(self.position,65,8)]
        mov_possiveis_VS.remove (self.position)
        mov_possiveis_VS = self.remover_movimentos_invalidos_diagonal_superior(cor_do_jogador,mov_possiveis_VS)
        #VI = Vertical Inferior#
        mov_possiveis_VI = [x for x in range(self.position,0,-8)]
        mov_possiveis_VI.remove (self.position)
        mov_possiveis_VI = self.remover_movimentos_invalidos_diagonal_inferior(cor_do_jogador,mov_possiveis_VI)
        mov_possiveis = mov_possiveis_HD + mov_possiveis_HE + mov_possiveis_VI + mov_possiveis_VS
        return mov_possiveis