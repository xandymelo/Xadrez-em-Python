
import os
from boards.ChessBoard import Board
from pieces.piece import Piece
from boards.move import Move
from pieces.pawn import Pawn
from boards.utilMove import util
from util import Colors, MoveTypes, MoveStatus


class Main():
    def __init__(self):
        pass

    def main(self):
        ut = util()
        chessBoard = Board()
        chessBoard.createBoard()
        cor1 = Colors.WHITE
        cor2 = Colors.BLACK
        move = Move()
        chessBoard.printBoard()
        #x = chessBoard.gameTiles[29].pieceOnTile.possible_mov() 
        x = True
        while x:
            actualMoviment = True
            while actualMoviment:
                jogada1 = input("Jogador1: ")
                jogada1 = MoveTypes.MINOR_CASTLING if jogada1.lower() == "minorCastle" else jogada1
                jogada1 = MoveTypes.MAJOR_CASTLING if jogada1.lower() == "majorCastle" else jogada1
                moviment = move.move_piece(cor1,jogada1)
                actualMoviment = True if moviment == MoveStatus.INVALID_MOVE else False
            chessBoard.printBoard()
            actualMoviment = True
            if ut.xeque_mate(cor2):
                print("Xeque mate!! Brancas vencem")
                x = False
                actualMoviment = False
                break
            if ut.afogamento(cor2):
                print("Empate, rei afogado")
                x = False
                actualMoviment = False
            if move.contagem_movimentos():
                x = False
                actualMoviment = False
                break
            while actualMoviment:
                jogada2 = input("Jogador2: ")
                actualMoviment = move.move_piece(cor2,jogada2)
            chessBoard.printBoard()
            if ut.xeque_mate(cor1):
                print("Xeque mate!! Pretas vencem")
                x = False
                actualMoviment = False
                break
            if ut.afogamento(cor1):
                print("Empate, rei afogado")
                x = False
                actualMoviment = False
            if move.contagem_movimentos():
                x = False
                actualMoviment = False
                break
x = Main()
x.main()

#dividir a função movimentar_peça criando subfunções em utilmove
#reduzir o custo do programa
#pensar em fazer o movimento En Passant
#rei x rei e cavalo ou rei x rei e bispo = empate








