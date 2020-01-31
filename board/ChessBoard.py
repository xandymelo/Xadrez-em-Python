from board.tile import Tile
from pieces.nullpiece import NullPiece
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.nullpiece import NullPiece
from pieces.knight import Knight
from pieces.king import King
from pieces.bishop import Bishop

class Board():
    
    gameTiles = []
    primeira_coluna = [x for x in range(1,65) if x % 8 == 1]
    primeira_e_segunda_coluna = [x for x in range(1,65) if x % 8 == 1 or x % 8 == 2]
    penultima_e_ultima_coluna = [x for x in range(1,65) if x % 8 == 7 or x % 8 == 0]
    primeira_e_segunda_linha = [x for x in range(1,17)]
    penultima_e_ultima_linha = [x for x in range(49,65)]
    ultima_coluna = [x for x in range(1,64) if x % 8 == 0]
    ultima_linha = [x for x in range(56,65)]
    primeira_linha = [x for x in range(1,9)]

    def __init__(self):
        pass
        
    def createBoard(self):
        
        for tile in range(1,65):
            self.gameTiles[tile] = Tile(tile, NullPiece())
        

        self.gameTiles[1] = Tile(1, Rook("Black", 1))
        self.gameTiles[2] = Tile(2, Knight("Black", 2))
        self.gameTiles[3] = Tile(3, Bishop("Black", 3))
        self.gameTiles[4] = Tile(4, Queen("Black", 4))
        self.gameTiles[5] = Tile(5, King("Black", 5))
        self.gameTiles[6] = Tile(6, Bishop("Black", 6))
        self.gameTiles[7] = Tile(7, Knight("Black", 7))
        self.gameTiles[8] = Tile(8, Rook("Black", 8))
        self.gameTiles[9] = Tile(9, Pawn("Black", 9))
        self.gameTiles[10] = Tile(10, Pawn("Black", 10))
        self.gameTiles[11] = Tile(11, Pawn("Black", 11))
        self.gameTiles[12] = Tile(12, Pawn("Black", 12))
        self.gameTiles[13] = Tile(13, Pawn("Black", 13))
        self.gameTiles[14] = Tile(14, Pawn("Black", 14))
        self.gameTiles[15] = Tile(15, Pawn("Black", 15))
        self.gameTiles[16] = Tile(16, Pawn("Black", 16))

        self.gameTiles[49] = Tile(49, Pawn("White", 49))
        self.gameTiles[50] = Tile(50, Pawn("White", 50))
        self.gameTiles[51] = Tile(51, Pawn("White", 51))
        self.gameTiles[52] = Tile(52, Pawn("White", 52))
        self.gameTiles[53] = Tile(53, Pawn("White", 53))
        self.gameTiles[54] = Tile(54, Pawn("White", 54))
        self.gameTiles[55] = Tile(55, Pawn("White", 55))
        self.gameTiles[56] = Tile(56, Pawn("White", 56))
        self.gameTiles[57] = Tile(57, Rook("White", 57))
        self.gameTiles[58] = Tile(58, Knight("White", 58))
        self.gameTiles[59] = Tile(59, Bishop("White", 59))
        self.gameTiles[60] = Tile(60, Queen("White", 60))
        self.gameTiles[61] = Tile(61, King("White", 61))
        self.gameTiles[62] = Tile(62, Bishop("White", 62))
        self.gameTiles[63] = Tile(63, Knight("White", 63))
        self.gameTiles[64] = Tile(64, Rook("White", 64))

    def printBoard(self):
        count = 0
        for tiles in range(1,65):
            print(' l ',end=self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('l ',end='\n')
                count = 0
        

        