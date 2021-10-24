from os import path
import turtle
from plateau import wn
from pieces import Pion, Tour, Fou, Reine, Cavalier


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

pion_blanc_1_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_2_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_3_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_4_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_5_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_6_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_7_tortue = turtle.Turtle(shape=chemin_pion_blanc)
pion_blanc_8_tortue = turtle.Turtle(shape=chemin_pion_blanc)

fou_blanc_1_tortue = turtle.Turtle(shape=chemin_fou_blanc)
fou_blanc_2_tortue = turtle.Turtle(shape=chemin_fou_blanc)
cavalier_blanc_1_tortue = turtle.Turtle(shape=chemin_cavalier_blanc)
cavalier_blanc_2_tortue = turtle.Turtle(shape=chemin_cavalier_blanc)
tour_blanc_1_tortue = turtle.Turtle(shape=chemin_tour_blanc)
tour_blanc_2_tortue = turtle.Turtle(shape=chemin_tour_blanc)
reine_blanc_tortue = turtle.Turtle(shape=chemin_reine_blanc)
roi_blanc_tortue = turtle.Turtle(shape=chemin_roi_blanc)


pion_noir_1_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_2_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_3_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_4_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_5_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_6_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_7_tortue = turtle.Turtle(shape=chemin_pion_noir)
pion_noir_8_tortue = turtle.Turtle(shape=chemin_pion_noir)

fou_noir_1_tortue = turtle.Turtle(shape=chemin_fou_noir)
fou_noir_2_tortue = turtle.Turtle(shape=chemin_fou_noir)
cavalier_noir_1_tortue = turtle.Turtle(shape=chemin_cavalier_noir)
cavalier_noir_2_tortue = turtle.Turtle(shape=chemin_cavalier_noir)
tour_noir_1_tortue = turtle.Turtle(shape=chemin_tour_noir)
tour_noir_2_tortue = turtle.Turtle(shape=chemin_tour_noir)
reine_noir_tortue = turtle.Turtle(shape=chemin_reine_noir)
roi_noir_tortue = turtle.Turtle(shape=chemin_roi_noir)


# pions et leur position de départ
pions_positions = {pion_blanc_1_tortue:'a2', pion_blanc_2_tortue:'b2', pion_blanc_3_tortue:'c2', pion_blanc_4_tortue:'d2', pion_blanc_5_tortue:'e2', pion_blanc_6_tortue:'f2', pion_blanc_7_tortue:'g2', pion_blanc_8_tortue:'h2', fou_blanc_1_tortue:'c1', fou_blanc_2_tortue:'f1', cavalier_blanc_1_tortue:'b1', cavalier_blanc_2_tortue:'g1', tour_blanc_1_tortue:'a1', tour_blanc_2_tortue:'h1', reine_blanc_tortue:'d1', roi_blanc_tortue:'e1', pion_noir_1_tortue:'h7', pion_noir_2_tortue:'g7', pion_noir_3_tortue:'f7', pion_noir_4_tortue:'e7', pion_noir_5_tortue:'d7', pion_noir_6_tortue:'c7', pion_noir_7_tortue:'b7', pion_noir_8_tortue:'a7', fou_noir_1_tortue:'f8', fou_noir_2_tortue:'c8', cavalier_noir_1_tortue:'g8', cavalier_noir_2_tortue:'b8', tour_noir_1_tortue:'h8', tour_noir_2_tortue:'a8', reine_noir_tortue:'d8', roi_noir_tortue:'e8'}