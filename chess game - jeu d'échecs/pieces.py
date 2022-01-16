import turtle
from functools import partial

INFORMATIONS = 'le pavé en dessous' ### A corriger
'''Pour obtenir :
- lettre et numéro d'une case (par exemple a1) : cases[caseActuelle]
- numéro de la case actuelle (par exemple 21) : Piece.caseActuelle
- coordonées Turtle d'une case par exemple (265.00, -135.00) : pour la case 'h3' -> case_h3.coordonnees 

Pour chaque pièces, (on va prendre pour exemple le fou) mouvement_fou[-1] est un booléens.
S'il est Vrai les mouvement de la pièce peuvent se répéter :
    fou en 36 peut aller en : 
    - 36 - 11 = 25
    - mais aussi en 25 - 11 = 14 et ainsi de suite et pour toutes les directions
'''

PL_120 = (
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
) # = plateau_120
PL_64 = (
        21, 22, 23, 24, 25, 26, 27, 28,
        31, 32, 33, 34, 35, 36, 37, 38,
        41, 42, 43, 44, 45, 46, 47, 48,
        51, 52, 53, 54, 55, 56, 57, 58,
        61, 62, 63, 64, 65, 66, 67, 68,
        71, 72, 73, 74, 75, 76, 77, 78,
        81, 82, 83, 84, 85, 86, 87, 88,
        91, 92, 93, 94, 95, 96, 97, 98
) # = plateau_64

marquage = turtle.Turtle()
marquage.pencolor('cyan')
marquage.pensize(1)
marquage.hideturtle()

### Fonctions pour toutes les pièces

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

CASES = ['a8','b8','c8','d8','e8','f8','g8','h8', 'a7','b7','c7','d7','e7','f7','g7','h7', 'a6','b6','c6','d6','e6','f6','g6','h6', 'a5','b5','c5','d5','e5','f5','g5','h5', 'a4','b4','c4','d4','e4','f4','g4','h4', 'a3','b3','c3','d3','e3','f3','g3','h3', 'a2','b2','c2','d2','e2','f2','g2','h2', 'a1','b1','c1','d1','e1','f1','g1','h1']

def MontrerDeplacementsPossibles(DDP):
    '''DDP -> dictionnaire {objet de la case à marquer : True -> Piece à manger ; False -> deplacement simple'''
    if len(DDP) < 0:
        for i in DDP:
            coordonnees = i.get_coordonnees()
            if DDP[i]: # si la clé (la case) a pour valeur True, c'est une piece  manger donc la case sera en rouge
                carree(coordonnees[0] - 5, coordonnees[1] - 5 , 10, marquage, '#b32727', 0)
            else: # sinon, la case sera en bleu car ce sera un simple déplacement.
                carree(coordonnees[0] - 5, coordonnees[1] - 5, 10, marquage, '#2f43ba', 0)        


def mangerUnePiece(piece, case, piece_mangee):
    '''Deplace la pièce voulue vers une case et mange la pièce sur la case :    
    - piece -> class nom de la pièce qui est déplacée
    - case -> objet case_XX de la classe Plateau
    - piece_mangee -> class nom de la piece mangee
    '''

    # on rend libre la case actuelle de la piece qui mange
    caseActuelle = piece.get_case_actuelle()
    caseActuelle.ChangerLeStatutDeLaCase()

    # on deplace la piece qui mange vers sa nouvelle case
    coordonnees = case.get_coordonnees()
    piece.aller_a(coordonnees)
    piece.ChangerLaCase(case)
    case.ChangerLestatutDeLaCase()
    case.ChangerLeCamp()

    # on sort la piece mangee du plateau
    piece_mangee.aller_a(-750,0)
    piece_mangee.cacher()


def deplacerUnePiece(piece, case):
    '''Deplace la pièce voulue vers une case :  
    - piece -> objet de la piece a deplacer
    - case -> objet dela case d'arrivee
    '''
    if case.est_occupee:                                                                                    # si la case d'arrivée est ocuppée
        piece_a_manger = case.get_piece()                                                                   
        mangerUnePiece(piece, case, piece_a_manger)
        return 0
    coordonnees = case.get_coordonnees()                                                                    # récupère les coordoonées de la case d'arrivée
    piece.aller_a(coordonnees)
    piece.ChangerLaCase(case)
    caseActuelle = piece.get_case()
    caseActuelle.ChangerLeStatutDeLaCase()                                                                  # rend la case de départ inoccupée
    case.ChangerLeStatutDeLaCase()                                                                          # rend la case d'arrivée occupée
    case.ChangerLaPiece(piece)                                                                              # change la piece qui occuppe la case
    case.ChangerLeCamp(piece.get)                                                                           # change la camp qui occuppe la case
    


'''Définition'''
pieces = ('cavalier','fou','pion','reine','roi','tour')
valeur_pieces = (3,3,1,9,0,5)
mouvement_cavalier = (-12,-21,-19,-8,12,21,19,8)
mouvement_fou = (-11,-9,11,9)
mouvement_tour = (-10,10,-1,1)


### Classe de chaque pièce

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
        self.caseActuelle = caseActuelle                    # Plateau -> objet case        #########
        self.couleur = couleur                              # str -> camp de la pièce
        self.dejaBouge = dejaBouge                          # bool -> vérifie si le pion a déjà bougé
        self.sens = sens                                    # bool -> voir définition de a class
        if self.sens:                                  # si le pion est orinté vers le haut
            self.deplacementsPossibles = (-16,-8,-9,-7)     # tuple -> déplacements possibles de la pièce
        else:                                               # si le pion est orienté vers le bas
            self.deplacementsPossibles = (16,8,9,7)         # tuple -> déplacements possibles de la pièce
        self.tortue = tortue                                # turtle.Turtle Object -> tortue qui a l'image du pion
        self.alive = True
        self.tortue.onclick(partial(MontrerDeplacementsPossibles(self.MouvementsPossibles())))

    def __str__(self):
        return f"Ce pion {self.couleur} est sur la case {self.caseActuelle}. Déja bougé = {self.dejaBouge}. Il est représenté par la tortue {[i for i, a in locals().items() if a == self.tortue]}"

    def aller_a(self, x, y):
        self.tortue.goto(x, y)
    
    def cacher(self):
        self.tortue.hideturtle()
    
    def ChangerLaCase(self, case):
        self.caseActuelle = case

    def get_camp(self) -> str:
        return self.couleur
    
    def get_case(self) -> object: # -> Plateau
        return self.caseActuelle

    def set_dead(self):
        self.alive = False


    def MouvementsPossibles(self) -> dict:
        '''Retourne le numéro de toutes les cases où le pion peut se déplacer sous forme de dictionnaire'''
        dico_deplacements_possibles = {}
        point_de_depart = self.caseActuelle
        
        if self.dejaBouge == False:                                             # si le pion n'a pas encore bougé et peut donc avancer de deux cases d'un coup
            case_0 = point_de_depart + 20                                       # case où le pion à le droit d'aller
            case_1 = point_de_depart + 10                                       # case où le pion à le droit d'aller

            if not case_0.est_occupee():                                        # si la case est libre
                dico_deplacements_possibles[case_0] = False                     # case où le pion peut aller

            if not case_1.est_occupee():                                        # si la case est libre
                dico_deplacements_possibles[case_1] = False                     # case où le pion peut aller

        else:
            case_0 = point_de_depart + 10                                       # case où le pion à le droit d'aller

            if case_0 != -1 and not case_0.est_occupee():              # si la case est libre
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
        self.deplacementsPossibles = (-12,-21,-19,-8,12,21,19,8)
        self.tortue = tortue
        self.alive = True

    def __str__(self):
        return f"Ce cavalier {self.couleur} est sur la case {self.caseActuelle}. Il est représenté par la tortue {[i for i, a in locals().items() if a == self.tortue]}"

    def aller_a(self, x, y):
        self.tortue.goto(x, y)
    
    def cacher(self):
        self.tortue.hideturtle()
    
    def ChangerLaCase(self, case):
        self.caseActuelle = case

    def get_camp(self) -> str:
        return self.couleur
    
    def get_case(self) -> object: # -> Plateau
        return self.caseActuelle

    def set_dead(self):
        self.alive = False
        
    def MouvementsPossibles(self) -> dict:
        '''Retourne le numéro de toutes les cases où le cavalier peut se déplacer sous forme de dictionnaire'''
        dico_deplacements_possibles = {}
        for i in self.deplacementsPossibles:
            if PL_120[PL_64[self.caseActuelle] + i] != -1:                                                                              # si la pièce ne sort pas du plateau
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
        self.deplacementsPossibles = (-11,-9,11,9)
        self.tortue = tortue
        self.alive = True

    def __str__(self):
        return f"Ce fou {self.couleur} est sur la case {self.caseActuelle}. Il est représenté par la tortue {[i for i, a in locals().items() if a == self.tortue]}"

    def aller_a(self, x, y):
        self.tortue.goto(x, y)
    
    def cacher(self):
        self.tortue.hideturtle()
    
    def ChangerLaCase(self, case):
        self.caseActuelle = case

    def get_camp(self) -> str:
        return self.couleur
    
    def get_case(self) -> object: # -> Plateau
        return self.caseActuelle

    def set_dead(self):
        self.alive = False
        
    def MouvementsPossibles(self) -> dict:
        dico_deplacements_possibles = {}
        for i in self.deplacementsPossibles:
            while PL_120[PL_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
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
        self.deplacementsPossibles = (-10,10,-1,1)
        self.tortue = tortue
        self.alive = True

    def __str__(self):
        return f"Cette tour {self.couleur} est sur la case {self.caseActuelle}. Il est représenté par la tortue {[i for i, a in locals().items() if a == self.tortue]}"
    
    def aller_a(self, x, y):
        self.tortue.goto(x, y)
    
    def cacher(self):
        self.tortue.hideturtle()
    
    def ChangerLaCase(self, case):
        self.caseActuelle = case

    def get_camp(self) -> str:
        return self.couleur
    
    def get_case(self) -> object: # -> Plateau
        return self.caseActuelle

    def set_dead(self):
        self.alive = False
        
    def MouvementsPossibles(self) -> dict:
        dico_deplacements_possibles = {}
        for i in self.deplacementsPossibles:
            while PL_120[PL_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
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
        self.alive = True

    def __str__(self):
        return f"Cette reine {self.couleur} est sur la case {self.caseActuelle}. Il est représenté par la tortue {[i for i, a in locals().items() if a == self.tortue]}"

    def aller_a(self, x, y):
        self.tortue.goto(x, y)
    
    def cacher(self):
        self.tortue.hideturtle()
    
    def ChangerLaCase(self, case):
        self.caseActuelle = case

    def get_camp(self) -> str:
        return self.couleur
    
    def get_case(self) -> object: # -> Plateau
        return self.caseActuelle

    def set_dead(self):
        self.alive = False
        
    def MouvementsPossibles(self) -> dict:
        dico_deplacements_possibles = {}
        for i in self.deplacementsPossibles:
            while PL_120[PL_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
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
    
    def __str__(self):
        return f"Ce roi {self.couleur} est sur la case {self.caseActuelle}. Il est représenté par la tortue {[i for i, a in locals().items() if a == self.tortue]}. Déja bouge = {self.dejaBouge} et deja echec = {self.dejaEchec}"

    def aller_a(self, x, y):
        self.tortue.goto(x, y)
    
    def cacher(self):
        self.tortue.hideturtle()
    
    def ChangerLaCase(self, case):
        self.caseActuelle = case

    def get_camp(self) -> str:
        return self.couleur
    
    def get_case(self) -> object: # -> Plateau
        return self.caseActuelle
        
    def MouvementsPossibles(self) -> dict:
        dico_deplacements_possibles = {}
        for i in self.deplacementspossibles:
            if eval("case_" + CASES[self.caseActuelle + i] + ".occupeeParQuelCamp") != self.couleur:                                    # si la case, n'est pas occupée par un pièce du même camp
                dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
        return dico_deplacements_possibles