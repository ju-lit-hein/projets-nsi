from time import sleep
import pygame
from pygame.locals import *
from constants import *

pygame.init()

pygame.display.set_caption('Chess Game')
pygame.display.set_icon(ICON)
window = pygame.display.set_mode(RES)

#Size of squares
size = SQUARE_SIZE

#board length, must be even
boardLength = 8
window.fill(MAIN_COLOR)
window.
cnt = 0
for i in range(1,boardLength+1):
    for z in range(5,boardLength+5):
        # check if it's a white or a black cell
        if cnt % 2 == 0:
            pygame.draw.rect(window, WHITE_BOARD_COLOR,[size * z,size*i,size,size])
        else:
            pygame.draw.rect(window, DARK_BOARD_COLOR, [size*z,size*i,size,size])
        cnt +=1
    cnt-=1
#Add a nice boarder
pygame.draw.rect(window,(0,0,0),[5*size,size,boardLength*size,boardLength*size],1)

pygame.display.update()
sleep(2)
print()