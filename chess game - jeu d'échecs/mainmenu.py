import pygame
from pygame.locals import *


#Constants
SCREEN_HEIGHT = 960
SCREEN_WIDTH = 1440
BACKGROUND = (12,247,129)
BUTTON_COLOR = (46,201,123)


#OOP for buttons
class Button:

    def __init__(self, text, width, height, pos, elevation, onClickCommand):
        # core attributions
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = BUTTON_COLOR


        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width, height))
        self.bottom_color = '#354B5E'

        # text
        self.text_surf = GUI_FONT.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

        # command to execute when clicked
        self.onClickCommand = onClickCommand
    
    def draw(self):
        #elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    exec(self.onClickCommand)
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


#Create window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Game Menu")
GUI_FONT = pygame.font.SysFont("", 30)
btn1 = Button('Start', 200, 40, (SCREEN_WIDTH // 2 - 100,200),5, '')
btn2 = Button('Options', 200, 40, (SCREEN_WIDTH // 2 - 100,250), 5, '')
btn3 = Button('Exit', 200, 40, (SCREEN_WIDTH // 2 - 100, 300), 5, 'pygame.quit()')

#Window loop
run = True
while run:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill(BACKGROUND)
        btn1.draw()
        btn2.draw()
        btn3.draw()
        pygame.display.update()
    except:
        run = False

pygame.quit()
quit()


