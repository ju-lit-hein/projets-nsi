import plateau
from os import path
import turtle

currentDir = path.abspath(path.curdir) #get the python file location

def creer_les_images_des_pieces():
    '''ajoute les images des pièces'''
    plateau.wn.addshape(currentDir + "\\pieces\\cavalier blanc.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\fou blanc.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\pion blanc.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\reine blanc.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\roi blanc.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\tour blanc.gif")

    plateau.wn.addshape(currentDir + "\\pieces\\cavalier noir.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\fou noir.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\pion noir.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\reine noir.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\roi noir.gif")
    plateau.wn.addshape(currentDir + "\\pieces\\tour noir.gif")

def creer_les_tortues_des_pions():
    pass

pion_blanc_1 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_2 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_3 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_4 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_5 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_6 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_7 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")
pion_blanc_8 = turtle.Turtle(shape=currentDir + "\\pieces\\pion blanc.gif")

fou_blanc_1 = turtle.Turtle(shape=currentDir + "\\pieces\\fou blanc.gif")
fou_blanc_2 = turtle.Turtle(shape=currentDir + "\\pieces\\fou blanc.gif")
cavalier_blanc_1 = turtle.Turtle(shape=currentDir + "\\pieces\\cavalier blanc.gif")
cavalier_blanc_2 = turtle.Turtle(shape=currentDir + "\\pieces\\cavalier blanc.gif")
tour_blanc_1 = turtle.Turtle(shape=currentDir + "\\pieces\\tour blanc.gif")
tour_blanc_2 = turtle.Turtle(shape=currentDir + "\\pieces\\tour blanc.gif")
reine_blanc = turtle.Turtle(shape=currentDir + "\\pieces\\reine blanc.gif")
roi_blanc = turtle.Turtle(shape=currentDir + "\\pieces\\roi blanc.gif")


pion_noir_1 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_2 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_3 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_4 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_5 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_6 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_7 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")
pion_noir_8 = turtle.Turtle(shape=currentDir + "\\pieces\\pion noir.gif")

fou_noir_1 = turtle.Turtle(shape=currentDir + "\\pieces\\fou noir.gif")
fou_noir_2 = turtle.Turtle(shape=currentDir + "\\pieces\\fou noir.gif")
cavalier_noir_1 = turtle.Turtle(shape=currentDir + "\\pieces\\cavalier noir.gif")
cavalier_noir_2 = turtle.Turtle(shape=currentDir + "\\pieces\\cavalier noir.gif")
tour_noir_1 = turtle.Turtle(shape=currentDir + "\\pieces\\tour noir.gif")
tour_noir_2 = turtle.Turtle(shape=currentDir + "\\pieces\\tour noir.gif")
reine_noir = turtle.Turtle(shape=currentDir + "\\pieces\\reine noir.gif")
roi_noir = turtle.Turtle(shape=currentDir + "\\pieces\\roi noir.gif")