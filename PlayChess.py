import pygame
from board.ChessBoard import Board


pygame.init() #inicialize todos os módulos pygame importados#
gameDisplay = pygame.display.set_mode((800,800)) #Inicialize uma janela ou tela para exibição#
pygame.display.set_caption("PyChess") #Defina a legenda da janela atual#
clock = pygame.time.Clock() #crie um objeto para ajudar a controlar o tempo#



chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()




quitGame = False

while not quitGame:

    for event in pygame.event.get():  #obter eventos da fila#

        if event.type == pygame.QUIT: #inicializar todos os módulos pygame#
            quitGame = True
            pygame.quit()
            quit()

    pygame.display.update() #Atualizar partes da tela para exibições de software#
    clock.tick(60) #atualizar o relógio#
