from time import sleep
import pygame
from pygame.locals import *
from constants import *
from pieces import *


class Board:
    rect = ()
    X = rect[0]
    Y = rect[1]
    def __init__(self, rows, columns):
        self.rows = rows
        self.colums = columns
        self.ready = False
        self.last = None
        self.copy = True
        self.board = [[0 for _ in range(8)] for _ in range(rows)] # board[0] = first row from the bottom ; board[0][0] = first cell in the firs row from the left
        self.creatBoard()
        self.p1Name = 'Player 1'
        self.p2Name = 'player 2'
        self.turn = 'w'
        self.winner = None

    def createBoard(self):
        colors = ['b', 'w']        
        p_rows = [1,6] # Pawn rows
        o_rows = [0,7] # Other pieces rows

        # Make pawns

        for i in range(2):
            for n in range(8):
                self.board[p_rows[i]][n] = Pawn(p_rows[i], n, colors[i]) # board[row = p_rows[i]][column = n]

        # Make other pieces

        for i in range(2):
            self.board[o_rows[i]][0] = Rook(o_rows[i], 0, colors[i]) # board[row = o_rows[i]][column = 0]
            self.board[o_rows[i]][1] = Knight(o_rows[i], 1, colors[i]) # board[row = o_rows[i]][column = 1]
            self.board[o_rows[i]][2] = Bishop(o_rows[i], 2, colors[i]) # board[row = o_rows[i]][column = 2]
            self.board[o_rows[i]][3] = Queen(o_rows[i], 3, colors[i]) # board[row = o_rows[i]][column = 3]
            self.board[o_rows[i]][4] = King(o_rows[i], 4, colors[i]) # board[row = o_rows[i]][column = 4]
            self.board[o_rows[i]][5] = Bishop(o_rows[i], 5, colors[i]) # board[row = o_rows[i]][column = 5]
            self.board[o_rows[i]][6] = Knight(o_rows[i], 6, colors[i]) # board[row = o_rows[i]][column = 6]
            self.board[o_rows[i]][7] = Rook(o_rows[i], 7, colors[i]) # board[row = o_rows[i]][column = 7]

    def updateMoves(self):
        for row in range(self.rows):
            for column in range(self.colums):
                if self.board[row][column] != 0:
                    self.board[row][column].updateValidMoves(self.board)

    def draw(self, win, color):
        if self.last and color == self.turn:
            y, x = self.last[0]
            y1, x1 = self.last[1]

            xx = (4 - x) + round(self.X + (x * self.rect[2] / 8))
            yy = 3 + round(self.Y + (y * self.rect[3] / 8))
            pygame.draw.circle(win, (0,0,,255), (xx+32, yy+30), 34, 4)

        s = None
        

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