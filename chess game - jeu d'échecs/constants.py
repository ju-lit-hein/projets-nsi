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
FONT = pygame.font.SysFont('Corbel', 30) # font and font size

'''uneditable constants (could break the game)'''
BOARD_WIDTH = (600, 600)