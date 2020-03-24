
import os
from boards.ChessBoard import Board
from pieces.piece import Piece
from boards.move import Move
from pieces.pawn import Pawn
from boards.utilMove import util


class Main():
    def __init__(self):
        pass

    def main(self):
        ut = util()
        chessBoard = Board()
        chessBoard.createBoard()
        cor1 = "white"
        cor2 = 'Black'
        move = Move()
        chessBoard.printBoard()
        #x = chessBoard.gameTiles[29].pieceOnTile.possible_mov() 
        x = True
        while x:
            moviment = True

            while moviment:
                jogada1 = input("Jogador1: ")
                moviment = move.movimentar_peca(cor1,jogada1)
            chessBoard.printBoard()
            moviment = True
            if ut.xeque_mate(cor2):
                print("Xeque mate!! Brancas vencem")
                x = False
                moviment = False
                break
            if ut.afogamento(cor2):
                print("Empate, rei afogado")
                x = False
                moviment = False
            if move.contagem_movimentos():
                x = False
                moviment = False
                break
            while moviment:
                jogada2 = input("Jogador2: ")
                moviment = move.movimentar_peca(cor2,jogada2)
            chessBoard.printBoard()
            if ut.xeque_mate(cor1):
                print("Xeque mate!! Pretas vencem")
                x = False
                moviment = False
                break
            if ut.afogamento(cor1):
                print("Empate, rei afogado")
                x = False
                moviment = False
            if move.contagem_movimentos():
                x = False
                moviment = False
                break
x = Main()
x.main()

#reduzir o custo do programa
#dividir a função movimentar_peça criando subfunções em utilmove
#pensar em fazer o movimento En Passant
#40 lances sem tomar peça = empate
#rei x rei e cavalo ou rei x rei e bispo = empate








