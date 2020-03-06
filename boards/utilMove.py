from pieces.piece import Piece
from boards.tile import Tile
from pieces.nullpiece import NullPiece
import copy

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
        casa_do_rei = ""
        if cor_do_jogador == "BLACK":
            casa_do_rei = self.conseguir_casa_do_rei(cor_do_jogador)
            movimentos_possiveis = self.todos_os_movimentos_possiveis("WHITE")
            if casa_do_rei in movimentos_possiveis:
                return True
            else:
                return False
        if cor_do_jogador == "WHITE":
            casa_do_rei = self.conseguir_casa_do_rei(cor_do_jogador)
            movimentos_possiveis = self.todos_os_movimentos_possiveis("BLACK")
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

    def peca_ameacada(self,local_atual,cor_do_jogador):
        cor_do_jogador_adversario = ""
        cor_do_jogador = cor_do_jogador.upper()
        if cor_do_jogador == "BLACK":
            cor_do_jogador_adversario = "WHITE"
        elif cor_do_jogador == "WHITE":
            cor_do_jogador_adversario = "BLACK"
        if local_atual in self.todos_os_movimentos_possiveis(cor_do_jogador_adversario):
            return True
        else:
            return False

    def peca_cravada(self,cor_do_jogador):
        if self.peca_ameacada(self.position,cor_do_jogador):
            x = copy.deepcopy(self.gameTiles[self.position])
            self.gameTiles[self.position] = Tile(self.position, NullPiece())  #usar deepcopy
            if self.xeque(self.alliance):
                self.gameTiles[self.position] = x
                return True
            else:
                self.gameTiles[self.position] = x
                return False   
        else:
            return False
    def xeque_mate(self,cor_do_jogador):
        cor_do_jogador = cor_do_jogador.upper()
        if self.xeque(cor_do_jogador):
            return self.testar_se_o_rei_tem_movimentos(cor_do_jogador)
        return False
                
    def conseguir_casa_do_rei(self,cor_do_jogador):
        cor_do_jogador = cor_do_jogador.upper()
        if cor_do_jogador == "BLACK":
            for c in self.gameTiles:
                if c.pieceOnTile.toString() == "K":
                    casa_do_rei = c.pieceOnTile.position
        if cor_do_jogador == "WHITE":
            for c in self.gameTiles:
                if c.pieceOnTile.toString() == "k":
                    casa_do_rei = c.pieceOnTile.position
        return casa_do_rei
    def testar_se_o_mov_eh_possivel(self,cor_do_jogador,local_atual_convertido,novo_local_convertido):
        ut = util()
        x = copy.deepcopy(self.gameTiles[novo_local_convertido])
        self.gameTiles[novo_local_convertido] = self.gameTiles[local_atual_convertido]
        self.gameTiles[novo_local_convertido].tileCoordinate = novo_local_convertido
        self.gameTiles[novo_local_convertido].pieceOnTile.position = novo_local_convertido
        self.gameTiles[local_atual_convertido] = Tile(local_atual_convertido,NullPiece())
        if ut.xeque(cor_do_jogador):
            self.gameTiles[local_atual_convertido] = self.gameTiles[novo_local_convertido]
            self.gameTiles[local_atual_convertido].tileCoordinate = local_atual_convertido
            self.gameTiles[local_atual_convertido].pieceOnTile.position = local_atual_convertido
            self.gameTiles[novo_local_convertido] = x
            return True
        self.gameTiles[local_atual_convertido] = self.gameTiles[novo_local_convertido]
        self.gameTiles[local_atual_convertido].tileCoordinate = local_atual_convertido
        self.gameTiles[local_atual_convertido].pieceOnTile.position = local_atual_convertido
        self.gameTiles[novo_local_convertido] = x
        return False
    
    
    def afogamento(self,cor_do_jogador):
        cor_do_jogador = cor_do_jogador.upper()
        if not self.xeque(cor_do_jogador):
            return self.testar_se_o_rei_tem_movimentos(cor_do_jogador)
        return False
    

    def testar_se_o_rei_tem_movimentos(self,cor_do_jogador):
        casa_do_rei = self.conseguir_casa_do_rei(cor_do_jogador)
        if self.gameTiles[casa_do_rei].pieceOnTile.possible_mov() == []:
            return True
        soma = 0 
        for c in self.gameTiles[casa_do_rei].pieceOnTile.possible_mov():
            x = self.testar_se_o_mov_eh_possivel(cor_do_jogador,casa_do_rei,c)
            if x:
                soma += 1
        if soma == len(self.gameTiles[casa_do_rei].pieceOnTile.possible_mov()):
            return True
        return False