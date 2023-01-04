
from boards.ChessBoard import Board
from boards.move import Move
from boards.utilMove import util
from util import Colors, MoveTypes, Status


class Main():
    def __init__(self):
        pass

    def start_game(self):
        ut = util()
        chessBoard = Board()
        chessBoard.createBoard()
        white = Colors.WHITE
        black = Colors.BLACK
        move = Move()
        chessBoard.printBoard()
        #x = chessBoard.gameTiles[29].pieceOnTile.possible_mov() 
        x = True
        while x:
            actualMoviment = True
            while actualMoviment:
                jogada1 = input("Jogador1: ")
                jogada1 = MoveTypes.MINOR_CASTLING if jogada1.lower() == "minorcastle" else MoveTypes.MAJOR_CASTLING if jogada1.lower() == "majorcastle" else jogada1
                moviment = move.move_piece(white,jogada1)
                actualMoviment = True if moviment == Status.INVALID else False
            chessBoard.printBoard()
            actualMoviment = True
            if ut.checkmate(black):
                print("Xeque mate!! Brancas vencem")
                x = False
                actualMoviment = False
                break
            if ut.stalemate(black):
                print("Empate, rei afogado")
                x = False
                actualMoviment = False
            if move.contagem_movimentos():
                x = False
                actualMoviment = False
                break
            while actualMoviment:
                jogada2 = input("Jogador2: ")
                jogada2 = MoveTypes.MINOR_CASTLING if jogada2.lower() == "minorcastle" else MoveTypes.MAJOR_CASTLING if jogada2.lower() == "majorcastle" else jogada2
                moviment = move.move_piece(black,jogada2)
                actualMoviment = True if moviment == Status.INVALID else False
            chessBoard.printBoard()
            if ut.checkmate(white):
                print("Xeque mate!! Pretas vencem")
                x = False
                actualMoviment = False
                break
            if ut.stalemate(white):
                print("Empate, rei afogado")
                x = False
                actualMoviment = False
            if move.contagem_movimentos():
                x = False
                actualMoviment = False
                break
if __name__ == '__main__':
    match = Main()
    match.start_game()

#dividir a função movimentar_peça criando subfunções em utilmove
#reduzir o custo do programa
#pensar em fazer o movimento En Passant
#rei x rei e cavalo ou rei x rei e bispo = empate








