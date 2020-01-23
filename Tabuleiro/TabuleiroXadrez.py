from Tabuleiro.tile import Tile
from peças.peçanula import NullPiece

class Board():
    
    gameTiles = {}

    def __init__(self):
        pass

    def createBoard(self):
        
        for tile in range(64):
            self.gameTiles[tile] = Tile(tile, NullPiece())

    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('l',end=self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('l',end='\n')
                count = 0