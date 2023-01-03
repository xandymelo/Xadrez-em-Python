from util import Colors

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
        


    def remover_movimentos_invalidos_diagonal_superior(self,mov_possiveisDSD):
        if self.alliance == "Black":
            for c in mov_possiveisDSD:
                if self.gameTiles[c].pieceOnTile.toString().isupper():
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x < c]
                    break
                elif self.gameTiles[c].pieceOnTile.toString().islower():
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x <= c]
                    break
                
        if self.alliance == "White":
            for c in mov_possiveisDSD:
                if self.gameTiles[c].pieceOnTile.toString().islower():
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x < c]
                    break
                elif self.gameTiles[c].pieceOnTile.toString().isupper():
                    mov_possiveisDSD = [x for x in mov_possiveisDSD if x <= c]
                    break
        return mov_possiveisDSD
    
    def remover_movimentos_invalidos_diagonal_inferior(self,mov_possiveisDIE):
        if self.alliance == "Black":
            for c in mov_possiveisDIE:
                if self.gameTiles[c].pieceOnTile.toString().isupper():
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x > c]
                    break
                elif self.gameTiles[c].pieceOnTile.toString().islower():
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x >= c]
                    break
                
        if self.alliance == "White":
            for c in mov_possiveisDIE:
                if self.gameTiles[c].pieceOnTile.toString().islower():
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x > c]
                    break
                elif self.gameTiles[c].pieceOnTile.toString().isupper():
                    mov_possiveisDIE = [x for x in mov_possiveisDIE if x >= c]
                    break
        return mov_possiveisDIE
    

    def all_possible_moves(self,color_of_the_player):#Note que não adicionei os movimentos dos reis, pois vou usar esta função para verificar xeque, e xeque mate#
        mov_possiveis = []
        if color_of_the_player == Colors.BLACK:
            #mov_possiveis = torre(self.gameTiles.index("Torre2Pretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + torre(self.gameTiles.index("TorrePretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoPPretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoBPretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("CavaloPretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("Cavalo2Pretas"),cor_do_jogador).mov_possiveis(self.gameTiles) + dama(self.gameTiles.index("DamaPretas"),cor_do_jogador).mov_possiveis(self.gameTiles.index("DamaPretas")) + peao(self.gameTiles.index("peãoPretas1"),cor_do_jogador).mov_possiveis(self.gameTiles.index("peãoPretas1")) + peao(self.gameTiles.index("peãoPretas2"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas3"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas4"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas5"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas6"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas7"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoPretas8"),cor_do_jogador).mov_possiveis(self.gameTiles)
            for c in self.gameTiles:
                if c.pieceOnTile.alliance == Colors.WHITE:
                    if c.pieceOnTile.toString() == "♙":
                        if c.pieceOnTile.position in self.primeira_coluna:
                            mov_possiveis.append(c.pieceOnTile.position + 9)
                        elif c.pieceOnTile.position in self.ultima_coluna:
                            mov_possiveis.append(c.pieceOnTile.position + 7)
                        else:
                            mov_possiveis.append(c.pieceOnTile.position + 7)
                            mov_possiveis.append(c.pieceOnTile.position + 9)
                    elif c.pieceOnTile.toString() == "♔":
                        mov_possiveis.append(c.pieceOnTile.position + 8)
                        mov_possiveis.append(c.pieceOnTile.position - 8)
                        mov_possiveis.append(c.pieceOnTile.position + 7)
                        mov_possiveis.append(c.pieceOnTile.position - 7)
                        mov_possiveis.append(c.pieceOnTile.position + 1)
                        mov_possiveis.append(c.pieceOnTile.position - 1)
                        mov_possiveis.append(c.pieceOnTile.position + 9)
                        mov_possiveis.append(c.pieceOnTile.position - 9)
                    else:
                        if (len(c.pieceOnTile.possible_mov()) != 0):
                            mov_possiveis = list(set(mov_possiveis)) + list(set(c.pieceOnTile.possible_mov()))
                        # for d in c.pieceOnTile.possible_mov():
                        #     mov_possiveis.append(d)
                else:
                    pass
        if color_of_the_player == Colors.WHITE:
            for c in self.gameTiles:
                if c.pieceOnTile.alliance == Colors.BLACK:
                    if c.pieceOnTile.toString() == "♟":
                        if c.pieceOnTile.position in self.primeira_coluna:
                            mov_possiveis.append(c.pieceOnTile.position - 7)
                        elif c.pieceOnTile.position in self.ultima_coluna:
                            mov_possiveis.append(c.pieceOnTile.position - 9)
                        else:
                            mov_possiveis.append(c.pieceOnTile.position - 7)
                            mov_possiveis.append(c.pieceOnTile.position - 9)
                    
                    elif c.pieceOnTile.toString() == "♚":
                        mov_possiveis.append(c.pieceOnTile.position + 8)
                        mov_possiveis.append(c.pieceOnTile.position - 8)
                        mov_possiveis.append(c.pieceOnTile.position + 7)
                        mov_possiveis.append(c.pieceOnTile.position - 7)
                        mov_possiveis.append(c.pieceOnTile.position + 1)
                        mov_possiveis.append(c.pieceOnTile.position - 1)
                        mov_possiveis.append(c.pieceOnTile.position + 9)
                        mov_possiveis.append(c.pieceOnTile.position - 9)

                    else:
                        for d in c.pieceOnTile.possible_mov():
                            mov_possiveis.append(d)
            
        # mov_possiveis = set(mov_possiveis)
        # mov_possiveis = list(mov_possiveis)
        remover = []
        for c in mov_possiveis:
            if c > 64 or c < 1:
                remover.append(c)
        for c in remover:
            mov_possiveis.remove(c)
        #mov_possiveis = torre(self.gameTiles.index("Torre2Brancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + torre(self.gameTiles.index("TorreBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoPBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + bispo.bispo(self.gameTiles.index("BispoBBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("CavaloBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + cavalo(self.gameTiles.index("Cavalo2Brancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + dama(self.gameTiles.index("DamaBrancas"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas1"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas2"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas3"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas4"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas5"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas6"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas7"),cor_do_jogador).mov_possiveis(self.gameTiles) + peao(self.gameTiles.index("peãoBrancas8"),cor_do_jogador).mov_possiveis(self.gameTiles)
        return mov_possiveis
    
