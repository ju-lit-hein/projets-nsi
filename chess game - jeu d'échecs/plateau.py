import turtle
from time import sleep


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
# c'est mieux de ne pas changer les constantes de dimensions (bah en fait ca marche plus très bien si on change celles conçernant les dimensions)

# Création du "papier" et du "crayon"
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

plateau_120 =  (
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, 0, 1, 2, 3, 4, 5, 6, 7, -1,
        -1, 8, 9, 10, 11, 12, 13, 14, 15, -1,
        -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
        -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
        -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
        -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
        -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
        -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
 )

plateau_64 = (
        21, 22, 23, 24, 25, 26, 27, 28,
        31, 32, 33, 34, 35, 36, 37, 38,
        41, 42, 43, 44, 45, 46, 47, 48,
        51, 52, 53, 54, 55, 56, 57, 58,
        61, 62, 63, 64, 65, 66, 67, 68,
        71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98
)

def faire_le_plateau():
    cases_buggees = [55, 57, 59, 61, 63]
    '''Les cases buggées ci-dessus sont buggees du fait de la façon dont est réaliser le plateau et de la façon dont les cases sont représentées numériquement.'''
    remplissage = 1
    count = 1
    for y in range(Y_DEPART, Y_FIN, -COTE_CASES):

        
        count -= 1   # indice de la liste $cases
        for x in range(X_DEPART, X_FIN, COTE_CASES * 2):
            carree(x, y, COTE_CASES, tortue, DARK_COLOR, remplissage)   # fait un carree de l'échiquier
            if count not in cases_buggees:
                position = tortue.pos()
                position = tuple(position)
                position = (position[0] + COTE_CASES/2, position[1] + COTE_CASES/2)
                position = turtle.Vec2D(position[0], position[1])
                #print(cases[count], position)
                exec("case_" + cases[count] + " = Case(cases[count], count, position, False, 0, 0)")   # crée la variable de nom $case_** ayant pour valeur la class de la case
            if count + 2 < 64:
                count += 2  # saute une case
            
        
        count -= 7   # indice de la liste $cases
        for x in range(X_DEPART+90, X_FIN, COTE_CASES * 2):
            carree(x, y, COTE_CASES, tortue, DARK_COLOR, 1 - remplissage)   # fait un carree de l'échiquier
            if count not in cases_buggees:
                position = tortue.pos()
                position = tuple(position)
                position = (position[0] + COTE_CASES/2, position[1] + COTE_CASES/2)
                position = turtle.Vec2D(position[0], position[1])
                exec("case_" + cases[count] + " = Case(cases[count], count, position, False, 0, 0)")   # crée la variable de nom $case_** ayant pour valeur la class de la case
            if count + 2 < 64:
                count += 2  # saute une case

        remplissage = 1 - remplissage

    # Création des cases bugées
    
    case_h2 = Case('h2', 55, turtle.Vec2D(265.00, -225.00), False, 0, 0)
    case_b1 = Case('b1', 57, turtle.Vec2D(-275.00, -315.00), False, 0, 0)
    case_d1 = Case('d1', 59, turtle.Vec2D(-95.00, -315.00), False, 0, 0)
    case_f1 = Case('f1', 61, turtle.Vec2D(85.00, -315.00), False, 0, 0)
    case_h1 = Case('h1', 63, turtle.Vec2D(265.00, -315.00), False, 0, 0)
    wn.update()

    import creation
    
    for i in creation.pions_positions:  # i est la tortue de chaque pièce
        j = creation.pions_positions[i] # case où doivent aller les pièces au début de la partie
        i.penup()
        i.goto(eval("case_" + j + ".coordonnees"))
        ########################## Pour tester le cases prises en compte par la boucle -> la case h2 n'est pas prise en compte et une case sur deux bug après
        # carree(eval("case_" + j + ".coordonnees[0]"), eval("case_" + j + ".coordonnees[1]"), 45, tortue, '#ff0000', 0)
        ##############################################################################################################
    if creation.jouer_blanc: # remet en place le pièces buggées
        exec("creation.pion_blanc_8_tortue.goto(265.00, -225.00)")
        exec("creation.cavalier_blanc_1_tortue.goto(-275.00, -315.00)")
        exec("creation.cavalier_blanc_2_tortue.goto(175.00, -315.00)")
        exec("creation.reine_blanc_tortue.goto(-95.00, -315.00)")
        exec("creation.fou_blanc_2_tortue.goto(85.00, -315.00)")
    else:
        exec("creation.pion_noir_8_tortue.goto(265.00, -225.00)")
        exec("creation.cavalier_noir_1_tortue.goto(-275.00, -315.00)")
        exec("creation.cavalier_noir_2_tortue.goto(175.00, -315.00)")
        exec("creation.reine_noir_tortue.goto(-5.00, -315.00)")
        exec("creation.roi_noir_tortue.goto(-95.00, -315.00)")
        exec("creation.fou_noir_2_tortue.goto(85.00, -315.00)")
    # Les 5 et 6 lignes au-dessus sont présentes car le code bug et après des heures (littéralement des heures) on n'a trouver aucune solution car tout est correct 

    for i in creation.pions_positions_str:
        piece = i[:-7]
        case = creation.pions_positions_str[i]
        exec("case_" + case + ".ChangerLeStatutDeLaCase()")
        exec("case_" + case + ".occupeeParQuelCamp = creation." + piece + ".couleur")
        exec("case_" + case + ".occupeeParQuellePiece = creation." + piece)
    # etat = etat_partie()
    # print(etat)
    
    wn.update()
    wn.mainloop()
        
class Case:
    '''class Plateau:   

        Données : 
            - Case (a8)
            - Numéro (0)
            - Coordonnees ( (-365.00,315.00) -> centre de la case)
            - Occupee (True ou False)
            - OccupeeParQuellePiece (class -> nom de la pièce 0 si vide)
            - OccuppeParQuelCamp ('blanc' ou 'noir' 0 si vide)   

        Actions : 
            - ChangerLeStatutDeLaCase()
    '''
    def __init__(self, case, numero, coordonnees, occupee, occupeeParQuellePiece, occupeeParQuelCamp):
        self.case = case
        self.numero = numero
        self.coordonnees = coordonnees
        self.occupee = occupee
        self.occupeeParQuellePiece = occupeeParQuellePiece
        self.occupeeParQuelCamp = occupeeParQuelCamp

    def __str__(self) -> str:
        return f'La case {self.case} | numéro {self.numero} a pour coordonnees {self.coordonnees} | Occupee : {self.occupee} | Piece : {self.occupeeParQuellePiece} | Camp : {self.occupeeParQuelCamp}'

    def ChangerLeStatutDeLaCase(self):
        if self.occupee:
            self.occupee = False
        else:
            self.occupee = True
    
    def ChangerLaPiece(self, piece):    
        self.occupeeParQuellePiece == piece
    
    def ChangerLeCamp(self, couleur=0):
        if couleur == 0:
            if self.occupeeParQuelCamp == 'blanc':
                self.occupeeParQuelCamp == 'noir'
            else:
                self.occupeeParQuelCamp == 'blanc'
        else:
            self.occupeeParQuelCamp == couleur

    def est_occupee(self) -> bool:
        return self.occupee

    def get_camp(self) -> int or str:
        return self.occupeeParQuelCamp

    def get_coordonnees(self) -> tuple:
        return self.coordonnees

    def get_piece(self) -> object: # -> Piece
        return self.occupeeParQuellePiece



 
# def etat_partie() -> dict:
#         etat_de_la_partie = {}
#         for i in cases:
#             etat_de_la_partie["case " + i] = [eval("case_" + i + ".occupee"), eval("case_" + i + ".occupeeParQuellePiece"), eval("case_" + i + ".occupeeParQuelCamp")]
#         return etat_de_la_partie