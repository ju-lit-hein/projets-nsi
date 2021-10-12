import turtle
import plateau
import creation_des_pieces

INFORMATIONS = 'le pavé en dessous'
'''Pour obtenir :
- lettre et numéro d'une case (par exemple a1) : cases[caseActuelle]
- numéro de la case actuelle (par exemple 21) : Piece.caseActuelle
- coordonées Turtle d'une case (par exemple (-200, 50) ) : locals(){'pos_' + str(cases[self.caseActuelle])} 

Pour chaque pièces, (on va prendre pour exemple le fou) mouvement_fou[-1] est un booléens.
S'il est Vrai les mouvement de la pièce peuvent se répéter :
    fou en 36 peut aller en : 
    - 36 - 11 = 25
    - mais aussi en 25 - 11 = 14 et ainsi de suite et pour toutes les directions
'''
COTE_CASES = 90

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
    'a1','b1','c1','d1','e1','f1','g1','h1'
]

'''Définition'''
pieces = ('cavalier','fou','pion','reine','roi','tour','vide')
valeur_pieces = (3,3,1,9,0,5,0)
mouvement_cavalier = (-12,-21,-19,-8,12,21,19,8,False)
mouvement_fou = (-11,-9,11,9,True)
mouvement_pion = (-16,-8,-9,-7,False)
mouvement_tour = (-10,10,-1,1,True)
mouvement_reine = (-11,-10,-9,-1,11,10,9,1,True)
mouvement_roi = (-11,-10,-9,-1,11,10,9,1,False)






class Piece:
    '''
    class Piece
        Données :
            - Couleur
            - DéplacementPossibles
            - CaseActuelle
            - Tortue
        Actions : 
            - MouvementPossibles()
            - MontrerDéplacementPossibles()
            - MangerUnePiece()
            - DeplacerPiece()
    '''
    def __init__(self, couleur, deplacementPossibles, caseActuelle, tortue):
        self.couleur = couleur                              # str -> camp de la pièce
        self.deplacementsPossibles = deplacementPossibles   # tuple -> les déplacement possibles
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
    
    def MontrerDeplacementsPossibles(self):
        '''Montre au joueur toutes les cases où sa pièce peut se déplacer après avoir effacer les cases déjà marquées (pour une autre pièces par exemple'''
        marquage.clear()
        casesAMarquer = []
        for i in self.deplacements_possibles:
            exec("casesAMarquer.append(case_" + CASES[i] +".coordonnees)")
            pass
        coordonneesAMarquer = []
        for cases in casesAMarquer:
            case = (cases[0] + COTE_CASES * 0.45, cases[1] + COTE_CASES * 0.45)
            coordonneesAMarquer.append(case)
        for coord in coordonneesAMarquer:
            carree(coord[0], coord[1], 10, marquage, 'cyan', 0)



'''Code des pions : type_C_numéro   (C =Couleur) '''

