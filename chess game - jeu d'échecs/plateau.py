import turtle
import numpy as np


'''CONSTANTES'''
COTE_CASES = 90
DARK_COLOR = '#5c3427'
HEIGHT = 1.0 # taille de l'écran
LIGHT_COLOR = 'beige'
WIDTH = 1.0 # taille de l'écran
X_DEPART = -410
X_FIN = X_DEPART + 7 * COTE_CASES + 1 
Y_DEPART = 270
Y_FIN = Y_DEPART - 8 * COTE_CASES + 1
# c'est mieux de ne pas changer les constante

#Création du "papier" et du "crayon"
wn = turtle.Screen()
wn.tracer(100)

tortue = turtle.Turtle()
tortue.hideturtle()

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


class Plateau:      # Nom de class Plateau qui contient plein de petites cases (je trouve ca plus joli que class Case)
    '''
    class Plateau:
        Données : 
            - Case (a8)
            - Numéro (0)
            - Coordonnees ((-410.00,270.00))
            - Occupee (True ou False)
        Actions : 
            - ChangerLeStatutDeLaCase
    '''
    def __init__(self, case, numero, coordonnees, occupee):
        self.case = case
        self.numero = numero
        self.coordonnees = coordonnees
        self.occupee = occupee

    def ChangerLeStatutDeLaCase(self):
        if self.occupee:
            self.occupee = False
        else:
            self.occupee = True



def faire_le_plateau():
    remplissage = 1
    count = 1
    for y in range(Y_DEPART, Y_FIN, -COTE_CASES):

        
        count -= 1   # indice de la liste $cases
        for x in range(X_DEPART, X_FIN, COTE_CASES * 2):
            carree(x, y, COTE_CASES, tortue, DARK_COLOR, remplissage)   # fait un carree de l'échiquier
            exec("case_" + cases[count] + " = Plateau(cases[count], count, tortue.pos(), False)")   # crée la variable de nom $case_** ayant pour valeur la class de la case
            if count + 2 < 64:
                count += 2  # saute une case
            
        
        count -= 7   # indice de la liste $cases
        for x in range(X_DEPART+90, X_FIN, COTE_CASES * 2):
            carree(x, y, COTE_CASES, tortue, DARK_COLOR, 1 - remplissage)   # fait un carree de l'échiquier
            exec("case_" + cases[count] + " = Plateau(cases[count], count, tortue.pos(), False)")   # crée la variable de nom $pos_cases[count] ayant pour valeur les coordonnées de l'angle bas gauche de la case
            if count + 2 < 64:
                count += 2  # saute une case

        remplissage = 1 - remplissage
    case_h1 = Plateau('h1', 63, (220.00, -360.00), False) # ca fait pas h1 donc voila

    wn.update()
    wn.mainloop()


