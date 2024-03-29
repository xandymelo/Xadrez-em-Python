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
from util import Colors



class Board(Piece):
    
    

    def __init__(self):
        pass
        
    def createBoard(self):

        for c in range(65):
            self.gameTiles.append(None)
        
        for tile in range(65):
            self.gameTiles[tile] = Tile(tile, NullPiece())
        

        self.gameTiles[1] = Tile(1, Rook(1, Colors.BLACK))
        # self.gameTiles[2] = Tile(2, Knight(2, Colors.BLACK))
        # self.gameTiles[3] = Tile(3, Bishop(3, Colors.BLACK))
        # self.gameTiles[4] = Tile(4, Queen(4, Colors.BLACK))
        self.gameTiles[5] = Tile(5, King(5, Colors.BLACK))
        # self.gameTiles[6] = Tile(6, Bishop(6, Colors.BLACK))
        # self.gameTiles[7] = Tile(7, Knight(7, Colors.BLACK))
        # self.gameTiles[8] = Tile(8, Rook(8, Colors.BLACK))
        # self.gameTiles[9] = Tile(9, Pawn(9, Colors.BLACK))
        self.gameTiles[10] = Tile(10, Pawn(10, Colors.BLACK))
        # self.gameTiles[11] = Tile(11, Pawn(11, Colors.BLACK))
        # self.gameTiles[12] = Tile(12, Pawn(12, Colors.BLACK))
        # self.gameTiles[13] = Tile(13, Pawn(13, Colors.BLACK))
        # self.gameTiles[14] = Tile(14, Pawn(14, Colors.BLACK))
        # self.gameTiles[15] = Tile(15, Pawn(15, Colors.BLACK))
        # self.gameTiles[16] = Tile(16, Pawn(16, Colors.BLACK))


        
        #self.gameTiles[35] = Tile(35, Bishop(35, Colors.WHITE))

        #self.gameTiles[14] = Tile(14,Queen(14, Colors.WHITE))

        # self.gameTiles[49] = Tile(49, Pawn(49, Colors.WHITE))
        # self.gameTiles[50] = Tile(50, Pawn(50, Colors.WHITE))
        # self.gameTiles[51] = Tile(51, Pawn(51, Colors.WHITE))
        # self.gameTiles[52] = Tile(52, Pawn(52, Colors.WHITE))
        self.gameTiles[53] = Tile(53, Pawn(53, Colors.WHITE))
        # self.gameTiles[54] = Tile(54, Pawn(54, Colors.WHITE))
        # self.gameTiles[55] = Tile(55, Pawn(55, Colors.WHITE))
        # self.gameTiles[56] = Tile(56, Pawn(56, Colors.WHITE))
        # self.gameTiles[57] = Tile(57, Rook(57, Colors.WHITE))
        # self.gameTiles[58] = Tile(58, Knight(58, Colors.WHITE))
        # self.gameTiles[59] = Tile(59, Bishop(59, Colors.WHITE))
        # self.gameTiles[60] = Tile(60, Queen(60, Colors.WHITE))
        self.gameTiles[61] = Tile(61, King(61, Colors.WHITE))
        # self.gameTiles[62] = Tile(62, Bishop(62, Colors.WHITE))
        # self.gameTiles[63] = Tile(63, Knight(63, Colors.WHITE))
        self.gameTiles[64] = Tile(64, Rook(64, Colors.WHITE))

    def printBoard(self):
        countSquares = 0
        countColumns = 8
        for tiles in range(1,65):
            if (tiles % 8 == 1):
                print(countColumns, end='')
                countColumns -= 1
            print(' | ',end=self.gameTiles[tiles].pieceOnTile.toString())
            countSquares += 1
            if countSquares == 8:
                print(' | ',end='\n')
                countSquares = 0
        print("X | A | B | C | D | E | F | G | H |")

        