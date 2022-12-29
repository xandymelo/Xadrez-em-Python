from boards.ChessBoard import Board
from pieces.nullpiece import NullPiece
from boards.utilMove import util
from boards.tile import Tile
from pieces.piece import Piece
from pieces.king import King
from pieces.rook import Rook
from util import Colors, Status, MoveTypes
# import copy





class Move(Piece):
    def __init__(self,black_king_move_counts = 0,white_king_move_counts = 0,count_move_black_king_rook = 0,count_move_white_king_rook = 0,count_move_white_queen_rook = 0,count_move_black_queen_rook = 0):
        self.black_king_move_counts = black_king_move_counts
        self.white_king_move_counts = white_king_move_counts
        self.count_move_black_king_rook = count_move_black_king_rook
        self.count_move_white_king_rook = count_move_white_king_rook
        self.count_move_white_queen_rook = count_move_white_queen_rook
        self.count_move_black_queen_rook = count_move_black_queen_rook
        self.move_count_without_taking_piece = 0
    
    #AJEITAR ESSA FUNÇÃO E COLOCAR OUTRAS#
    def move_piece(self,color_of_the_player,moveType): #mudar o formato do input para o formatov'd2d4'#
        ut = util()
        opponent_player_color = Colors.WHITE if color_of_the_player == Colors.BLACK else Colors.WHITE
        if moveType == MoveTypes.MINOR_CASTLING: 
            move = self.minor_castle(color_of_the_player)
            if move:
                print("Rock done successfully")
                return Status.VALID
            else:
                print("Unable to rock")
                return Status.INVALID
        elif moveType == MoveTypes.MAJOR_CASTLING:
            move = self.major_castle(color_of_the_player)
            if move:
                print("Rock done successfully")
                return Status.VALID
            else:
                print("Unable to rock")
                return Status.INVALID
        if (len(moveType) == 0) or not (moveType[0].isalpha() and moveType[1].isdigit() and moveType[2].isalpha() and moveType[3].isdigit()):
            print("invalid move")
            return Status.INVALID
        

        current_location = moveType[0] + moveType[1]
        new_location = moveType[2] + moveType[3]
        converted_current_location = ut.convert_positions(current_location)
        converted_new_location = ut.convert_positions(new_location)
            
        #criar a parte que verifica se a jogada é válida#
        verification = ut.check_if_move_is_valid(converted_current_location,converted_new_location)
        if not verification or (self.gameTiles[converted_current_location].pieceOnTile.alliance != color_of_the_player):
            print('invalid move')
            return Status.INVALID


        piece_name = self.gameTiles[converted_current_location].pieceOnTile.toString()
        if piece_name == "♔":
            self.black_king_move_counts += 1
        if piece_name == "♚":
            self.white_king_move_counts += 1
        if piece_name == "♖":
            if converted_current_location == 64:
                self.count_move_black_king_rook += 1
            if converted_current_location == 57:
                self.count_move_black_queen_rook += 1
        if piece_name == "♜":
            if converted_current_location == 8:
                self.count_move_white_king_rook += 1
            if converted_current_location == 1:
                self.count_move_white_queen_rook += 1
        move = ut.check_if_move_is_possible(color_of_the_player,converted_current_location,converted_new_location)
        if not move:
            print('invalid move')
            return Status.INVALID
        if self.gameTiles[converted_new_location].pieceOnTile.toString() == '-':
            self.move_count_without_taking_piece += 1
        else:
            self.move_count_without_taking_piece = 0
        
        
        self.gameTiles[converted_new_location] = self.gameTiles[converted_current_location]
        self.gameTiles[converted_new_location].tileCoordinate = converted_new_location
        self.gameTiles[converted_new_location].pieceOnTile.position = converted_new_location
        self.gameTiles[converted_current_location] = Tile(converted_current_location,NullPiece())
        print("Jogada feita com sucesso")
        if ut.is_check(opponent_player_color):
            print('xeque!')
        return Status.VALID

        #else:
            #print("Escolha uma jogada com a cor correta (" + cor_do_jogador + ")")
            #return True
    
    def minor_castle(self,color_of_the_player):
        ut = util()
        if color_of_the_player == Colors.WHITE:
            if (self.white_king_move_counts > 0) or (self.count_move_white_king_rook > 0) or (ut.peca_ameacada(62,color_of_the_player)) or (ut.peca_ameacada(63,color_of_the_player)) or (type(self.gameTiles[62].pieceOnTile) is not NullPiece ) or (type(self.gameTiles[63].pieceOnTile) is not NullPiece) or (ut.is_check(color_of_the_player)):
                return False
            else:
                self.gameTiles[63] = Tile(63, King(63, Colors.WHITE))
                self.gameTiles[62] = Tile(62, Rook(62, Colors.WHITE))
                self.gameTiles[61] = Tile(61, NullPiece())
                self.gameTiles[64] = Tile(64, NullPiece())
                return True
        if color_of_the_player == Colors.BLACK:
            if (self.black_king_move_counts > 0) or (self.count_move_black_king_rook > 0) or (ut.peca_ameacada(6,color_of_the_player)) or (ut.peca_ameacada(7,color_of_the_player)) or (type(self.gameTiles[6].pieceOnTile) is not NullPiece) or (type(self.gameTiles[7].pieceOnTile) is not NullPiece) or (ut.is_check(color_of_the_player)):
                return False
            else:
                self.gameTiles[6] = Tile(6,Rook(6,Colors.BLACK))
                self.gameTiles[7] = Tile(7, King(7, Colors.BLACK))
                self.gameTiles[5] = Tile(5, NullPiece())
                self.gameTiles[8] = Tile(8, NullPiece())
                return True


    def major_castle(self,color_of_the_player):
        ut = util()
        if color_of_the_player == Colors.WHITE:
            if (self.white_king_move_counts > 0) or (self.count_move_white_queen_rook > 0) or (ut.peca_ameacada(60,color_of_the_player)) or (ut.peca_ameacada(59,color_of_the_player)) or (ut.peca_ameacada(58,color_of_the_player)) or (type(self.gameTiles[60].pieceOnTile) is not NullPiece ) or (type(self.gameTiles[59].pieceOnTile) is not NullPiece) or (type(self.gameTiles[58].pieceOnTile) is not NullPiece) or (ut.is_check(color_of_the_player)):
                return True
            else:
                self.gameTiles[59] = Tile(59, King(59, "White"))
                self.gameTiles[60] = Tile(60, Rook(60, "White"))
                self.gameTiles[61] = Tile(61, NullPiece())
                self.gameTiles[57] = Tile(64, NullPiece())
                return False
        if color_of_the_player == Colors.BLACK:
            if (self.black_king_move_counts > 0) or (self.count_move_black_queen_rook > 0) or (ut.peca_ameacada(4,color_of_the_player)) or (ut.peca_ameacada(3,color_of_the_player)) or (ut.peca_ameacada(2,color_of_the_player)) or (type(self.gameTiles[4].pieceOnTile) is not NullPiece) or (type(self.gameTiles[3].pieceOnTile) is not NullPiece) or (type(self.gameTiles[2].pieceOnTile) is not NullPiece) or (ut.is_check(color_of_the_player)):
                return True
            else:
                self.gameTiles[4] = Tile(4,Rook(4,"Black"))
                self.gameTiles[3] = Tile(3, King(3, "Black"))
                self.gameTiles[5] = Tile(5, NullPiece())
                self.gameTiles[1] = Tile(1, NullPiece())
                return False


    def contagem_movimentos(self):
        if self.move_count_without_taking_piece == 80:
            print('Empate, 40 movimentos sem nenhuma peça ser tomada')
            return True
        else:
            return False