from pieces.piece import Piece
from boards.tile import Tile
from pieces.nullpiece import NullPiece
import copy
from util import Colors

class util(Piece):
    def __init__(self):
        pass

    def convert_positions(self,input):
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
    

    
    def is_check(self,color_of_the_player):#Aqui irei verificar se a casa do rei está na lista de movimentos possiveis (lembrando que a função de todos os movimentos possiveis não inclui os movimentos do rei  #
        kings_house = ""
        if color_of_the_player == Colors.BLACK:
            kings_house = self.get_kings_house(color_of_the_player)
            possible_moves = self.all_possible_moves(Colors.BLACK)
            if kings_house in possible_moves:
                return True
            else:
                return False
        if color_of_the_player == Colors.WHITE:
            kings_house = self.get_kings_house(color_of_the_player)
            possible_moves = self.all_possible_moves(Colors.WHITE)
            if kings_house in possible_moves:
                return True
            else:
                return False

    def check_if_move_is_valid(self,local_atual_convertido,novo_local_convertido):
        mov_possiveis_da_peca = self.gameTiles[local_atual_convertido].pieceOnTile.possible_mov()
        if (not (novo_local_convertido in mov_possiveis_da_peca)):
            return False
        else:
            return True

    def threat_piece(self,current_location, opponent_possible_moves):
        if current_location in opponent_possible_moves:
            return True
        else:
            return False

    def peca_cravada(self,cor_do_jogador):
        if self.threat_piece(self.position,cor_do_jogador):
            x = copy.deepcopy(self.gameTiles[self.position])
            self.gameTiles[self.position] = Tile(self.position, NullPiece())  #usar deepcopy
            if self.is_check(self.alliance):
                self.gameTiles[self.position] = x
                return True
            else:
                self.gameTiles[self.position] = x
                return False   
        else:
            return False
    def checkmate(self,color_of_the_player):
        if self.is_check(color_of_the_player):
            return self.the_king_has_moves(color_of_the_player)
        return False
                
    def get_kings_house(self,color_of_the_player):
        if color_of_the_player == Colors.BLACK:
            for c in self.gameTiles:
                if c.pieceOnTile.toString() == "♔":
                    kings_house = c.pieceOnTile.position
                    break
        if color_of_the_player == Colors.WHITE:
            for c in self.gameTiles:
                if c.pieceOnTile.toString() == "♚":
                    kings_house = c.pieceOnTile.position
                    break
        return kings_house
    def check_if_move_is_possible(self,color_of_the_player,converted_current_location,converted_new_location):
        if ( self.gameTiles[converted_new_location].pieceOnTile.alliance == color_of_the_player ):
            return False
        ut = util()
        copy_new_location_tile = copy.deepcopy(self.gameTiles[converted_new_location])
        self.gameTiles[converted_new_location] = self.gameTiles[converted_current_location]
        self.gameTiles[converted_new_location].tileCoordinate = converted_new_location
        self.gameTiles[converted_new_location].pieceOnTile.position = converted_new_location
        self.gameTiles[converted_current_location] = Tile(converted_current_location,NullPiece())
        if ut.is_check(color_of_the_player):
            self.gameTiles[converted_current_location] = self.gameTiles[converted_new_location]
            self.gameTiles[converted_current_location].tileCoordinate = converted_current_location
            self.gameTiles[converted_current_location].pieceOnTile.position = converted_current_location
            self.gameTiles[converted_new_location] = copy_new_location_tile
            return False
        self.gameTiles[converted_current_location] = self.gameTiles[converted_new_location]
        self.gameTiles[converted_current_location].tileCoordinate = converted_current_location
        self.gameTiles[converted_current_location].pieceOnTile.position = converted_current_location
        self.gameTiles[converted_new_location] = copy_new_location_tile
        return True
    
    
    def stalemate(self,color_of_the_player):
        if not self.is_check(color_of_the_player):
            #cor_do_jogador_adversario = self.achar_a_cor_do_adversario(cor_do_jogador)
            casa_do_rei = self.get_kings_house(color_of_the_player)
            x = self.all_possible_moves(color_of_the_player)
            if casa_do_rei + 8 in x:
                x.remove(casa_do_rei + 8)
            if casa_do_rei - 8 in x:
                x.remove(casa_do_rei - 8)
            if casa_do_rei + 7 in x:
                x.remove(casa_do_rei + 7)
            if casa_do_rei - 7 in x:
                x.remove(casa_do_rei - 7)
            if casa_do_rei + 1 in x:
                x.remove(casa_do_rei + 1)
            if casa_do_rei - 1 in x:
                x.remove(casa_do_rei - 1)
            if casa_do_rei + 9 in x:    
                x.remove(casa_do_rei + 9)
            if casa_do_rei - 9 in x:
                x.remove(casa_do_rei - 9)
            if x == []:
                return self.the_king_has_moves(color_of_the_player)
        return False
    

    def the_king_has_moves(self,color_of_the_player):
        kings_house = self.get_kings_house(color_of_the_player)
        if self.gameTiles[kings_house].pieceOnTile.possible_mov() == []:
            return False
        soma = 0 
        for moves in self.gameTiles[kings_house].pieceOnTile.possible_mov():
            x = self.check_if_move_is_possible(color_of_the_player,kings_house,moves)
            if x:
                soma += 1
        if soma == len(self.gameTiles[kings_house].pieceOnTile.possible_mov()):
            return True
        return False

    # def achar_a_cor_do_adversario(self,cor_do_jogador):
    #     cor_do_jogador = cor_do_jogador.upper()
    #     cor_do_jogador_adversario = ""
    #     if cor_do_jogador == "WHITE":
    #         cor_do_jogador_adversario = "BLACK"
    #     elif cor_do_jogador == "BLACK":
    #         cor_do_jogador_adversario = 'WHITE'
    #     return cor_do_jogador_adversario