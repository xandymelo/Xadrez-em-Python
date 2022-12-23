from pieces.piece import Piece

class Bishop(Piece):
    
    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♗" if self.alliance == "Black" else "♝"
    
    def possible_mov(self):#COMO FAZER NÃO REBATER A DIAGONAL NO MOVIMENTO? RESTO DA DIVISÃO DA POSIÇÃO POR 8, SUBTRAI O RESTO POR 8, É O NUMERO DE POSIÇÕES NAQUELA DIREÇÃO DA DIAGONAL#
        #Isto é para achar as casa da Diagonal Superior Direita(DSD) das casas do bispo +9#
        mov_possiveisDSD = [x for x in range (self.position, 65, 9)]
        mov_possiveisDSD.remove(self.position)
        while len (mov_possiveisDSD) > 8 - (self.position % 8):
            mov_possiveisDSD.pop ()
        mov_possiveisDSD = self.remover_movimentos_invalidos_diagonal_superior(mov_possiveisDSD)
        
        # Isto é para achar as casa da Diagonal Infeiror Esquerda(DIE) das casas do bispo -9#
        mov_possiveisDIE = [x for x in range (self.position, 0, -9)]
        while len (mov_possiveisDIE) > (self.position // 8) + 1:
            mov_possiveisDIE.pop ()
        mov_possiveisDIE.remove(self.position)
        mov_possiveisDIE = self.remover_movimentos_invalidos_diagonal_inferior(mov_possiveisDIE)

        #DSE#
        mov_possiveisDSE = [x for x in range (self.position, 65, 7)]
        while len (mov_possiveisDSE) > (self.position % 8) - 1:
            mov_possiveisDSE.pop ()
        mov_possiveisDSE = self.remover_movimentos_invalidos_diagonal_superior(mov_possiveisDSE)
        #DID(Se basear no caso de DIE)MUITO MASSA, CONSEGUIMOS RESOLVER O B.O APENAS PENSANDO#
        mov_possiveisDID = [x for x in range (self.position, 0, -7)]
        while len (mov_possiveisDIE) > (self.position // 8) + 1:
            mov_possiveisDIE.pop ()
        mov_possiveisDID.remove(self.position)
        mov_possiveisDID = self.remover_movimentos_invalidos_diagonal_inferior(mov_possiveisDID)
        mov_possiveis = mov_possiveisDSD + mov_possiveisDID + mov_possiveisDSE + mov_possiveisDIE
        return mov_possiveis