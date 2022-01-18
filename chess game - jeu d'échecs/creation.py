from os import path
import turtle
from plateau import wn
from pieces import CASES, Pion, Tour, Fou, Reine, Cavalier, Roi


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


jouer_blanc = True
# pions et leur position de départ
if jouer_blanc:
    pions_positions = {pion_blanc_1_tortue:'a2', pion_blanc_2_tortue:'b2', pion_blanc_3_tortue:'c2', pion_blanc_4_tortue:'d2', pion_blanc_5_tortue:'e2', pion_blanc_6_tortue:'f2', pion_blanc_7_tortue:'g2', pion_blanc_8_tortue:'h2', fou_blanc_1_tortue:'c1', fou_blanc_2_tortue:'f1', cavalier_blanc_1_tortue:'b1', cavalier_blanc_2_tortue:'g1', tour_blanc_1_tortue:'a1', tour_blanc_2_tortue:'h1', reine_blanc_tortue:'d1', roi_blanc_tortue:'e1', pion_noir_1_tortue:'h7', pion_noir_2_tortue:'g7', pion_noir_3_tortue:'f7', pion_noir_4_tortue:'e7', pion_noir_5_tortue:'d7', pion_noir_6_tortue:'c7', pion_noir_7_tortue:'b7', pion_noir_8_tortue:'a7', fou_noir_1_tortue:'f8', fou_noir_2_tortue:'c8', cavalier_noir_1_tortue:'g8', cavalier_noir_2_tortue:'b8', tour_noir_1_tortue:'h8', tour_noir_2_tortue:'a8', reine_noir_tortue:'d8', roi_noir_tortue:'e8'}

    pions_positions_str = {'pion_blanc_1_tortue':'a2', 'pion_blanc_2_tortue':'b2', 'pion_blanc_3_tortue':'c2', 'pion_blanc_4_tortue':'d2', 'pion_blanc_5_tortue':'e2', 'pion_blanc_6_tortue':'f2', 'pion_blanc_7_tortue':'g2', 'pion_blanc_8_tortue':'h2', 'fou_blanc_1_tortue':'c1', 'fou_blanc_2_tortue':'f1', 'cavalier_blanc_1_tortue':'b1', 'cavalier_blanc_2_tortue':'g1', 'tour_blanc_1_tortue':'a1', 'tour_blanc_2_tortue':'h1', 'reine_blanc_tortue':'d1', 'roi_blanc_tortue':'e1', 'pion_noir_1_tortue':'h7', 'pion_noir_2_tortue':'g7', 'pion_noir_3_tortue':'f7', 'pion_noir_4_tortue':'e7', 'pion_noir_5_tortue':'d7', 'pion_noir_6_tortue':'c7', 'pion_noir_7_tortue':'b7', 'pion_noir_8_tortue':'a7', 'fou_noir_1_tortue':'f8', 'fou_noir_2_tortue':'c8', 'cavalier_noir_1_tortue':'g8', 'cavalier_noir_2_tortue':'b8', 'tour_noir_1_tortue':'h8', 'tour_noir_2_tortue':'a8', 'reine_noir_tortue':'d8', 'roi_noir_tortue':'e8'}
else:
    pions_positions = {pion_blanc_1_tortue:'h7', pion_blanc_2_tortue:'g7', pion_blanc_3_tortue:'f7', pion_blanc_4_tortue:'e7', pion_blanc_5_tortue:'d7', pion_blanc_6_tortue:'c7', pion_blanc_7_tortue:'b7', pion_blanc_8_tortue:'a7', fou_blanc_1_tortue:'f8', fou_blanc_2_tortue:'c8', cavalier_blanc_1_tortue:'g8', cavalier_blanc_2_tortue:'b8', tour_blanc_1_tortue:'h8', tour_blanc_2_tortue:'a8', reine_blanc_tortue:'e8', roi_blanc_tortue:'d8', pion_noir_1_tortue:'a2', pion_noir_2_tortue:'b2', pion_noir_3_tortue:'c2', pion_noir_4_tortue:'d2', pion_noir_5_tortue:'e2', pion_noir_6_tortue:'f2', pion_noir_7_tortue:'g2', pion_noir_8_tortue:'h2', fou_noir_1_tortue:'c1', fou_noir_2_tortue:'f1', cavalier_noir_1_tortue:'b1', cavalier_noir_2_tortue:'g1', tour_noir_1_tortue:'a1', tour_noir_2_tortue:'h1', reine_noir_tortue:'e1', roi_noir_tortue:'d1'}

    pions_positions_str = {'pion_blanc_1_tortue':'h7', 'pion_blanc_2_tortue':'g7', 'pion_blanc_3_tortue':'f7', 'pion_blanc_4_tortue':'e7', 'pion_blanc_5_tortue':'d7', 'pion_blanc_6_tortue':'c7', 'pion_blanc_7_tortue':'b7', 'pion_blanc_8_tortue':'a7', 'fou_blanc_1_tortue':'f8', 'fou_blanc_2_tortue':'c8', 'cavalier_blanc_1_tortue':'g8', 'cavalier_blanc_2_tortue':'b8', 'tour_blanc_1_tortue':'h8', 'tour_blanc_2_tortue':'a8', 'reine_blanc_tortue':'e8', 'roi_blanc_tortue':'d8', 'pion_noir_1_tortue':'a2', 'pion_noir_2_tortue':'b2', 'pion_noir_3_tortue':'c2', 'pion_noir_4_tortue':'d2', 'pion_noir_5_tortue':'e2', 'pion_noir_6_tortue':'f2', 'pion_noir_7_tortue':'g2', 'pion_noir_8_tortue':'h2', 'fou_noir_1_tortue':'c1', 'fou_noir_2_tortue':'f1', 'cavalier_noir_1_tortue':'b1', 'cavalier_noir_2_tortue':'g1', 'tour_noir_1_tortue':'a1', 'tour_noir_2_tortue':'h1', 'reine_noir_tortue':'e1', 'roi_noir_tortue':'d1'}


### Pieces


### regarder comment fonctionne le '.index(...)' pq sah j'ai oublié
pion_blanc_1 = Pion(CASES.index(pions_positions[pion_blanc_1_tortue]), 'blanc', jouer_blanc, pion_blanc_1_tortue)
pion_blanc_2 = Pion(CASES.index(pions_positions[pion_blanc_2_tortue]), 'blanc', jouer_blanc, pion_blanc_2_tortue)
pion_blanc_3 = Pion(CASES.index(pions_positions[pion_blanc_3_tortue]), 'blanc', jouer_blanc, pion_blanc_3_tortue)
pion_blanc_4 = Pion(CASES.index(pions_positions[pion_blanc_4_tortue]), 'blanc', jouer_blanc, pion_blanc_4_tortue)
pion_blanc_5 = Pion(CASES.index(pions_positions[pion_blanc_5_tortue]), 'blanc', jouer_blanc, pion_blanc_5_tortue)
pion_blanc_6 = Pion(CASES.index(pions_positions[pion_blanc_6_tortue]), 'blanc', jouer_blanc, pion_blanc_6_tortue)
pion_blanc_7 = Pion(CASES.index(pions_positions[pion_blanc_7_tortue]), 'blanc', jouer_blanc, pion_blanc_7_tortue)
pion_blanc_8 = Pion(CASES.index(pions_positions[pion_blanc_8_tortue]), 'blanc', jouer_blanc, pion_blanc_8_tortue)

fou_blanc_1 = Fou(CASES.index(pions_positions[fou_blanc_1_tortue]), 'blanc', fou_blanc_1_tortue)
fou_blanc_2 = Fou(CASES.index(pions_positions[fou_blanc_2_tortue]), 'blanc', fou_blanc_2_tortue)
cavalier_blanc_1 = Cavalier(CASES.index(pions_positions[cavalier_blanc_1_tortue]), 'blanc', cavalier_blanc_1_tortue)
cavalier_blanc_2 = Cavalier(CASES.index(pions_positions[cavalier_blanc_2_tortue]), 'blanc', cavalier_blanc_2_tortue)
tour_blanc_1 = Tour(CASES.index(pions_positions[tour_blanc_1_tortue]), 'blanc', tour_blanc_1_tortue)
tour_blanc_2 = Tour(CASES.index(pions_positions[tour_blanc_2_tortue]), 'blanc', tour_blanc_2_tortue)
reine_blanc = Reine(CASES.index(pions_positions[reine_blanc_tortue]), 'blanc', reine_blanc_tortue)
roi_blanc = Roi(CASES.index(pions_positions[roi_blanc_tortue]), 'blanc', roi_blanc_tortue)


pion_noir_1 = Pion(CASES.index(pions_positions[pion_noir_1_tortue]), 'noir', not(jouer_blanc), pion_noir_1_tortue)
pion_noir_2 = Pion(CASES.index(pions_positions[pion_noir_2_tortue]), 'noir', not(jouer_blanc), pion_noir_2_tortue)
pion_noir_3 = Pion(CASES.index(pions_positions[pion_noir_3_tortue]), 'noir', not(jouer_blanc), pion_noir_3_tortue)
pion_noir_4 = Pion(CASES.index(pions_positions[pion_noir_4_tortue]), 'noir', not(jouer_blanc), pion_noir_4_tortue)
pion_noir_5 = Pion(CASES.index(pions_positions[pion_noir_5_tortue]), 'noir', not(jouer_blanc), pion_noir_5_tortue)
pion_noir_6 = Pion(CASES.index(pions_positions[pion_noir_6_tortue]), 'noir', not(jouer_blanc), pion_noir_6_tortue)
pion_noir_7 = Pion(CASES.index(pions_positions[pion_noir_7_tortue]), 'noir', not(jouer_blanc), pion_noir_7_tortue)
pion_noir_8 = Pion(CASES.index(pions_positions[pion_noir_8_tortue]), 'noir', not(jouer_blanc), pion_noir_8_tortue)

fou_noir_1 = Fou(CASES.index(pions_positions[fou_noir_1_tortue]), 'noir', fou_noir_1_tortue)
fou_noir_2 = Fou(CASES.index(pions_positions[fou_noir_2_tortue]), 'noir', fou_noir_2_tortue)
cavalier_noir_1 = Cavalier(CASES.index(pions_positions[cavalier_noir_1_tortue]), 'noir', cavalier_noir_1_tortue)
cavalier_noir_2 = Cavalier(CASES.index(pions_positions[cavalier_noir_2_tortue]), 'noir', cavalier_noir_2_tortue)
tour_noir_1 = Tour(CASES.index(pions_positions[tour_noir_1_tortue]), 'noir', tour_noir_1_tortue)
tour_noir_2 = Tour(CASES.index(pions_positions[tour_noir_2_tortue]), 'noir', tour_noir_2_tortue)
reine_noir = Reine(CASES.index(pions_positions[reine_noir_tortue]), 'noir', reine_noir_tortue)
roi_noir = Roi(CASES.index(pions_positions[roi_noir_tortue]), 'noir', roi_noir_tortue)

# tout = [pion_blanc_1, pion_blanc_2, pion_blanc_3, pion_blanc_4, pion_blanc_5, pion_blanc_6, pion_blanc_7, pion_blanc_8, fou_blanc_1, fou_blanc_2, cavalier_blanc_1, cavalier_blanc_2, tour_blanc_1, tour_blanc_2, reine_blanc, roi_blanc, pion_noir_1, pion_noir_2, pion_noir_3, pion_noir_4, pion_noir_5, pion_noir_6, pion_noir_7, pion_noir_8, fou_noir_1, fou_noir_2, cavalier_noir_1, cavalier_noir_2, tour_noir_1, tour_noir_2, reine_noir, roi_noir]

### Cases du plateau

# case_a8 = Plateau('a8', 0, (), False, 0, 0)
# case_b8 = Plateau('b8', 1, (), False, 0, 0)
# case_c8 = Plateau('c8', 2, (), False, 0, 0)
# case_d8 = Plateau('d8', 3, (), False, 0, 0)
# case_e8 = Plateau('e8', 4, (), False, 0, 0)
# case_f8 = Plateau('f8', 5, (), False, 0, 0)
# case_g8 = Plateau('g8', 6, (), False, 0, 0)
# case_h8 = Plateau('h8', 7, (), False, 0, 0)
# case_a7 = Plateau('a7', 8, (), False, 0, 0)
# case_b7 = Plateau('b7', 9, (), False, 0, 0)
# case_c7 = Plateau('c7', 10, (), False, 0, 0)
# case_d7 = Plateau('d7', 11, (), False, 0, 0)
# case_e7 = Plateau('e7', 12, (), False, 0, 0)
# case_f7 = Plateau('f7', 13, (), False, 0, 0)
# case_g7 = Plateau('g7', 14, (), False, 0, 0)
# case_h7 = Plateau('h7', 15, (), False, 0, 0)
# case_a6 = Plateau('a6', 16, (), False, 0, 0)
# case_b6 = Plateau('b6', 17, (), False, 0, 0)
# case_c6 = Plateau('c6', 18, (), False, 0, 0)
# case_d6 = Plateau('d6', 19, (), False, 0, 0)
# case_e6 = Plateau('e6', 20, (), False, 0, 0)
# case_f6 = Plateau('f6', 21, (), False, 0, 0)
# case_g6 = Plateau('g6', 22, (), False, 0, 0)
# case_h6 = Plateau('h6', 23, (), False, 0, 0)
# case_a5 = Plateau('a5', 24, (), False, 0, 0)
# case_b5 = Plateau('b5', 25, (), False, 0, 0)
# case_c5 = Plateau('c5', 26, (), False, 0, 0)
# case_d5 = Plateau('d5', 27, (), False, 0, 0)
# case_e5 = Plateau('e5', 28, (), False, 0, 0)
# case_f5 = Plateau('f5', 29, (), False, 0, 0)
# case_g5 = Plateau('g5', 30, (), False, 0, 0)
# case_h5 = Plateau('h5', 31, (), False, 0, 0)
# case_a4 = Plateau('a4', 32, (), False, 0, 0)
# case_b4 = Plateau('b4', 33, (), False, 0, 0)
# case_c4 = Plateau('c4', 34, (), False, 0, 0)
# case_d4 = Plateau('d4', 35, (), False, 0, 0)
# case_e4 = Plateau('e4', 36, (), False, 0, 0)
# case_f4 = Plateau('f4', 37, (), False, 0, 0)
# case_g4 = Plateau('g4', 38, (), False, 0, 0)
# case_h4 = Plateau('h4', 39, (), False, 0, 0)
# case_a3 = Plateau('a3', 40, (), False, 0, 0)
# case_b3 = Plateau('b3', 41, (), False, 0, 0)
# case_c3 = Plateau('c3', 42, (), False, 0, 0)
# case_d3 = Plateau('d3', 43, (), False, 0, 0)
# case_e3 = Plateau('e3', 44, (), False, 0, 0)
# case_f3 = Plateau('f3', 45, (), False, 0, 0)
# case_g3 = Plateau('g3', 46, (), False, 0, 0)
# case_h3 = Plateau('h3', 47, (), False, 0, 0)
# case_a2 = Plateau('a2', 48, (), False, 0, 0)
# case_b2 = Plateau('b2', 49, (), False, 0, 0)
# case_c2 = Plateau('c2', 50, (), False, 0, 0)
# case_d2 = Plateau('d2', 51, (), False, 0, 0)
# case_e2 = Plateau('e2', 52, (), False, 0, 0)
# case_f2 = Plateau('f2', 53, (), False, 0, 0)
# case_g2 = Plateau('g2', 54, (), False, 0, 0)
# case_h2 = Plateau('h2', 55, (), False, 0, 0)
# case_a1 = Plateau('a1', 56, (), False, 0, 0)
# case_b1 = Plateau('b1', 57, (), False, 0, 0)
# case_c1 = Plateau('c1', 58, (), False, 0, 0)
# case_d1 = Plateau('d1', 59, (), False, 0, 0)
# case_e1 = Plateau('e1', 60, (), False, 0, 0)
# case_f1 = Plateau('f1', 61, (), False, 0, 0)
# case_g1 = Plateau('g1', 62, (), False, 0, 0)
# case_h1 = Plateau('h1', 63, (), False, 0, 0)