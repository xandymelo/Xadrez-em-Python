from boards.ChessBoard import Board
from pieces.nullpiece import NullPiece
from boards.utilMove import util
from boards.tile import Tile
from pieces.piece import Piece
from pieces.king import King
from pieces.rook import Rook
import copy





class Move(Piece):
    def __init__(self,contagem_movimento_rei_pretas = 0,contagem_movimento_rei_brancas = 0,contagem_movimento_torre_rm_pretas = 0,contagem_movimento_torre_rm_brancas = 0,contagem_movimento_torre_rma_brancas = 0,contagem_movimento_torre_rma_pretas = 0):
        self.contagem_movimento_rei_pretas = contagem_movimento_rei_pretas
        self.contagem_movimento_rei_brancas = contagem_movimento_rei_brancas
        self.contagem_movimento_torre_rm_pretas = contagem_movimento_torre_rm_pretas
        self.contagem_movimento_torre_rm_brancas = contagem_movimento_torre_rm_brancas
        self.contagem_movimento_torre_rma_brancas = contagem_movimento_torre_rma_brancas
        self.contagem_movimento_torre_rma_pretas = contagem_movimento_torre_rma_pretas
        self.contagem_de_movimento_sem_tomar_peca = 0
    
    
    
    
    
    #AJEITAR ESSA FUNÇÃO E COLOCAR OUTRAS#
    def movimentar_peca(self,cor_do_jogador,input): #mudar o formato do input para o formatov'd2d4'#
        ut = util()
        cor_do_jogador = cor_do_jogador.upper()
        cor_do_jogador_adversario = ''
        if input == 'castle': 
            x = self.roque_menor(cor_do_jogador)
            if x:
                print("Não é possível fazer o roque")
            else:
                print("Roque feito com sucesso")
            return x
        elif input == 'bcastle':
            x = self.roque_maior(cor_do_jogador)
            if x:
                print("Não é possível fazer o roque")
            else:
                print("Roque feito com sucesso")
            return x
        cor_do_jogador_adversario = ut.achar_a_cor_do_adversario(cor_do_jogador)
        if not (input[0].isalpha() and input[1].isdigit() and input[2].isalpha() and input[3].isdigit()):
            print("Movimento Inválido")
            return True
        

        local_atual = input[0] + input[1]
        novo_local = input[2] + input[3]
        local_atual_convertido = ut.converter_inputs(local_atual)
        novo_local_convertido = ut.converter_inputs(novo_local)
        #criar a parte que verifica se a jogada é válida#
        verificacao = ut.verificar_se_mov_eh_valido(local_atual_convertido,novo_local_convertido)
        if not verificacao:
            print('Movimento Inválido')
            return True


        nome_da_peca = self.gameTiles[local_atual_convertido].pieceOnTile.toString()
        if nome_da_peca == "K":
            self.contagem_movimento_rei_pretas += 1
        if nome_da_peca == "k":
            self.contagem_movimento_rei_brancas += 1
        if nome_da_peca == "R":
            if local_atual_convertido == 64:
                self.contagem_movimento_torre_rm_pretas += 1
            if local_atual_convertido == 57:
                self.contagem_movimento_torre_rma_pretas += 1
        if nome_da_peca == "r":
            if local_atual_convertido == 8:
                self.contagem_movimento_torre_rm_brancas += 1
            if local_atual_convertido == 1:
                self.contagem_movimento_torre_rma_brancas += 1
        #if cor_do_jogador in nome_da_peca:
        #if (self.gameTiles[novo_local_convertido] is NullPiece):
        x = ut.testar_se_o_mov_eh_possivel(cor_do_jogador,local_atual_convertido,novo_local_convertido)
        if x:
            return True
        if self.gameTiles[novo_local_convertido].pieceOnTile.toString() == '-':
            self.contagem_de_movimento_sem_tomar_peca += 1
        else:
            self.contagem_de_movimento_sem_tomar_peca = 0
        
        
        self.gameTiles[novo_local_convertido] = self.gameTiles[local_atual_convertido]
        self.gameTiles[novo_local_convertido].tileCoordinate = novo_local_convertido
        self.gameTiles[novo_local_convertido].pieceOnTile.position = novo_local_convertido
        self.gameTiles[local_atual_convertido] = Tile(local_atual_convertido,NullPiece())
        print("Jogada feita com sucesso")
        if ut.xeque(cor_do_jogador_adversario):
            print('xeque!')
        return False

        #else:
            #print("Escolha uma jogada com a cor correta (" + cor_do_jogador + ")")
            #return True
    

    
    
    
    
    
    
    
    
    def roque_menor(self,cor_do_jogador):
        ut = util()
        cor_do_jogador = cor_do_jogador.upper()
        if cor_do_jogador == "WHITE":
            if (self.contagem_movimento_rei_brancas > 0) or (self.contagem_movimento_torre_rm_brancas > 0) or (ut.peca_ameacada(62,cor_do_jogador)) or (ut.peca_ameacada(63,cor_do_jogador)) or (type(self.gameTiles[62].pieceOnTile) is not NullPiece ) or (type(self.gameTiles[63].pieceOnTile) is not NullPiece) or (ut.xeque(cor_do_jogador)):
                return True
            else:
                self.gameTiles[63] = Tile(63, King(63, "White"))
                self.gameTiles[62] = Tile(62, Rook(62, "White"))
                self.gameTiles[61] = Tile(61, NullPiece())
                self.gameTiles[64] = Tile(64, NullPiece())
                return False
        if cor_do_jogador == 'BLACK':
            if (self.contagem_movimento_rei_pretas > 0) or (self.contagem_movimento_torre_rm_pretas > 0) or (ut.peca_ameacada(6,cor_do_jogador)) or (ut.peca_ameacada(7,cor_do_jogador)) or (type(self.gameTiles[6].pieceOnTile) is not NullPiece) or (type(self.gameTiles[7].pieceOnTile) is not NullPiece) or (ut.xeque(cor_do_jogador)):
                return True
            else:
                self.gameTiles[6] = Tile(6,Rook(6,"Black"))
                self.gameTiles[7] = Tile(7, King(7, "Black"))
                self.gameTiles[5] = Tile(5, NullPiece())
                self.gameTiles[8] = Tile(8, NullPiece())
                return False


    def roque_maior(self,cor_do_jogador):
        ut = util()
        cor_do_jogador = cor_do_jogador.upper()
        if cor_do_jogador == "WHITE":
            if (self.contagem_movimento_rei_brancas > 0) or (self.contagem_movimento_torre_rma_brancas > 0) or (ut.peca_ameacada(60,cor_do_jogador)) or (ut.peca_ameacada(59,cor_do_jogador)) or (ut.peca_ameacada(58,cor_do_jogador)) or (type(self.gameTiles[60].pieceOnTile) is not NullPiece ) or (type(self.gameTiles[59].pieceOnTile) is not NullPiece) or (type(self.gameTiles[58].pieceOnTile) is not NullPiece) or (ut.xeque(cor_do_jogador)):
                return True
            else:
                self.gameTiles[59] = Tile(59, King(59, "White"))
                self.gameTiles[60] = Tile(60, Rook(60, "White"))
                self.gameTiles[61] = Tile(61, NullPiece())
                self.gameTiles[57] = Tile(64, NullPiece())
                return False
        if cor_do_jogador == 'BLACK':
            if (self.contagem_movimento_rei_pretas > 0) or (self.contagem_movimento_torre_rma_pretas > 0) or (ut.peca_ameacada(4,cor_do_jogador)) or (ut.peca_ameacada(3,cor_do_jogador)) or (ut.peca_ameacada(2,cor_do_jogador)) or (type(self.gameTiles[4].pieceOnTile) is not NullPiece) or (type(self.gameTiles[3].pieceOnTile) is not NullPiece) or (type(self.gameTiles[2].pieceOnTile) is not NullPiece) or (ut.xeque(cor_do_jogador)):
                return True
            else:
                self.gameTiles[4] = Tile(4,Rook(4,"Black"))
                self.gameTiles[3] = Tile(3, King(3, "Black"))
                self.gameTiles[5] = Tile(5, NullPiece())
                self.gameTiles[1] = Tile(1, NullPiece())
                return False


    def contagem_movimentos(self):
        if self.contagem_de_movimento_sem_tomar_peca == 40:
            print('Empate, 40 movimentos sem nenhuma peça ser tomada')
            return True
        else:
            return False