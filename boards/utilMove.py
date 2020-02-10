from boards.ChessBoard import Board
from pieces.piece import Piece
from boards.tile import Tile
from pieces.nullpiece import NullPiece

class util(Piece):
    def __init__(self):
        pass

    def converter_inputs(self,input):
        novo_local_provisorio = input[0] + input[1]
        novo_local = 0
        if novo_local_provisorio[0] == "a":
            novo_local += 1
        elif novo_local_provisorio[0] == "b":
            novo_local += 2
        elif novo_local_provisorio[0] == "c":
            novo_local += 3
        elif novo_local_provisorio[0] == "d":
            novo_local += 4
        elif novo_local_provisorio[0] == "e":
            novo_local += 5
        elif novo_local_provisorio[0] == "f":
            novo_local += 6
        elif novo_local_provisorio[0] == "g":
            novo_local += 7
        elif novo_local_provisorio[0] == "h":
            novo_local += 8
        novo_local += (8 - int(novo_local_provisorio[1])) * 8
        return novo_local
    

    
    def xeque(self,cor_do_jogador):#Aqui irei verificar se a casa do rei está na lista de movimentos possiveis (lembrando que a função de todos os movimentos possiveis não inclui os movimentos do rei  #
        cor_do_jogador = cor_do_jogador.upper()
        if cor_do_jogador == "PRETAS" or cor_do_jogador == "NEGRAS":
            casa_do_rei = self.gameTiles.index("K")
            movimentos_possiveis = self.todos_os_movimentos_possiveis("Brancas")
            if casa_do_rei in movimentos_possiveis:
                return True
            else:
                return False
        if cor_do_jogador == "BRANCAS":
            casa_do_rei = self.gameTiles.index("k")
            movimentos_possiveis = self.todos_os_movimentos_possiveis("Pretas")
            if casa_do_rei in movimentos_possiveis:
                return True
            else:
                return False

    def verificar_se_mov_eh_valido(self,local_atual_convertido,novo_local_convertido):
        mov_possiveis_da_peca = self.gameTiles[local_atual_convertido].pieceOnTile.possible_mov()
        if (not (novo_local_convertido in mov_possiveis_da_peca)):
            return False
        else:
            return True

    def peca_ameacada(self,local_atual):
        cor_do_jogador_adversario = ""
        if self.gameTiles[local_atual].count("Pretas") == 1:
            cor_do_jogador_adversario = "Brancas"
        else:
            cor_do_jogador_adversario = "Pretas"
        if local_atual in self.todos_os_movimentos_possiveis(cor_do_jogador_adversario):
            return 1
        else:
            return 0
        mov_possiveis = self.todos_os_movimentos_possiveis("Brancas") + self.todos_os_movimentos_possiveis("Pretas")
        if self.gameTiles[local_atual] == "" and (local_atual in mov_possiveis):
            return 1
        else:
            return 0
    
    def peca_cravada(self):
        if self.peca_ameacada(self.position):
            self.gameTiles[self.position] = Tile(self.position, NullPiece())  #usar deepcopy
            if self.xeque(self.alliance):
                pass
                
            
        else:
            return False
