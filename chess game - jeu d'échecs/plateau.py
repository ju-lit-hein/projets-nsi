from time import sleep
import pygame
from pygame.locals import *
from constants import *


class Board:
    def __init__(self, Width, Height, Rows, Columns, Square, Win)
        self.Width = Width
        self.Height = Height
        self.Rows = Rows
        self.Columns = Columns
        self.Square = Square
        self.Win = Win
        self.Board = []
        self.createBoard()

    def createBoard(self):
        for row in range(self.Rows):
            self.Board.append([0 for i in range(self.Columns)])
            for column in range(self.Columns):
                if row == 1:
                    self.Board[row][column] = Pawn(self.Square, )

'''
pygame.init()

pygame.display.set_caption('Chess Game')
window = pygame.display.set_mode(RES)

#Size of squares
size = 75


#board length, must be even
boardLength = 8
window.fill(MAIN_COLOR)

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pygame.draw.rect(window, WHITE_BOARD_COLOR,[size*z,size*i,size,size])
        else:
            pygame.draw.rect(window, DARK_BOARD_COLOR, [size*z,size*i,size,size])
        cnt +=1
    #since theres an even number of squares go back one value
    cnt-=1
#Add a nice boarder
pygame.draw.rect(window,(0,0,0),[size,size,boardLength*size,boardLength*size],1)

pygame.display.update()
sleep(1)
print()
'''