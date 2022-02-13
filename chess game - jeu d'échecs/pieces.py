import pygame
import os


currentDir = os.path.abspath(os.path.curdir)


#Chemins d'accès
path_to_white_pawn = r"s%\\pieces\\pion blanc.gif" % currentDir
path_to_white_bishop = r"s%\\pieces\\fou blanc.gif" % currentDir
path_to_white_knight = r"s%\\pieces\\cavalier blanc.gif" % currentDir
path_to_white_rook = r"s%\\pieces\\tour blanc.gif" % currentDir
path_to_white_queen = r"s%\\pieces\\reine blanc.gif" % currentDir
path_to_white_king = r"s%\\pieces\\roi blanc.gif" % currentDir


path_to_black_pawn = r"s%\\pieces\\pion noir.gif" % currentDir
path_to_black_bishop = r"s%\\pieces\\fou noir.gif" % currentDir
path_to_black_knight = r"s%\\pieces\\cavalier noir.gif" % currentDir
path_to_black_rook = r"s%\\pieces\\tour noir.gif" % currentDir
path_to_black_queen = r"s%\\pieces\\reine noir.gif" % currentDir
path_to_black_king = r"s%\\pieces\\roi noir.gif" % currentDir


#Création des pièces
black_pawn = pygame.image.load(path_to_black_pawn)
black_bishop = pygame.image.load(path_to_black_bishop)
black_knight = pygame.image.load(path_to_black_knight)
black_rook = pygame.image.load(path_to_black_rook)
black_queen = pygame.image.load(path_to_black_queen)
black_king = pygame.image.load(path_to_black_king)


white_pawn = pygame.image.load(path_to_white_pawn)
white_bishop = pygame.image.load(path_to_white_bishop)
white_knight = pygame.image.load(path_to_white_knight)
white_rook = pygame.image.load(path_to_white_rook)
white_queen = pygame.image.load(path_to_white_queen)
white_king = pygame.image.load(path_to_white_king)



bl = [black_bishop, black_king, black_knight, black_pawn, black_queen, black_rook]
wh = [white_bishop, white_king, white_knight, white_pawn, white_queen, white_rook]


BLACK = []
WHITE = []


for img in bl:
    BLACK.append(pygame.transform.scale(img, (55,55)))

for img in wh:
    WHITE.append(pygame.transform.scale(img, (55,55)))


#Création des objets des différentes pièces
class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
        self.king = False
        self.pawn = False
    
    def isSelected(self):
        return self.selected

    def updateValidMoves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, win, color):
        if self.color == 'wh':
            drawThis = WHITE[self.img]
        else:
            drawThis = BLACK[self.img]
        
        x = (4 - self.col) + round(self.startX + (self.col * self.rect[2] / 8))
        y = 3 + round(self.StartY + (self.row * self.rect[3] /8))

        if self.selected and self.color == color:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 62, 62), 4)
        
        win.blit(drawThis, (x,y))
    
    def changePos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def __str__(self):
        return str(self.col) + " " + str(self.row)


class Bishop(Piece):
    img = 0

    def validMoves(self, board):
        i = self.row
        j = self.col

        moves = []

        #TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i-1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break

            djL += 1

        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1
        
        #TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            else:
                break
            djL += 1
        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            else:
                break

            djR -= 1

        return moves


class King(Piece):
    img = 1

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True

    def validMoves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i>0:
            #TOP LEFT
            if j >0:
                p = board[i-1][j-1]
                if p == 0:
                    moves.append((j-1, i-1))
                elif p.color != self.color:
                    moves.append((j-1, i-1))
            
            #TOP MIDDLE
            p = board[i-1][j]
            if p == 0:
                moves.append((j, i-1))
            elif p.color != self.color:
                moves.append((j, i-1))
            
            #TOP RIGHT
            if j <7:
                p = board[i - 1][j+1]
                if p == 0:
                    moves.append((j+1, i-1))
                elif p.color != self.color:
                    moves.append((j+1, i-1))
        
        if i<7:
            #BOTTOM LEFT
            if j>0:
                p = board[i+1][j-1]
                if p == 0:
                    moves.append((j-1, i+1))
                elif p.color != self.color:
                    moves.append((j-1, i+1))
            
            #BOTTOM MIDDLE
            p = board[i+1][j]
            if p == 0:
                moves.append((j, i+1))
            elif p.color != self.color:
                moves.append((j, i+1))
            
            #BOTTOM RIGHT
            p = board[i+1][j+1]
            if p == 0:
                moves.append((j+1, i+1))
            elif p.color != self.color:
                moves.append((j+1, i+1))

        #MIDDLE LEFT
        if j > 0:
            p = board[i][j -1]
            if p == 0:
                moves.append((j-1, i))
            elif p.color != self.color:
                moves.append((j-1, i))
        
        #MIDDLE RIGHT
        if j < 7:
            p = board[i][j+1]
            if p == 0:
                moves.append((j+1, i))
            elif p.color != self.color:
                moves.append((j-+1, i))
        
        return moves


class Knight(Piece):
    img = 2

    def validMoves(self, board):
        i = self.row
        j = self.col

        moves = []

        #DOWN LEFT
        if i<6 and j>0:
            p = board[i +2][j-1]
            if p == 0:
                moves.append((j-1, i+2))
            elif p.color != self.color:
                moves.append((j-1, i+2))
        
        #UP LEFT
        if i >1 and j>0:
            p = board[i-2][j-1]
            if p == 0:
                moves.append((j-1,i-2))
            elif p.color != self.color:
                moves.append((j-1,i-2))
        
        #DOWN RIGHT
        if i <6 and j < 7:
            p = board[i+2][j+1]
            if p == 0:
                moves.append((j+1, i+2))
            elif p.color != self.color:
                moves.append((j+1, i+2))

        #UP RIGHT
        if i > 1 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))
            elif p.color != self.color:
                moves.append((j + 1, i - 2))

        if i > 0 and j > 1:
            p = board[i - 1][j - 2]
            if p == 0:
                moves.append((j - 2, i - 1))
            elif p.color != self.color:
                moves.append((j - 2, i - 1))

        if i > 0 and j < 6:
            p = board[i - 1][j + 2]
            if p == 0:
                moves.append((j + 2, i - 1))
            elif p.color != self.color:
                moves.append((j + 2, i - 1))

        if i < 7 and j > 1:
            p = board[i + 1][j - 2]
            if p == 0:
                moves.append((j - 2, i + 1))
            elif p.color != self.color:
                moves.append((j - 2, i + 1))

        if i < 7 and j < 6:
            p = board[i + 1][j + 2]
            if p == 0:
                moves.append((j + 2, i + 1))
            elif p.color != self.color:
                moves.append((j + 2, i + 1))

        return moves


class Pawn(Piece):
    img = 3

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False
        self.pawn = True

    def validMoves(self, board):
        i = self.row
        j = self.col

        moves = []

        try:
            if self.color == 'bl':
                if i <7:
                    p = board[i+1][j]
                    if p == 0:
                        moves.append((j, i+1))
                
                    #DIAGONAL
                    if j<7:
                        p = board[i+1][j+1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j+1, i+1))
                    
                    if j>0:
                        p = board[i+1][j-1]
                        if p != 0:
                            if p.color != self.color:
                                moves.append((j-1, i+1))

                
                if self.first:
                    if i <6:
                        p = board[i+2][j]
                        if p == 0:
                            if board[i + 1][j] == 0:
                                moves.append((j,i+2))
                        elif p.color != self.color:
                            moves.append((j, i+2))
            
            #WHTIE
            else:

                if i > 0:
                    p = board[i-1][j]
                    if p == 0:
                        moves.append((j, i-1))
                
                if j<7:
                    p = board[i-1][j+1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j+1, i-1))
                
                if j >0:
                    p = board[i-1][j-1]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j-1, i-1))

                if self.first:
                    if i >1:
                        p = board[i-2][j]
                        if p == 0:
                            if board[i-1][j] == 0:
                                moves.append((j, i-2))
                        elif p.color != self.color:
                            moves.append(j, i-2)
        except:
            pass

        return moves


class Queen(Piece):
    img = 4

    def validMoves(self, board):
        i = self.row
        j = self.col

        moves = []

        #TOP RIGHT
        djL = j + 1
        djR = j - 1
        for di in range(i-1,-1,-1):
            if djL <8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    djL = 9
            
            djL += 1
        
        for di in range(i-1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p ==0:
                    moves.append((djR,di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1
            
            djR -= 1
        
        #TOP LEFT
        djL = j + 1
        djR = j - 1
        for di in range(i+1, 8):
            if djL <8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL,di))
                elif p.color != self.color:
                    moves.append((djL,di))
                    break
                else:
                    djL = 9
            
            djL += 1

        for di in range(i+1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    djR = -1

            djR -=1

        
        #UP
        for x in range(i-1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        
        #DOWN
        for x in range(i+1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        
        #LEFT
        for x in range(j-1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x,i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        
        #RIGHT
        for x in range(j+1, 8, 1):
            p =  board[i][x]
            if p == 0:
                moves.append((x,i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        
        return moves


class Rook(Piece):
    img = 5

    def validMoves(self, board):
        i = self.row
        j = self.col

        moves = []

        #UP
        for x in range(i-1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j,x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        #DOWN
        for x in range(i+1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j,x))
            elif p.color != self.color:
                moves.append((j,x))
                break
            else:
                break
        
        #LEFT
        for x in range(j-1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        
        #RIGHT
        for x in range(j+1, 8, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break
        
        return moves