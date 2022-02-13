import time
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
            pygame.draw.circle(win, (0,0,255), (xx+32, yy+30), 34, 4)

        s = None
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] != 0:
                    self.board[row][column].draw(win, color)
                    if self.board[row][column].isSelected():
                        s = (row, column)

    def getDangerMoves(self, color):
        dangerMoves = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] != 0:
                    if self.board[row][column].color != color:
                        for move in self.board[row][column].moveList:
                            dangerMoves.append(move)
        return dangerMoves

    def isChecked(self, color):
        self.updateMoves()
        dangerMoves = self.getDangerMoves(color)
        kingCoord = (-1, -1)
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] != 0:
                    if self.board[row][column].king and self.board[row][column].color == color:
                        kingCoord = (column, row)

        if kingCoord in dangerMoves:
            return True
        return False

    def select(self, column, row, color):
        changer = False
        previous = (-1, -1)
        for loopRow in range(self.rows):
            for loopColumn in range(self.columns):
                if self.board[loopRow][loopColumn] != 0:
                    if self.board[loopRow][loopColumn].selected:
                        previous = (loopRow, loopColumn)

        # if piece
        if self.board[row][column] == 0 and previous != (-1, -1):
            moves = self.board[previous[0]][previous[1]].moveList
            if (column, row) in moves:
                changed = self.move(previous, (row, column), color)
        else:
            if previous == (-1, -1):
                self.reserSelected()
                if self.board[row][column] != 0:
                    self.board[row][column].selected = True
            else:
                if self.board[previous[0]][previous[1]].color != self.board[row][column].color:
                    moves = self.board[previous[0]][previous[1]].moveList
                    if (column, row) in moves:
                        changed = self.move(previous, (row, column), color)
                    if self.board[row][column].color == color:
                        self.board[row][column].selected = True
                else:
                    if self.board[row][column].color == color:
                        # the castling
                        self.resetSelected()
                        if self.board[previous[0]][previous[1]].moved == False and self.board[previous[0]][previous[1]].rook and self.board[row][column].king and column != previous[1] and previous != (-1, -1):
                            castle = True
                            if previous[1] < column:
                                for loopColumn in range(previous[1] + 1, column):
                                    if self.board[row][loopColumn] != 0:
                                        castle = False
                                
                                if castle:
                                    changed = self.move(previous, (row, 3), color)
                                    changed = self.move((row, column), (row, 2), color)
                                if not changed:
                                    self.board[row][column].selected = True
                            else:
                                for loopColumn in range(column + 1, previous[1]):
                                    if self.board[row][loopColumn] != 0:
                                        castle = False
                                if castle:
                                    changed = self.move(previous, (row, 6), color)
                                    changed = self.move((row, column), (row, 5), color)
                                if not changed:
                                    self.board[row][column].selected = True
                        else:
                            self.board[row][column].selected = True
        if changed:
            if self.turn == 'w':
                self.turn = 'b'
                self.resetSelected()
            else:
                self.turn = 'w'
                self.resetSelected()

    def resetSelected(self):
        for row in range(self.rows):
            for column in range(self.column):
                if self.board[row][column] != 0:
                    self.board[row][column].selected = False

    def checkMate(self, color):
        if self.isChecked(color):
            king = None
            for row in range(self.rows):
                for column in range(self.columns):
                    if self.board[row][column] != 0:
                        if self.board[row][column].king and self.board[row][column].color == color:
                            king = self.board[row][column]
                if king is not None:
                    validMoves = king.validMoves(self.board)
                    dangerMoves = self.getDangerMoves(color)
                    dangerCount = 0
                    for move in validMoves:
                        if move in dangerMoves:
                            dangerCount += 1
                    return dangerCount == len(validMoves)

        
        return False

    def move(self, start, end, color):
        checkedBefore = self.isChecked(color)
        changed = True
        nBoard = self.board.copy()
        if nBoard[end[0]][end[1]].pawn:
            nBoard[end[0]][end[1]].first = False

        nBoard[start[0]][start[1]].changePos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard

        if self.isChecked(color) or (checkedBefore and self.isChecked(color)):
            changed = False
            nBoard = self.board.copy()
            if nBoard[end[0]][end[1]].pawn:
                nBoard[end[0]][end[1]].first = True

            nBoard[end[0]][end[1]].changePos((start[0], start[1]))
            nBoard[start[0]][start[1]] = nBoard[end[0]][end[1]]
            nBoard[end[0]][end[1]] = 0
            self.board = nBoard
        else:
            self.resetSelected()
        
        self.updateMoves()
        if changed:
            self.last = [start, end]
        return changed        

















































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