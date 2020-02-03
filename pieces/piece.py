


class Piece():

    gameTiles = []


    def __init__(self):
        pass


    def remover_movimentos_invalidos_diagonal_superior(self,cor_do_jogador,mov_possiveisDSD):
        if cor_do_jogador == "PRETAS" or cor_do_jogador == "NEGRAS":
            for c in mov_possiveisDSD:
                if "Pretas" in self.gameTiles[c]:
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x < c]
                    break
                elif "Brancas" in self.gameTiles[c]:
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x <= c]
                    break
                
        if cor_do_jogador == "BRANCAS":
            for c in mov_possiveisDSD:
                if "Brancas" in self.gameTiles[c]:
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x < c]
                    break
                elif "Pretas" in self.gameTiles[c]:
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x <= c]
                    break
        return mov_possiveisDSD
    
    def remover_movimentos_invalidos_diagonal_inferior(self,cor_do_jogador,mov_possiveisDIE):
        if cor_do_jogador == "PRETAS" or cor_do_jogador == "NEGRAS":
            for c in mov_possiveisDIE:
                if "Pretas" in self.gameTiles[c]:
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x > c]
                    break
                elif "Brancas" in self.gameTiles[c]:
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x >= c]
                    break
                
        if cor_do_jogador == "BRANCAS":
            for c in mov_possiveisDIE:
                if "Brancas" in self.gameTiles[c]:
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x > c]
                    break
                elif "Pretas" in self.gameTiles[c]:
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x >= c]
                    break
        return mov_possiveisDIE
    