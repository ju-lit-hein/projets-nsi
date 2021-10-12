from os import path
import turtle
from plateau import wn


currentDir = path.abspath(path.curdir) #get the python file location

'''ajoute les images des pièces'''
wn.addshape(currentDir + "\\pieces\\cavalier blanc.gif")
wn.addshape(currentDir + "\\pieces\\fou blanc.gif")
wn.addshape(currentDir + "\\pieces\\pion blanc.gif")
wn.addshape(currentDir + "\\pieces\\reine blanc.gif")
wn.addshape(currentDir + "\\pieces\\roi blanc.gif")
wn.addshape(currentDir + "\\pieces\\tour blanc.gif")

wn.addshape(currentDir + "\\pieces\\cavalier noir.gif")
wn.addshape(currentDir + "\\pieces\\fou noir.gif")
wn.addshape(currentDir + "\\pieces\\pion noir.gif")
wn.addshape(currentDir + "\\pieces\\reine noir.gif")
wn.addshape(currentDir + "\\pieces\\roi noir.gif")
wn.addshape(currentDir + "\\pieces\\tour noir.gif")


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


pion_blanc_1.goto((0,0))