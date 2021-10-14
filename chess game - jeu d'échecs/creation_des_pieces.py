from os import path
import turtle
from plateau import wn


currentDir = path.abspath(path.curdir) #get the python file location

# chemin d'accès des fichiers .gif

chemin_pion_blanc = r"%s\\pieces\\pion blanc.gif" % currentDir
chemin_fou_blanc = r"%s\\pieces\\fou blanc.gif" % currentDir
chemin_cavalier_blanc = r"%s\\pieces\\cavalier blanc.gif" % currentDir
chemin_tour_blanc = r"%s\\pieces\\tour blanc.gif" % currentDir
chemin_reine_blanc = r"%s\\pieces\\reine blanc.gif" % currentDir
chemin_roi_blanc = r"%s\\pieces\\roi blanc.gif" % currentDir

chemin_pion_noir = r"%s\\pieces\\pion noir.gif" % currentDir
chemin_fou_noir = r"%s\\pieces\\fou noir.gif" % currentDir
chemin_cavalier_noir = r"%s\\pieces\\cavalier noir.gif" % currentDir
chemin_tour_noir = r"%s\\pieces\\tour noir.gif" % currentDir
chemin_reine_noir = r"%s\\pieces\\reine noir.gif" % currentDir
chemin_roi_noir = r"%s\\pieces\\roi noir.gif" % currentDir

# ajout des shapes des pièces
wn.addshape(chemin_pion_blanc)
wn.addshape(chemin_fou_blanc)
wn.addshape(chemin_cavalier_blanc)
wn.addshape(chemin_tour_blanc)
wn.addshape(chemin_reine_blanc)
wn.addshape(chemin_roi_blanc)

wn.addshape(chemin_pion_noir)
wn.addshape(chemin_fou_noir)
wn.addshape(chemin_cavalier_noir)
wn.addshape(chemin_tour_noir)
wn.addshape(chemin_reine_noir)
wn.addshape(chemin_roi_noir)

# création des tortues des pièces

pion_blanc_1 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_2 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_3 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_4 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_5 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_6 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_7 = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_8 = turtle.Turtle(shape=chemin_pion_blanc)

fou_blanc_1 = turtle.Turtle(shape=chemin_fou_blanc)
fou_blanc_2 = turtle.Turtle(shape=chemin_fou_blanc)
cavalier_blanc_1 = turtle.Turtle(shape=chemin_cavalier_blanc)
cavalier_blanc_2 = turtle.Turtle(shape=chemin_cavalier_blanc)
tour_blanc_1 = turtle.Turtle(shape=chemin_tour_blanc)
tour_blanc_2 = turtle.Turtle(shape=chemin_tour_blanc)
reine_blanc = turtle.Turtle(shape=chemin_reine_blanc)
roi_blanc = turtle.Turtle(shape=chemin_roi_blanc)


pion_noir_1 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_2 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_3 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_4 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_5 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_6 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_7 = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_8 = turtle.Turtle(shape=chemin_pion_noir)

fou_noir_1 = turtle.Turtle(shape=chemin_fou_noir)
fou_noir_2 = turtle.Turtle(shape=chemin_fou_noir)
cavalier_noir_1 = turtle.Turtle(shape=chemin_cavalier_noir)
cavalier_noir_2 = turtle.Turtle(shape=chemin_cavalier_noir)
tour_noir_1 = turtle.Turtle(shape=chemin_tour_noir)
tour_noir_2 = turtle.Turtle(shape=chemin_tour_noir)
reine_noir = turtle.Turtle(shape=chemin_reine_noir)
roi_noir = turtle.Turtle(shape=chemin_roi_noir)


# pions et leur position de départ
pions_positions = {pion_blanc_1:'a2', pion_blanc_2:'b2', pion_blanc_3:'c2', pion_blanc_4:'d2', pion_blanc_5:'e2', pion_blanc_6:'f2', pion_blanc_7:'g2', 
                    pion_blanc_8:'h2', fou_blanc_1:'c1', fou_blanc_2:'f1', cavalier_blanc_1:'b1', cavalier_blanc_2:'g1', tour_blanc_1:'a1', 
                    tour_blanc_2:'h1', reine_blanc:'d1', roi_blanc:'e1', pion_noir_1:'h7', pion_noir_2:'g7', pion_noir_3:'f7', pion_noir_4:'e7', 
                    pion_noir_5:'d7', pion_noir_6:'c7', pion_noir_7:'b7', pion_noir_8:'a7', fou_noir_1:'f8', fou_noir_2:'c8', cavalier_noir_1:'g8', 
                    cavalier_noir_2:'b8', tour_noir_1:'h8', tour_noir_2:'a8', reine_noir:'d8', roi_noir:'e8'}
