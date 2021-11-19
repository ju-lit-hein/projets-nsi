from time import sleep
import turtle
from os import path

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
# c'est mieux de ne pas changer les constantes (bah en fait ca marche pas si on change)

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

        
class Plateau:      # Nom de class Plateau qui contient plein de petites cases (je trouve ca plus joli que class Case)
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

    def ChangerLeStatutDeLaCase(self):
        if self.occupee:
            self.occupee = False
        else:
            self.occupee = True

 
# def etat_partie() -> dict:
#         etat_de_la_partie = {}
#         for i in cases:
#             etat_de_la_partie["case " + i] = [eval("case_" + i + ".occupee"), eval("case_" + i + ".occupeeParQuellePiece"), eval("case_" + i + ".occupeeParQuelCamp")]
#         return etat_de_la_partie

def faire_le_plateau():
    remplissage = 1
    count = 1
    for y in range(Y_DEPART, Y_FIN, -COTE_CASES):

        
        count -= 1   # indice de la liste $cases
        for x in range(X_DEPART, X_FIN, COTE_CASES * 2):
            carree(x, y, COTE_CASES, tortue, DARK_COLOR, remplissage)   # fait un carree de l'échiquier
            position = tortue.pos()
            position = tuple(position)
            position = (position[0] + COTE_CASES/2, position[1] + COTE_CASES/2)
            position = turtle.Vec2D(position[0], position[1])
            #print(cases[count], position)
            exec("case_" + cases[count] + " = Plateau(cases[count], count, position, False, 0, 0)")   # crée la variable de nom $case_** ayant pour valeur la class de la case
            if count + 2 < 64:
                count += 2  # saute une case
            
        
        count -= 7   # indice de la liste $cases
        for x in range(X_DEPART+90, X_FIN, COTE_CASES * 2):
            carree(x, y, COTE_CASES, tortue, DARK_COLOR, 1 - remplissage)   # fait un carree de l'échiquier
            position = tortue.pos()
            position = tuple(position)
            position = (position[0] + COTE_CASES/2, position[1] + COTE_CASES/2)
            position = turtle.Vec2D(position[0], position[1])
            exec("case_" + cases[count] + " = Plateau(cases[count], count, position, False, 0, 0)")   # crée la variable de nom $case_** ayant pour valeur la class de la case
            if count + 2 < 64:
                count += 2  # saute une case

        remplissage = 1 - remplissage

    case_h1 = Plateau('h1', 63, turtle.Vec2D(265.00, -315.00), False, 0, 0) # ca fait pas h1 donc voila
    wn.update()

    
    INFORMATIONS = '''Pour obtenir :
    - lettre et numéro d'une case (par exemple a1) : cases[caseActuelle]
    - numéro de la case actuelle (par exemple 21) : Piece.caseActuelle
    - coordonées Turtle d'une case par exemple (265.00, -135.00) : pour la case 'h3' -> case_h3.coordonnees 

    Pour chaque pièces, (on va prendre pour exemple le fou) mouvement_fou[-1] est un booléens.
    S'il est Vrai les mouvement de la pièce peuvent se répéter :
        fou en 36 peut aller en : 
        - 36 - 11 = 25
        - mais aussi en 25 - 11 = 14 et ainsi de suite et pour toutes les directions
    '''

    marquage = turtle.Turtle()
    marquage.pencolor('cyan')
    marquage.pensize(1)
    marquage.hideturtle()



    CASES = [
        'a8','b8','c8','d8','e8','f8','g8','h8',
        'a7','b7','c7','d7','e7','f7','g7','h7',
        'a6','b6','c6','d6','e6','f6','g6','h6',
        'a5','b5','c5','d5','e5','f5','g5','h5',
        'a4','b4','c4','d4','e4','f4','g4','h4',
        'a3','b3','c3','d3','e3','f3','g3','h3',
        'a2','b2','c2','d2','e2','f2','g2','h2',
        'a1','b1','c1','d1','e1','f1','g1','h1']

    def MontrerDeplacementsPossibles(self, DDP):
        '''DDP -> dico {nom de la case à marquer : True -> Piece à manger ; False -> deplacement simple'''
        if len(DDP) < 0:
            for i in DDP:
                coordonnees = eval("case_" + i + ".coordonnees")
                if DDP[i]:                                                                              # si la clé (la case) a pour valeur True
                    carree(coordonnees[0] - 5, coordonnees[1] - 5 , 10, marquage, '#b32727', 0)
                else:
                    carree(coordonnees[0] - 5, coordonnees[1] - 5, 10, marquage, '#2f43ba', 0)        


    def mangerUnePiece(piece, case, piece_mangee) -> None:
        '''Deplace la pièce voulue vers une case et mange la pièce sur la case :    
        - piece -> class nom de la pièce qui est déplacée
        - case -> str nom de la case (f4)
        - piece_mangee -> class nom de la piece mangee
        '''
        caseActuelle = CASES[piece.caseActuelle]
        exec("case_" + caseActuelle + ".occupee = False")
        coordonnees = eval("case_" + case + ".cordonnees")
        piece.goto(coordonnees)
        exec("case_" + case + ".occupee = True")
        exec("case_" + case + ".occupeeParQuelCamp = " + piece + ".couleur")
        piece_mangee.hideturtle()
        piece_mangee.goto(-750,0)


    def deplacerUnePiece(case_depart, case_arrivee) -> None:
        '''Deplace la pièce voulue vers une case :  
        - case_depart -> str case de départ de la pièce qui va être déplacée ("b4")
        - case_arrivee -> str nom de la case d'arrivée de la pièce qui va être déplacée("a5")
        '''
        piece = eval("case_" + case_depart + ".OccupeeParQuellePiece")                                          # class -> piece qui va être déplacée
        if eval("case_" + case_arrivee + ".occupee"):                                                           # si la case d'arrivée est ocuppée
            mangerUnePiece(piece, case_arrivee, eval("case_" + case_arrivee + ".occupeeParQuellePiece"))
            return 0
        coordonnees = eval("case_" + case_arrivee + ".cordonnees")                                              # récupère les coordoonées de la case d'arrivée
        piece.goto(coordonnees)
        exec("case_" + case_depart + ".occupee = False")                                                        # rend la case de départ inoccupée
        exec("case_" + case_arrivee + ".occupee = True")                                                        # rend la case d'arrivée occupée
        exec("case_" + case_arrivee + ".occupeeParQuellePiece = piece")
        exec("case_" + case_arrivee + ".occupeeParQuelCamp = " + piece + ".couleur")
        


    '''Définition'''
    pieces = ('cavalier','fou','pion','reine','roi','tour')
    valeur_pieces = (3,3,1,9,0,5,0)
    mouvement_cavalier = (-12,-21,-19,-8,12,21,19,8)
    mouvement_fou = (-11,-9,11,9)
    mouvement_tour = (-10,10,-1,1)
    mouvement_reine = (-11,-10,-9,-1,11,10,9,1)
    mouvement_roi = (-11,-10,-9,-1,11,10,9,1)



    class Pion:
        '''class Pion   

            Données :
                - CaseActuelle -> int numéro de la case sur laquelle est le pion
                - Couleur -> str 'noir' ou 'blanc'
                - dejaBouge -> bool si le pion a déjà bougé (True) ou pas (False)
                - DéplacementPossibles -> tuple contenant des int
                - Sens -> bool True si le pion avance vers la haut du plateau et False si il avance vers le bas
                - Tortue -> turtle.Turtle Object -> tortue qui représente le pion   

            Actions : 
                - MouvementsPossibles() -> dict
        '''
        def __init__(self, caseActuelle, couleur, sens, tortue, dejaBouge = False) -> None:
            self.caseActuelle = caseActuelle                    # int -> numéro de la case sur laquelle le pion est
            self.couleur = couleur                              # str -> camp de la pièce
            self.dejaBouge = dejaBouge                          # bool -> vérifie si le pion a déjà bougé
            self.sens = sens                                    # bool -> voir définition de a class
            if self.sens:                                  # si le pion est orinté vers le haut
                self.deplacementsPossibles = (-16,-8,-9,-7)     # tuple -> déplacements possibles de la pièce
            else:                                               # si le pion est orienté vers le bas
                self.deplacementsPossibles = (16,8,9,7)         # tuple -> déplacements possibles de la pièce
            self.tortue = tortue                                # turtle.Turtle Object -> tortue qui a l'image du pion


        def MouvementsPossibles(self) -> dict:
            '''Retourne le numéro de toutes les cases où le pion peut se déplacer sous forme de dictionnaire'''
            dico_deplacements_possibles = {}
            point_de_depart = self.caseActuelle
            
            if self.dejaBouge == False:                                             # si le pion n'a pas encore bougé et peut donc avancer de deux cases d'un coup
                case_0 = CASES[self.caseActuelle + self.deplacementsPossibles[0]]   # case où le pion à le droit d'aller
                case_1 = CASES[self.caseActuelle + self.deplacementsPossibles[1]]   # case où le pion à le droit d'aller

                if not(eval("case_" + case_0 + ".occupee")):                        # si la case est libre
                    dico_deplacements_possibles[case_0] = False                     # case où le pion peut aller

                if not(eval("case_" + case_1 + ".occupee")):                        # si la case est libre
                    dico_deplacements_possibles[case_1] = False                     # case où le pion peut aller

            else:
                case_0 = CASES[self.caseActuelle + self.deplacementsPossibles[1]]   # case où le pion à le droit d'aller
                if not(eval("case_" + case_0 + ".occupee")) and self.caseActuelle + self.deplacementsPossibles[1] <= 0:                        # si la case est libre
                    dico_deplacements_possibles[case_0] = False                     # case où le pion peut aller
            if self.caseActuelle + self.deplacementsPossibles[2] <= 0 or self.caseActuelle + self.deplacementsPossibles[3] <= 0:
                for i in self.deplacementsPossibles[2:]:
                    case = CASES[self.caseActuelle + i]                                 # cases où le pion à le droit d'aller pour manger une autre pièce
                    if eval("case_" + case + ".occupee"):                               # si il y a une pièce a manger
                        if eval("case_" + case + ".occupeeParQuelCamp") != self.couleur and eval("case_" + case + ".occupeeParQuelCamp") != 0:
                            dico_deplacements_possibles[case] = True
            return dico_deplacements_possibles

        
    class Cavalier:
        '''class Cavalier     

            Données :     
                - CaseActuelle -> int numéro de la case sur laquelle est le pion
                - Couleur -> str 'noir' ou 'blanc'
                - DéplacementPossibles -> tuple contenant des int
                - Tortue -> turtle.Turtle Object -> tortue qui représente le pion   

            Actions :            
                - MouvementsPossibles() -> dict
        '''
        def __init__(self, caseActuelle, couleur, tortue) -> None:
            self.caseActuelle = caseActuelle
            self.couleur = couleur
            self.deplacementsPossibles = (-12, -21, -19, -8, 12, 21, 19, 8)
            self.tortue = tortue

        def MouvementsPossibles(self) -> dict:
            '''Retourne le numéro de toutes les cases où le cavalier peut se déplacer sous forme de dictionnaire'''
            dico_deplacements_possibles = {}
            for i in self.deplacementsPossibles:
                if plateau_120[plateau_64[self.caseActuelle] + i] != -1:                                                                              # si la pièce ne sort pas du plateau
                    if eval("case_" + CASES[self.caseActuelle + i] + ".occupeeParQuelCamp") != self.couleur:                                # si la case, n'est pas occupée par un pièce du même camp
                        dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
            return dico_deplacements_possibles


    class Fou:
        '''class Fou     

            Données :     
                - CaseActuelle -> int numéro de la case sur laquelle est le pion
                - Couleur -> str 'noir' ou 'blanc'
                - DéplacementPossibles -> tuple contenant des int
                - Tortue -> turtle.Turtle Object -> tortue qui représente le pion    

            Actions :    
                - MouvementsPossibles() -> dict
        '''
        def __init__(self, caseActuelle, couleur, tortue) -> None:
            self.caseActuelle = caseActuelle
            self.couleur = couleur
            self.deplacementsPossibles = (-9,-7, 7, 9)
            self.tortue = tortue
        

        def MouvementsPossibles(self) -> dict:
            dico_deplacements_possibles = {}
            for i in self.deplacementsPossibles:
                while plateau_120[plateau_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
                    if eval("case_" + CASES[self.caseActuelle] + ".occupeeParQuelCamp") != self.couleur:                                    # si la case, n'est pas occupée par un pièce du même camp
                        dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
            return dico_deplacements_possibles


    class Tour:
        '''class Tour     

            Données :     
                - CaseActuelle -> int numéro de la case sur laquelle est le pion
                - Couleur -> str 'noir' ou 'blanc'
                - DéplacementPossibles -> tuple contenant des int
                - Tortue -> turtle.Turtle Object -> tortue qui représente le pion    

            Actions :    
                - MouvementsPossibles() -> dict
        '''
        def __init__(self, caseActuelle, couleur, tortue) -> None:
            self.caseActuelle = caseActuelle
            self.couleur = couleur
            self.deplacementsPossibles = (-8, -1, 1, 8)
            self.tortue = tortue

        def MouvementsPossibles(self) -> dict:
            dico_deplacements_possibles = {}
            for i in self.deplacementsPossibles:
                while plateau_120[plateau_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
                    if eval("case_" + CASES[self.caseActuelle] + ".occupeeParQuelCamp") != self.couleur:                                    # si la case, n'est pas occupée par un pièce du même camp
                        dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
            return dico_deplacements_possibles


    class Reine:
        '''class Reine     

            Données :     
                - CaseActuelle -> int numéro de la case sur laquelle est le pion
                - Couleur -> str 'noir' ou 'blanc'
                - DéplacementPossibles -> tuple contenant des int
                - Tortue -> turtle.Turtle Object -> tortue qui représente le pion    

            Actions :    
                - MouvementsPossibles() -> dict
        '''
        def __init__(self, caseActuelle, couleur, tortue) -> None:
            self.caseActuelle = caseActuelle
            self.couleur = couleur
            self.deplacementsPossibles = (-9, -8, -7, -1, 1, 7, 8, 9)
            self.tortue = tortue

        def MouvementsPossibles(self) -> dict:
            dico_deplacements_possibles = {}
            for i in self.deplacementsPossibles:
                while plateau_120[plateau_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
                    if eval("case_" + CASES[self.caseActuelle + i] + ".occupeeParQuelCamp") != self.couleur:                                    # si la case, n'est pas occupée par un pièce du même camp
                        dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
            return dico_deplacements_possibles

    class Roi:
        '''class Roi     

            Données :     
                - CaseActuelle -> int numéro de la case sur laquelle est le pion
                - Couleur -> str 'noir' ou 'blanc'
                - DéplacementPossibles -> tuple contenant des int
                - Tortue -> turtle.Turtle Object -> tortue qui représente le pion    

            Actions :    
                - MouvementsPossibles() -> dict
        '''
        def __init__(self, caseActuelle, couleur, tortue, dejaBouge = False, dejaEchec = False) -> None:
            self.caseActuelle = caseActuelle
            self.couleur = couleur
            self.dejaBouge = dejaBouge
            self.dejaEchec = dejaEchec
            self.deplacementspossibles = (-9, -8, -7, -1, 1, 7, 8, 9)
            self.tortue = tortue
        
        def MouvementsPossibles(self) -> dict:
            dico_deplacements_possibles = {}
            for i in self.deplacementspossibles:
                if eval("case_" + CASES[self.caseActuelle + i] + ".occupeeParQuelCamp") != self.couleur:                                    # si la case, n'est pas occupée par un pièce du même camp
                    dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
            return dico_deplacements_possibles



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


    sens = False
    # pions et leur position de départ
    if sens:
        pions_positions = {pion_blanc_1_tortue:'a2', pion_blanc_2_tortue:'b2', pion_blanc_3_tortue:'c2', pion_blanc_4_tortue:'d2', pion_blanc_5_tortue:'e2', pion_blanc_6_tortue:'f2', pion_blanc_7_tortue:'g2', pion_blanc_8_tortue:'h2', fou_blanc_1_tortue:'c1', fou_blanc_2_tortue:'f1', cavalier_blanc_1_tortue:'b1', cavalier_blanc_2_tortue:'g1', tour_blanc_1_tortue:'a1', tour_blanc_2_tortue:'h1', reine_blanc_tortue:'d1', roi_blanc_tortue:'e1', pion_noir_1_tortue:'h7', pion_noir_2_tortue:'g7', pion_noir_3_tortue:'f7', pion_noir_4_tortue:'e7', pion_noir_5_tortue:'d7', pion_noir_6_tortue:'c7', pion_noir_7_tortue:'b7', pion_noir_8_tortue:'a7', fou_noir_1_tortue:'f8', fou_noir_2_tortue:'c8', cavalier_noir_1_tortue:'g8', cavalier_noir_2_tortue:'b8', tour_noir_1_tortue:'h8', tour_noir_2_tortue:'a8', reine_noir_tortue:'d8', roi_noir_tortue:'e8'}

        pions_positions_str = {'pion_blanc_1_tortue':'a2', 'pion_blanc_2_tortue':'b2', 'pion_blanc_3_tortue':'c2', 'pion_blanc_4_tortue':'d2', 'pion_blanc_5_tortue':'e2', 'pion_blanc_6_tortue':'f2', 'pion_blanc_7_tortue':'g2', 'pion_blanc_8_tortue':'h2', 'fou_blanc_1_tortue':'c1', 'fou_blanc_2_tortue':'f1', 'cavalier_blanc_1_tortue':'b1', 'cavalier_blanc_2_tortue':'g1', 'tour_blanc_1_tortue':'a1', 'tour_blanc_2_tortue':'h1', 'reine_blanc_tortue':'d1', 'roi_blanc_tortue':'e1', 'pion_noir_1_tortue':'h7', 'pion_noir_2_tortue':'g7', 'pion_noir_3_tortue':'f7', 'pion_noir_4_tortue':'e7', 'pion_noir_5_tortue':'d7', 'pion_noir_6_tortue':'c7', 'pion_noir_7_tortue':'b7', 'pion_noir_8_tortue':'a7', 'fou_noir_1_tortue':'f8', 'fou_noir_2_tortue':'c8', 'cavalier_noir_1_tortue':'g8', 'cavalier_noir_2_tortue':'b8', 'tour_noir_1_tortue':'h8', 'tour_noir_2_tortue':'a8', 'reine_noir_tortue':'d8', 'roi_noir_tortue':'e8'}
    else:
        pions_positions = {pion_blanc_1_tortue:'h7', pion_blanc_2_tortue:'g7', pion_blanc_3_tortue:'f7', pion_blanc_4_tortue:'e7', pion_blanc_5_tortue:'d7', pion_blanc_6_tortue:'c7', pion_blanc_7_tortue:'b7', pion_blanc_8_tortue:'a7', fou_blanc_1_tortue:'f8', fou_blanc_2_tortue:'c8', cavalier_blanc_1_tortue:'g8', cavalier_blanc_2_tortue:'b8', tour_blanc_1_tortue:'h8', tour_blanc_2_tortue:'a8', reine_blanc_tortue:'e8', roi_blanc_tortue:'d8', pion_noir_1_tortue:'a2', pion_noir_2_tortue:'b2', pion_noir_3_tortue:'c2', pion_noir_4_tortue:'d2', pion_noir_5_tortue:'e2', pion_noir_6_tortue:'f2', pion_noir_7_tortue:'g2', pion_noir_8_tortue:'h2', fou_noir_1_tortue:'c1', fou_noir_2_tortue:'f1', cavalier_noir_1_tortue:'b1', cavalier_noir_2_tortue:'g1', tour_noir_1_tortue:'a1', tour_noir_2_tortue:'h1', reine_noir_tortue:'e1', roi_noir_tortue:'d1'}

        pions_positions_str = {'pion_blanc_1_tortue':'h7', 'pion_blanc_2_tortue':'g7', 'pion_blanc_3_tortue':'f7', 'pion_blanc_4_tortue':'e7', 'pion_blanc_5_tortue':'d7', 'pion_blanc_6_tortue':'c7', 'pion_blanc_7_tortue':'b7', 'pion_blanc_8_tortue':'a7', 'fou_blanc_1_tortue':'f8', 'fou_blanc_2_tortue':'c8', 'cavalier_blanc_1_tortue':'g8', 'cavalier_blanc_2_tortue':'b8', 'tour_blanc_1_tortue':'h8', 'tour_blanc_2_tortue':'a8', 'reine_blanc_tortue':'e8', 'roi_blanc_tortue':'d8', 'pion_noir_1_tortue':'a2', 'pion_noir_2_tortue':'b2', 'pion_noir_3_tortue':'c2', 'pion_noir_4_tortue':'d2', 'pion_noir_5_tortue':'e2', 'pion_noir_6_tortue':'f2', 'pion_noir_7_tortue':'g2', 'pion_noir_8_tortue':'h2', 'fou_noir_1_tortue':'c1', 'fou_noir_2_tortue':'f1', 'cavalier_noir_1_tortue':'b1', 'cavalier_noir_2_tortue':'g1', 'tour_noir_1_tortue':'a1', 'tour_noir_2_tortue':'h1', 'reine_noir_tortue':'e1', 'roi_noir_tortue':'d1'}




    pion_blanc_1 = Pion(CASES.index(pions_positions[pion_blanc_1_tortue]), 'blanc', sens, pion_blanc_1_tortue)
    pion_blanc_2 = Pion(CASES.index(pions_positions[pion_blanc_2_tortue]), 'blanc', sens, pion_blanc_2_tortue)
    pion_blanc_3 = Pion(CASES.index(pions_positions[pion_blanc_3_tortue]), 'blanc', sens, pion_blanc_3_tortue)
    pion_blanc_4 = Pion(CASES.index(pions_positions[pion_blanc_4_tortue]), 'blanc', sens, pion_blanc_4_tortue)
    pion_blanc_5 = Pion(CASES.index(pions_positions[pion_blanc_5_tortue]), 'blanc', sens, pion_blanc_5_tortue)
    pion_blanc_6 = Pion(CASES.index(pions_positions[pion_blanc_6_tortue]), 'blanc', sens, pion_blanc_6_tortue)
    pion_blanc_7 = Pion(CASES.index(pions_positions[pion_blanc_7_tortue]), 'blanc', sens, pion_blanc_7_tortue)
    pion_blanc_8 = Pion(CASES.index(pions_positions[pion_blanc_8_tortue]), 'blanc', sens, pion_blanc_8_tortue)

    fou_blanc_1 = Fou(CASES.index(pions_positions[fou_blanc_1_tortue]), 'blanc', fou_blanc_1_tortue)
    fou_blanc_2 = Fou(CASES.index(pions_positions[fou_blanc_2_tortue]), 'blanc', fou_blanc_2_tortue)
    cavalier_blanc_1 = Cavalier(CASES.index(pions_positions[cavalier_blanc_1_tortue]), 'blanc', cavalier_blanc_1_tortue)
    cavalier_blanc_2 = Cavalier(CASES.index(pions_positions[cavalier_blanc_2_tortue]), 'blanc', cavalier_blanc_2_tortue)
    tour_blanc_1 = Tour(CASES.index(pions_positions[tour_blanc_1_tortue]), 'blanc', tour_blanc_1_tortue)
    tour_blanc_2 = Tour(CASES.index(pions_positions[tour_blanc_2_tortue]), 'blanc', tour_blanc_2_tortue)
    reine_blanc = Reine(CASES.index(pions_positions[reine_blanc_tortue]), 'blanc', reine_blanc_tortue)
    roi_blanc = Roi(CASES.index(pions_positions[roi_blanc_tortue]), 'blanc', roi_blanc_tortue)


    pion_noir_1 = Pion(CASES.index(pions_positions[pion_noir_1_tortue]), 'noir', not(sens), pion_noir_1_tortue)
    pion_noir_2 = Pion(CASES.index(pions_positions[pion_noir_2_tortue]), 'noir', not(sens), pion_noir_2_tortue)
    pion_noir_3 = Pion(CASES.index(pions_positions[pion_noir_3_tortue]), 'noir', not(sens), pion_noir_3_tortue)
    pion_noir_4 = Pion(CASES.index(pions_positions[pion_noir_4_tortue]), 'noir', not(sens), pion_noir_4_tortue)
    pion_noir_5 = Pion(CASES.index(pions_positions[pion_noir_5_tortue]), 'noir', not(sens), pion_noir_5_tortue)
    pion_noir_6 = Pion(CASES.index(pions_positions[pion_noir_6_tortue]), 'noir', not(sens), pion_noir_6_tortue)
    pion_noir_7 = Pion(CASES.index(pions_positions[pion_noir_7_tortue]), 'noir', not(sens), pion_noir_7_tortue)
    pion_noir_8 = Pion(CASES.index(pions_positions[pion_noir_8_tortue]), 'noir', not(sens), pion_noir_8_tortue)

    fou_noir_1 = Fou(CASES.index(pions_positions[fou_noir_1_tortue]), 'noir', fou_noir_1_tortue)
    fou_noir_2 = Fou(CASES.index(pions_positions[fou_noir_2_tortue]), 'noir', fou_noir_2_tortue)
    cavalier_noir_1 = Cavalier(CASES.index(pions_positions[cavalier_noir_1_tortue]), 'noir', cavalier_noir_1_tortue)
    cavalier_noir_2 = Cavalier(CASES.index(pions_positions[cavalier_noir_2_tortue]), 'noir', cavalier_noir_2_tortue)
    tour_noir_1 = Tour(CASES.index(pions_positions[tour_noir_1_tortue]), 'noir', tour_noir_1_tortue)
    tour_noir_2 = Tour(CASES.index(pions_positions[tour_noir_2_tortue]), 'noir', tour_noir_2_tortue)
    reine_noir = Reine(CASES.index(pions_positions[reine_noir_tortue]), 'noir', reine_noir_tortue)
    roi_noir = Roi(CASES.index(pions_positions[roi_noir_tortue]), 'noir', roi_noir_tortue)
    
    for i in pions_positions:  # i est la tortue de chaque pièce
        j = pions_positions[i] # case où doivent aller les pièces au début de la partie
        i.penup()
        i.goto(eval("case_" + j + ".coordonnees"))
        ########################## Pour tester le cases prises en compte par la boucle -> la case h2 n'est pas prise en compte et une case sur deux bug après
        # carree(eval("case_" + j + ".coordonnees[0]"), eval("case_" + j + ".coordonnees[1]"), 45, tortue, '#ff0000', 0)
        ##############################################################################################################
    if sens:
        exec("pion_blanc_8_tortue.goto(265.00, -225.00)")
        exec("cavalier_blanc_1_tortue.goto(-275.00, -315.00)")
        exec("cavalier_blanc_2_tortue.goto(175.00, -315.00)")
        exec("reine_blanc_tortue.goto(-95.00, -315.00)")
        exec("fou_blanc_2_tortue.goto(85.00, -315.00)")
    else:
        exec("pion_noir_8_tortue.goto(265.00, -225.00)")
        exec("cavalier_noir_1_tortue.goto(-275.00, -315.00)")
        exec("cavalier_noir_2_tortue.goto(175.00, -315.00)")
        exec("reine_noir_tortue.goto(-5.00, -315.00)")
        exec("roi_noir_tortue.goto(-95.00, -315.00)")
        exec("fou_noir_2_tortue.goto(85.00, -315.00)")
    # Les 5 et 6 lignes au-dessus sont présentes car le code bug et après des heures (littéralement des heures) on n'a trouver aucune solution car tout est correct 

    for i in pions_positions_str:
        piece = i[:-7]
        case = pions_positions_str[i]
        exec("case_" + case + ".ChangerLeStatutDeLaCase()")
        exec("case_" + case + ".occupeeParQuelCamp = " + piece + ".couleur")
        exec("case_" + case + ".occupeeParQuellePiece = " + piece)
    # etat = etat_partie()
    # print(etat)
    sleep(1)
    deplacerUnePiece('a2', 'a3')
    wn.update()
    wn.mainloop()

faire_le_plateau()