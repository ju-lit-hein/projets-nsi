from constants import *
import pygame
from pygame.locals import *
import os
import time

pygame.init()

board = pygame.transform.scale(pygame.image.load(os.path.join('img', 'board_alt.png')), (750, 750))
boardBackground = pygame.image.load(os.path.join('img', 'bbg.png'))

turn = 'w'

def screenMenu(win, playerName):
    pygame.font.init()
    global bo, boardBackground
    run = True

    while run:
        win.blit(boardBackground, (0,0))
        font = pygame.font.SysFont('comicsans', 30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                run = False

def updateGameWindow(win, bo, p1, p2, color, ready):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    win.blit(board, (0, 0))
    bo.draw(win, color)
    keyToQuit = font.render('Press on Q to exit the game', 1, LIGHT_COLOR)
    win.blit(keyToQuit, (10, 20))

    if color == 'w':
        colorIndication = font.render('You play WHITE', 1, LIGHT_COLOR)
        win.blit(colorIndication, (width / 2 - colorIndication.get_width / 2, 10))
    else:
        colorIndication = font.render('You play BLACK', 1, LIGHT_COLOR)
        win.blit(colorIndication, (width / 2 - colorIndication.get_width / 2, 10))
    
    if bo.turn == color:
        turnIndication = font.render("it's your turn to play", 1, LIGHT_COLOR)
        win.blit(colorIndication, (width / 2 - turnIndication.get_width / 2, 700))
    else:
        turnIndication = font.render("it's opponent turn to play", 1, LIGHT_COLOR)
        win.blit(colorIndication, (width / 2 - turnIndication.get_width / 2, 700))

    pygame.display.update()    
    
def endScreen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 50)
    txt = font.render(text, 1, RED)
    win.blit(txt, (width / 2 - txt.get_width() / 2, 300))
    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False

def click(pos):
    '''return click position in the board (x, y) 0 <= x,y <= 7'''
    rect = RECT
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        divX = x - rect[0]
        divY = y - rect[1]
        column = int(divX / (rect[2] / 8))
        row = int(divY / (rect[3] / 8))
        return column, row
    return -1, -1

def main():
    global turn, bo, name

    color = 'w'
    count = 0
    run = True

    while run:
        try:
            updateGameWindow(win, bo, color, bo.ready)
        except Exception as e:
            print(e)
            endScreen(win, "Something is wrong with the code")
            run = False
            break

        if not color == 's':
            if bo.checkMate('b'):
                bo.send('winner b')
            elif bo.checkMate('w'):
                bo = n.send('winner w')
        
        if bo.winner == 'w':
            endScreen(win, 'White won this game!')
            run = False
        elif bo.winner == 'b':
            endScreen(win, 'Black won this game!')
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            
            # comprendre à quoi ça sert et si on le garde

            '''if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and color != "s":
                    # quit game
                    if color == "w":
                        bo = n.send("winner b")
                    else:
                        bo = n.send("winner w")

            if event.key == pygame.K_RIGHT:
                bo = n.send("forward")

            if event.key == pygame.K_LEFT:
                bo = n.send("back")'''

            if event.type == pygame.MOUSEBUTTONUP and color != 's':
                if color == bo.turn and bo.ready:
                    pos = pygame.mouse.get_pos()
                    bo = n.send('update moves')
                    column, row = click(pos)
                    bo.send(f'select {column} {row} {color}')

    n.disconnect()
    bo = 0
    screenMenu(win)

name = input("What's your player name ? \n")
width = RES[0]
height = RES[1]
win = pygame.display.set_mode((width, height))
screenMenu(win, name)