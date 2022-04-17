import ai
import board
import constants
import pieces
import pygame

class GraphicalUserInterface():

    def __init__(self):
        self.WIDTH = constants.WINDOW_WIDTH
        self.HEIGTH = constants.WINDOW_HEIGHT
        self.BOARD_HEIGHT = constants.BOARD_HEIGHT
        self.BOARD_WIDTH = constants.BOARD_WIDTH

        self.font = 0 # demander à Lukas
        self.title_font_size = 'to be determined'
        self.medium_font_size = 'to be determined'
        self.small_font_size = 'to be determined'

        self.color_red = constants.COLOR_RED
        self.color_green = constants.COLOR_GREEN
        self.color_blue = constants.COLOR_BLUE
        self.color_white = constants.COLOR_WHITE
        self.color_black = constants.COLOR_BLACK

        self.color_black_case = constants.BLACK_BOARD_COLOR
        self.color_white_case = constants.WHITE_BOARD_COLOR