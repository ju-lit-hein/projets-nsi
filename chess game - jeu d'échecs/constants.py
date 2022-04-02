import pygame
from pygame.locals import *

pygame.font.init()

'''editable constants to custom the game'''
RES = (1280,620)
MAIN_COLOR = ("#27415c")     # vert (<- à effacer) # background
LIGHT_COLOR = ("#efefef")    # blanc ou gris (<- à effacer)  # secondary color
DARK_COLOR = ('#111111')     # noir (<- à effacer) # font color
WHITE_BOARD_COLOR = ("#dfdfdf")
DARK_BOARD_COLOR = ('#5c3427')
RED = ('#ff0000')
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
BOARD_WIDTH = (600, 600)
RECT = (113, 113, 525, 525)
WHITE = 'W'
BLACK = 'B'
HEIGHT = 8
WIDTH = 8