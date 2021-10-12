import turtle
import numpy as np
#import pieces


'''CONSTANTES'''
COTE_CASES = 90
DARK_COLOR = '#5c3427'
HEIGHT = 1.0 # taille de l'écran
LIGHT_COLOR = 'beige'
WIDTH = 1.0 # taille de l'écran
X_DEPART = -410
X_FIN = X_DEPART + 6 * COTE_CASES + 1  # je sais pas pourquoi 6 mais ca fait un plateau de longueur  x+2 donc 6 --> 8
Y_DEPART = 270
Y_FIN = Y_DEPART - 8 * COTE_CASES + 1


#Création du "papier" et du "crayon"
wn = turtle.Screen()
wn.tracer(100)

tortue = turtle.Turtle()

#Taille, dimension et couleur pour le papier et le crayon
wn.bgcolor("#27415c")
wn.setup(width = WIDTH, height = HEIGHT)
wn.title("Jeu d'échecs")
tortue.pensize(2)
tortue.shape("turtle")
tortue.color("black")


#Création de l'échiquier
def carree(x, y, c, t, couleur, remplissage):
    '''Dessine un carré.
    Les arguments sont, dans l'ordre : 
    x -> axe x
    y -> axe y
    c -> taille du côté
    t -> tortue utilisée pour dessiner le carré
    couleur -> couleur de remplissage si $remplissage = 0
    remplissage -> sert à faire des alternances pour remplir les carrés (1/2, 1/3, ...)'''
    
    t.color('black')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor('beige')
    if remplissage == 0:
        t.fillcolor(couleur)
    t.begin_fill()
    for _ in range(4):
        t.forward(c)
        t.left(90)
    t.end_fill()
    t.hideturtle()


remplissage = 1

'''MODIFIER LES BOUCLES EN DESSOUS AVEC DES LISTE DE NOMBRES ET DE LETTRES
OU Y = [1,2,3,4,5,6,7,8] ET X = [A,B,C,D,E,F,G,H]
ET UTILISER EXEC POUR SAVOIR QUELLE CASE (X,Y) A QUELLE POSITION (x,y)'''

cases_couleur = {
    'a8':'beige','b8':'#5c3427','c8':'beige','d8':'#5c3427','e8':'beige','f8':'#5c3427','g8':'beige','h8':'#5c3427',
    'a7':'#5c3427','b7':'beige','c7':'#5c3427','d7':'beige','e7':'#5c3427','f7':'beige','g7':'#5c3427','h7':'beige',
    'a6':'beige','b6':'#5c3427','c6':'beige','d6':'#5c3427','e6':'beige','f6':'#5c3427','g6':'beige','h6':'#5c3427',
    'a5':'#5c3427','b5':'beige','c5':'#5c3427','d5':'beige','e5':'#5c3427','f5':'beige','g5':'#5c3427','h5':'beige',
    'a4':'beige','b4':'#5c3427','c4':'beige','d4':'#5c3427','e4':'beige','f4':'#5c3427','g4':'beige','h4':'#5c3427',
    'a3':'#5c3427','b3':'beige','c3':'#5c3427','d3':'beige','e3':'#5c3427','f3':'beige','g3':'#5c3427','h3':'beige',
    'a2':'beige','b2':'#5c3427','c2':'beige','d2':'#5c3427','e2':'beige','f2':'#5c3427','g2':'beige','h2':'#5c3427',
    'a1':'#5c3427','b1':'beige','c1':'#5c3427','d1':'beige','e1':'#5c3427','f1':'beige','g1':'#5c3427','h1':'beige'
}

cases = [
    'a8','b8','c8','d8','e8','f8','g8','h8',
    'a7','b7','c7','d7','e7','f7','g7','h7',
    'a6','b6','c6','d6','e6','f6','g6','h6',
    'a5','b5','c5','d5','e5','f5','g5','h5',
    'a4','b4','c4','d4','e4','f4','g4','h4',
    'a3','b3','c3','d3','e3','f3','g3','h3',
    'a2','b2','c2','d2','e2','f2','g2','h2',
    'a1','b1','c1','d1','e1','f1','g1','h1'
]
count = 1
for y in range(Y_DEPART, Y_FIN, -COTE_CASES):

    
    count -= 1   # indice de la liste $cases
    for x in range(X_DEPART, X_FIN, COTE_CASES * 2):
        carree(x, y, COTE_CASES, tortue, DARK_COLOR, remplissage)   # fait un carree de l'échiquier
        exec("pos_" + cases[count] + " = tortue.pos()")   # crée la variable de nom $pos_cases[count] ayant pour valeur les coordonnées de l'angle bas gauche de la case
        exec("num_" + cases[count] + " = count")   # crée la variable de nom $num_cases[count] ayant pour valeur le numéro de la case
        if count + 2 < 64:
            count += 2  # saute une case
        
    
    count -= 7   # indice de la liste $cases
    for x in range(X_DEPART-90, X_FIN, COTE_CASES * 2):
        carree(x, y, COTE_CASES, tortue, DARK_COLOR, 1 - remplissage)   # fait un carree de l'échiquier
        exec("pos_" + cases[count] + " = tortue.pos()")   # crée la variable de nom $pos_cases[count] ayant pour valeur les coordonnées de l'angle bas gauche de la case
        exec("num_" + cases[count] + " = count")   # crée la variable de nom $num_cases[count] ayant pour valeur le numéro de la case
        if count + 2 < 64:
            count += 2  # saute une case

    remplissage = 1 - remplissage
pos_h1 = (220.00,-360.00) # ca fait pas h1 donc voila
num_h1 = 63

print(locals())


wn.update()
wn.mainloop()


'''
    Chercher comment faire et faire une class Plateau, faire un self.casesOccupees -> list() avec le numéro des cases
'''