import turtle
from plateau import plateau_pour_pas_faire_de_sortie_de_plateau_ou_de_mouvements_illogiques, plateau_pour_pas_faire_de_sortie_de_plateau_ou_de_mouvements_illogiques_bis
#import creation_des_pieces

INFORMATIONS = 'le pavé en dessous'
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
COTE_CASES = 90
PL_120 = plateau_pour_pas_faire_de_sortie_de_plateau_ou_de_mouvements_illogiques
PL_64 = plateau_pour_pas_faire_de_sortie_de_plateau_ou_de_mouvements_illogiques_bis

marquage = turtle.Turtle()
marquage.pencolor('cyan')
marquage.pensize(1)
marquage.hideturtle()


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
                carree(coordonnees[0] - 45, coordonnees[1] -45 , 90, marquage, '#b32727', 0)
            else:
                carree(coordonnees[0] - 45, coordonnees[1] - 45, 10, marquage, '#2f43ba', 0)        


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
            - Sens -> int 1 si le pion avance vers la haut du plateau et 0 si il avance vers le bas
            - Tortue -> turtle.Turtle Object -> tortue qui représente le pion   

        Actions : 
            - MouvementsPossibles() -> dict
    '''
    def __init__(self, couleur, caseActuelle, sens, tortue, dejaBouge = False):
        self.caseActuelle = caseActuelle                    # int -> numéro de la case sur laquelle le pion est
        self.couleur = couleur                              # str -> camp de la pièce
        self.dejaBouge = dejaBouge                          # bool -> vérifie si le pion a déjà bougé
        self.sens = sens
        if self.sens == 1:                                  # si le pion est orinté vers le haut
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
    def __init__(self, caseActuelle, couleur, tortue):
        self.caseActuelle = caseActuelle
        self.couleur = couleur
        self.deplacementsPossibles = (-12, -21, -19, -8, 12, 21, 19, 8)
        self.tortue = tortue

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
    def __init__(self, caseActuelle, couleur, tortue):
        self.caseActuelle = caseActuelle
        self.couleur = couleur
        self.deplacementsPossibles = (-9,-7, 7, 9)
        self.tortue = tortue
    

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
    def __init__(self, caseActuelle, couleur, tortue):
        self.caseActuelle = caseActuelle
        self.couleur = couleur
        self.deplacementsPossibles = (-8, -1, 1, 8)
        self.tortue = tortue

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
    def __init__(self, caseActuelle, couleur, tortue):
        self.caseActuelle = caseActuelle
        self.couleur = couleur
        self.deplacementsPossibles = (-9, -8, -7, -1, 1, 7, 8, 9)
        self.tortue = tortue

    def MouvementsPossibles(self) -> dict:
        dico_deplacements_possibles = {}
        for i in self.deplacementsPossibles:
            while PL_120[PL_64[self.caseActuelle + i]] != -1:                                                                           # tant que la pièce reste dans le plateau
                if eval("case_" + CASES[self.caseActuelle] + ".occupeeParQuelCamp") != self.couleur:                                    # si la case, n'est pas occupée par un pièce du même camp
                    dico_deplacements_possibles[CASES[self.caseActuelle + i]] = eval("case_" + CASES[self.caseActuelle] + ".occupee")   # la case est ajoutée au $dico_deplacements_possibles avec pour valeur si la case est occupée ou non (si la case est libre -> rien à manger -> False | si la case est occupée c'est forcément une pièce du camp adverse -> il faut manger la pièce -> True)
        return dico_deplacements_possibles




class Piece:
    def __init__(self, couleur, caseActuelle, tortue):
        self.couleur = couleur                              # str -> camp de la pièce
        self.deplacementsPossibles = ()                     # tuple -> les déplacement possibles
        self.CaseActuelle = caseActuelle                    # int -> le numéro de la case
        self.tortue = tortue                                # turtle.Turtle Object -> la tortue qui à l'image du pion


    def MouvementsPossibles(self):
        '''Retourne le numéro de toutes les cases où la pièce peut se déplacer sous forme de liste.'''
        deplacements_possibles = []                                                     # initialisation de la liste des déplacements possibles
        depart = self.CaseActuelle                                                      # depart est la variable "point de départ" pour calculer les déplacements possibles
        if self.deplacementsPossibles[-1] == False:                                     # si la pièce ne peut se déplcer que d'une case à la fois
            for i in range(len(self.deplacementsPossibles) - 1):                        # pour tout les mouvements dans le tuple self.dP, sauf le dernier qui est un booléen
                deplacements_possibles.append(depart + self.deplacementsPossibles[i])   # ajoute à la liste des déplacements possibles le numéro des cases où la pièce peut aller
        else:                                                                           # si la pièce peut se déplacer de plusieurs cases à la fois
            for i in range(len(self.deplacementsPossibles) - 1):                        # pout tout les mouvements dans le tuple self.dP, sauf le dernier qui est un booléen
                etape = depart                                                          # initialisation de la variable etape qui prend la valeur de $depart pour pouvoir être modifiée sans perdre la valeur $depart
                while 0 <= etape + self.deplacementsPossibles[i] <= 63:                 # tant que etape + le mouvement en cours de calcul est positif et inférieur à 64
                    deplacements_possibles.append(etape + self.deplacementsPossibles[i])# ajouter à la liste des déplacements possibles le numéro des cases où la pièce peut aller
                    etape += self.deplacementsPossibles[i]                              # etape prend la valeur de la case qu'on vient d'ajouter pour calculer la case suivante

                # pour la boucle while ajouter les conditions si la cases est occupée ou pas et si elle l'est, si c'est une pièce de notre camp donc non-mangeable ou si c'est une pièce du camp adverse et donc mangeable
        self.deplacements_possibles = deplacements_possibles
    

