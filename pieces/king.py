from pieces.piece import Piece
from boards.utilMove import util
from util import Colors, BLACK_PIECES, WHITE_PIECES

class King(Piece):

    
    def __init__(self, position, alliance):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "♔" if self.alliance == Colors.BLACK else "♚"
    
    def possible_mov(self):
        ut = util()
        color_of_the_player = self.alliance
        possible_moves = []
        possible_moves.append(self.position + 8)
        possible_moves.append(self.position - 8)
        possible_moves.append(self.position + 7)
        possible_moves.append(self.position - 7)
        possible_moves.append(self.position + 1)
        possible_moves.append(self.position - 1)
        possible_moves.append(self.position + 9)
        possible_moves.append(self.position - 9)
        if self.position in self.primeira_linha:
            possible_moves.remove(self.position - 8)
            possible_moves.remove(self.position - 7)
            possible_moves.remove(self.position - 9)
        if self.position in self.ultima_linha:
            possible_moves.remove(self.position + 7)
            possible_moves.remove(self.position + 8)
            possible_moves.remove(self.position + 9)
        if self.position in self.primeira_coluna:
            possible_moves.remove(self.position - 1)
            if self.position + 7 in possible_moves:
                possible_moves.remove(self.position + 7)
            if self.position - 9 in possible_moves:
                possible_moves.remove(self.position - 9)
        if self.position in self.ultima_coluna:
            possible_moves.remove(self.position + 1)
            if self.position + 9 in possible_moves:
                possible_moves.remove(self.position + 9)
            if self.position - 7 in possible_moves:
                possible_moves.remove(self.position - 7)

        remove = []
        if color_of_the_player == Colors.WHITE:
            opponent_possible_moves = self.all_possible_moves(color_of_the_player)
            for c in range(len(possible_moves)):
                if ut.threat_piece(possible_moves[c],opponent_possible_moves) or self.gameTiles[possible_moves[c]].pieceOnTile.toString() in BLACK_PIECES or self.gameTiles[possible_moves[c]].pieceOnTile.toString() in WHITE_PIECES:
                    remove.append(possible_moves[c])
        if color_of_the_player == Colors.BLACK:
            opponent_possible_moves =  self.all_possible_moves(color_of_the_player)
            for c in range(len(possible_moves)):
                if ut.threat_piece(possible_moves[c], opponent_possible_moves) or self.gameTiles[possible_moves[c]].pieceOnTile.toString() in WHITE_PIECES or self.gameTiles[possible_moves[c]].pieceOnTile.toString() in BLACK_PIECES:
                    remove.append(possible_moves[c])
        return [move for move in possible_moves if move not in remove]
        