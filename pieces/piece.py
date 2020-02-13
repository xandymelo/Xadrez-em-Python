
class Piece():

    primeira_coluna = [x for x in range(1,65) if x % 8 == 1]
    primeira_e_segunda_coluna = [x for x in range(1,65) if x % 8 == 1 or x % 8 == 2]
    penultima_e_ultima_coluna = [x for x in range(1,65) if x % 8 == 7 or x % 8 == 0]
    primeira_e_segunda_linha = [x for x in range(1,17)]
    penultima_e_ultima_linha = [x for x in range(49,65)]
    ultima_coluna = [x for x in range(1,64) if x % 8 == 0]
    primeira_linha = [x for x in range(1,9)]
    segunda_linha = [x for x in range(9,17)]
    penultima_linha = [x for x in range(49,57)]
    ultima_linha = [x for x in range(56,65)]
    gameTiles = []

    def __init__(self,position = None, alliance = None):
        self.position = position
        self.alliance = alliance
        


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
    

    def todos_os_movimentos_possiveis(self,cor_do_jogador):#Note que não adicionei os movimentos dos reis, pois vou usar esta função para verificar xeque, e xeque mate#
        mov_possiveis = []
        if cor_do_jogador == "BLACK":
            #mov_possiveis = torre(self.gameTiles.index("Torre2Pretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + torre(self.gameTiles.index("TorrePretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoPPretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoBPretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("CavaloPretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("Cavalo2Pretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + dama(self.gameTiles.index("DamaPretas"),cor_do_jogador).mov_possiveis(self.gameTiles.index("DamaPretas")) + peao(self.gameTiles.index("peãoPretas1"),cor_do_jogador).mov_possiveis(self.gameTiles.index("peãoPretas1")) + peao(self.gameTiles.index("peãoPretas2"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas3"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas4"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas5"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas6"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas7"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas8"),cor_do_jogador).mov_possiveis(self.gameTiles)
            for c in self.gameTiles:
                if c.pieceOnTile.toString().isupper():
                    if c.pieceOnTile.toString() == "P":
                        if c in self.primeira_coluna:
                            mov_possiveis.append(c.pieceOnTile.position + 9)
                        elif c in self.ultima_coluna:
                            mov_possiveis.append(c.pieceOnTile.position + 7)
                        else:
                            mov_possiveis.append(c.pieceOnTile.position + 7)
                            mov_possiveis.append(c.pieceOnTile.position + 9)
                    else:
                        for d in c.pieceOnTile.possible_mov():
                            if d not in mov_possiveis:
                                mov_possiveis.append(d)
        if cor_do_jogador == "WHITE":
            for c in self.gameTiles:
                if c.pieceOnTile.toString().islower():
                    if c.pieceOnTile.toString() == "p":
                        if c in self.primeira_coluna:
                            mov_possiveis.append(c.pieceOnTile.position - 7)
                        elif c in self.ultima_coluna:
                            mov_possiveis.append(c.pieceOnTile.position - 9)
                        else:
                            mov_possiveis.append(c.pieceOnTile.position - 7)
                            mov_possiveis.append(c.pieceOnTile.position - 9)

                    else:
                        for d in c.pieceOnTile.possible_mov():
                            if d not in mov_possiveis:
                                mov_possiveis.append(d)
            #mov_possiveis = torre(self.gameTiles.index("Torre2Brancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + torre(self.gameTiles.index("TorreBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoPBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoBBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("CavaloBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("Cavalo2Brancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + dama(self.gameTiles.index("DamaBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas1"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas2"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas3"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas4"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas5"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas6"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas7"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas8"),cor_do_jogador).mov_possiveis(self.gameTiles)
        return mov_possiveis
    
