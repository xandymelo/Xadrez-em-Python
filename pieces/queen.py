from pieces.piece import Piece

class Queen(Piece):
    
    alliance = None
    position = None
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "Q" if self.alliance == "Black" else "q"

    def possible_mov(self):
        cor_do_jogador = self.alliance.upper()
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
        cor_do_jogador = cor_do_jogador.upper()
        #Isto é para achar as casa da Diagonal Superior Direita(DSD) das casas do bispo +9#
        mov_possiveisDSD = [x for x in range (self.position, 65, 9)]
        mov_possiveisDSD.remove (self.position)
        while len (mov_possiveisDSD) > 8 - (self.position % 8):
            mov_possiveisDSD.pop ()
        mov_possiveisDSD = self.remover_movimentos_invalidos_diagonal_superior(cor_do_jogador,mov_possiveisDSD)
        
        # Isto é para achar as casa da Diagonal Infeiror Esquerda(DIE) das casas do bispo -9#
        mov_possiveisDIE = [x for x in range (self.position, 0, -9)]
        while len (mov_possiveisDIE) > (self.position // 8) + 1:
            mov_possiveisDIE.pop ()
        mov_possiveisDIE.remove (self.position)
        mov_possiveisDIE = self.remover_movimentos_invalidos_diagonal_inferior(cor_do_jogador,mov_possiveisDIE)

        #DSE#
        mov_possiveisDSE = [x for x in range (self.position, 65, 7)]
        mov_possiveisDSE.remove (self.position)
        while len (mov_possiveisDSE) > (self.position % 8) - 1:
            mov_possiveisDSE.pop ()
        mov_possiveisDSE = self.remover_movimentos_invalidos_diagonal_superior(cor_do_jogador,mov_possiveisDSE)
        mov_possiveisDID = [x for x in range (self.position, 0, -7)]
        while len (mov_possiveisDID) > (self.position // 8) + 1:
            mov_possiveisDID.pop ()
        mov_possiveisDID.remove (self.position)
        mov_possiveisDID = self.remover_movimentos_invalidos_diagonal_inferior(cor_do_jogador,mov_possiveisDID)
        mov_possiveis = mov_possiveis_HD + mov_possiveis_HE + mov_possiveis_VI + mov_possiveis_VS + mov_possiveisDID + mov_possiveisDIE + mov_possiveisDSD + mov_possiveisDSE
        return mov_possiveis