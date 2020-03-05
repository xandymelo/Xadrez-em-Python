import sys

sys.path.append(r'C:\Users\xandy\Documents\GitHub\EstudoXadrez')

from pieces.piece import Piece
from boards.tile import Tile
from pieces.nullpiece import NullPiece
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.king import King
from pieces.bishop import Bishop



class Board(Piece):
    
    

    def __init__(self):
        pass
        
    def createBoard(self):

        for c in range(65):
            self.gameTiles.append(None)
        
        for tile in range(65):
            self.gameTiles[tile] = Tile(tile, NullPiece())
        

        self.gameTiles[1] = Tile(1, Rook(1, "Black"))
        self.gameTiles[2] = Tile(2, Knight(2, "Black"))
        self.gameTiles[3] = Tile(3, Bishop(3, "Black"))
        self.gameTiles[4] = Tile(4, Queen(4, "Black"))
        self.gameTiles[5] = Tile(5, King(5, "Black"))
        self.gameTiles[6] = Tile(6, Bishop(6, "Black"))
        self.gameTiles[7] = Tile(7, Knight(7, "Black"))
        self.gameTiles[8] = Tile(8, Rook(8, "Black"))
        self.gameTiles[9] = Tile(9, Pawn(9, "Black"))
        self.gameTiles[10] = Tile(10, Pawn(10, "Black"))
        self.gameTiles[11] = Tile(11, Pawn(11, "Black"))
        self.gameTiles[12] = Tile(12, Pawn(12, "Black"))
        self.gameTiles[13] = Tile(13, Pawn(13, "Black"))
        self.gameTiles[14] = Tile(14, Pawn(14, "Black"))
        self.gameTiles[15] = Tile(15, Pawn(15, "Black"))
        self.gameTiles[16] = Tile(16, Pawn(16, "Black"))
        
        #self.gameTiles[27] = Tile(27, Bishop(27, "Black"))

        #self.gameTiles[28] = Tile(28,King(28, "White"))

        self.gameTiles[49] = Tile(49, Pawn(49, "White"))
        self.gameTiles[50] = Tile(50, Pawn(50, "White"))
        self.gameTiles[51] = Tile(51, Pawn(51, "White"))
        self.gameTiles[52] = Tile(52, Pawn(52, "White"))
        self.gameTiles[53] = Tile(53, Pawn(53, "White"))
        self.gameTiles[54] = Tile(54, Pawn(54, "White"))
        self.gameTiles[55] = Tile(55, Pawn(55, "White"))
        self.gameTiles[56] = Tile(56, Pawn(56, "White"))
        self.gameTiles[57] = Tile(57, Rook(57, "White"))
        self.gameTiles[58] = Tile(58, Knight(58, "White"))
        self.gameTiles[59] = Tile(59, Bishop(59, "White"))
        self.gameTiles[60] = Tile(60, Queen(60, "White"))
        self.gameTiles[61] = Tile(61, King(61, "White"))
        self.gameTiles[62] = Tile(62, Bishop(62, "White"))
        self.gameTiles[63] = Tile(63, Knight(63, "White"))
        self.gameTiles[64] = Tile(64, Rook(64, "White"))

    def printBoard(self):
        count = 0
        for tiles in range(1,65):
            print(' l ',end=self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('l ',end='\n')
                count = 0
        

        