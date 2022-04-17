import pygame
from pygame.locals import *

pygame.font.init()

'''editable constants to custom the game'''
COLOR_BLACK = (17, 17, 17)     # noir (<- à effacer) # font color
COLOR_BLUE = (32, 129, 219)
COLOR_GREEN = (39, 65, 92)     # vert (<- à effacer) # background
COLOR_RED = (215, 75, 75)
COLOR_WHITE = (239, 239, 239)    # blanc ou gris (<- à effacer)  # secondary color
BLACK_BOARD_COLOR =  (92, 52, 39)
RES = (1280,620)
WHITE_BOARD_COLOR = (223, 223, 223)
FONT = pygame.font.SysFont('Corbel', 30) # font and font size

### Pieces and skins

'''edit this to break the IA (higher number is more important)'''
PAWN_VALUE = 100
ROOK_VALUE = 500
KNIGHT_VALUE = 320
BISHOP_VALUE = 330
QUEEN_VALUE = 900
KING_VALUE = 20000


'''uneditable constants (could break the game)'''
BLACK = 'B'
BOARD_WIDTH = 600       # change this to an operation that center the board whatever are window dimensions
BOARD_HEIGHT = 600      # change this to an operation that center the board whatever are window dimensions
HEIGHT = 8
RECT = (113, 113, 525, 525)
WHITE = 'W'
WIDTH = 8
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 720




# put here constants from all *menu.py files