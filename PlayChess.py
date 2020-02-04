#import pygame
import os
from boards.ChessBoard import Board
from pieces.piece import Piece



#pygame.init() #inicialize todos os módulos pygame importados#
#gameDisplay = pygame.display.set_mode((800,800)) #Inicialize uma janela ou tela para exibição#
#pygame.display.set_caption("PyChess") #Defina a legenda da janela atual#
#clock = pygame.time.Clock() #crie um objeto para ajudar a controlar o tempo#



chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()

allTiles = []
allPieces = []


#def squares(x,y,w,h,color):
    #pygame.draw.rect(gameDisplay, color, [x,y,w,h]) #desenhe um retângulo#
    #allTiles.append([color,[x,y,w,h]]) 

#def drawChessPieces():
#    xpos = 0
#    ypos = 0
#    color = 0
#    width = 100
#    height = 100
#    black = (66,134,244)
#    white = (143,155,175)
#    number = 1
#    for _ in range(8):
#        for _ in range(8):
#            if color % 2 == 0:
#                squares(xpos, ypos, width, height, white)
#                if not Piece.gameTiles[number].pieceOnTile.toString() == "-":
#                    img = pygame.image.load("./ChessArt/" + Piece.gameTiles[number].pieceOnTile.alliance[0].upper() + Piece.gameTiles[
#                        number].pieceOnTile.toString().upper() + ".png")
#                    img = pygame.transform.scale(img, (100, 100))
#                    allPieces.append([img, [xpos, ypos], Piece.gameTiles[number].pieceOnTile])
#                xpos += 100
#            else:
#                squares(xpos, ypos, width, height, black)
#                if not Piece.gameTiles[number].pieceOnTile.toString() == "-":
#                    img = pygame.image.load("./ChessArt/" + Piece.gameTiles[number].pieceOnTile.alliance[0].upper() + Piece.gameTiles[
#                        number].pieceOnTile.toString().upper() + ".png")
#                    img = pygame.transform.scale(img, (100, 100))
#                    allPieces.append([img, [xpos, ypos], Piece.gameTiles[number].pieceOnTile])
#                xpos += 100

#            color += 1
#            number += 1
#        color += 1
#        xpos = 0
#        ypos += 100


#drawChessPieces()

#quitGame = False

#while not quitGame:

    #for event in pygame.event.get():  #obter eventos da fila#

        #f event.type == pygame.QUIT: #inicializar todos os módulos pygame#
            #quitGame = True
            #pygame.quit()
            #quit()
    

#   for img in allPieces:
#        gameDisplay.blit(img[0],img[1]) #desenhar uma imagem na outra#

#   pygame.display.update() #Atualizar partes da tela para exibições de software#
#    clock.tick(60) #atualizar o relógio#
