from boards.ChessBoard import Board
from pieces.nullpiece import NullPiece
from boards.utilMove import util
from boards.tile import Tile
from pieces.piece import Piece





class Move(Piece):
    def __init__(self,contagem_movimento_rei_pretas = 0,contagem_movimento_rei_brancas = 0,contagem_movimento_torre_rm_pretas = 0,contagem_movimento_torre_rm_brancas = 0,contagem_movimento_torre_rma_brancas = 0,contagem_movimento_torre_rma_pretas = 0):
        self.contagem_movimento_rei_pretas = contagem_movimento_rei_pretas
        self.contagem_movimento_rei_brancas = contagem_movimento_rei_brancas
        self.contagem_movimento_torre_rm_pretas = contagem_movimento_torre_rm_pretas
        self.contagem_movimento_torre_rm_brancas = contagem_movimento_torre_rm_brancas
        self.contagem_movimento_torre_rma_brancas = contagem_movimento_torre_rma_brancas
        self.contagem_movimento_torre_rma_pretas = contagem_movimento_torre_rma_pretas
    
    
    
    
    
    
    #AJEITAR ESSA FUNÇÃO E COLOCAR OUTRAS#
    def movimentar_peca(self,cor_do_jogador,input): #mudar o formato do input para o formatov'd2d4'#
        ut = util()
        if input == 'castle':
            self.roque_menor(cor_do_jogador)
            return False
        local_atual = input[0] + input[1]
        novo_local = input[2] + input[3]
        local_atual_convertido = ut.converter_inputs(local_atual)
        novo_local_convertido = ut.converter_inputs(novo_local)
        cor_do_jogador = cor_do_jogador.upper()
        cor_do_adversario = ""
        if cor_do_jogador == "BRANCAS":
            cor_do_jogador = "Brancas"
            cor_do_adversario = "Pretas"
        if cor_do_jogador == "PRETAS":
            cor_do_jogador = 'Pretas'
            cor_do_adversario = "Brancas"

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
        self.gameTiles[novo_local_convertido] = self.gameTiles[local_atual_convertido]
        self.gameTiles[novo_local_convertido].pieceOnTile.position = novo_local_convertido
        self.gameTiles[local_atual_convertido] = Tile(local_atual_convertido,NullPiece())
        print("Jogada feita com sucesso")
        return False
        #else:
            #print("Escolha uma jogada com a cor correta (" + cor_do_jogador + ")")
            #return True
    

    
    
    
    
    
    
    
    
    def roque_menor(self,cor_do_jogador):
        ut = util()
        cor_do_jogador = cor_do_jogador.upper()
        if cor_do_jogador == "BRANCAS":
            if (self.contagem_movimento_rei_brancas > 0) or (self.contagem_movimento_torre_rm_brancas > 0) or (ut.peca_ameacada(6)) or (ut.peca_ameacada(7)) or (self.gameTiles[6] != "") or (self.gameTiles[7] != "") or (ut.xeque(cor_do_jogador)):
                return False
            else:
                self.gameTiles[63] = Tile(63, King(63, "White"))
                self.gameTiles[62] = Tile(62, Rook(62, "White"))
                self.gameTiles[61] = Tile(tile, NullPiece())
                self.gameTiles[64] = Tile(tile, NullPiece())
                return True
        if cor_do_jogador == "PRETAS" or (cor_do_jogador == "NEGRAS"):
            if (self.contagem_movimento_rei_pretas > 0) or (self.contagem_movimento_torre_rm_pretas > 0) or (ut.peca_ameacada(62)) or (ut.peca_ameacada(63)) or (self.gameTiles[63] != "") or (self.gameTiles[62] != "") or (ut.xeque(cor_do_jogador)):
                return False
            else:
                self.movimentar_peca(cor_do_jogador,"Rg8")
                self.movimentar_peca(cor_do_jogador,"Tf8")
                return True


