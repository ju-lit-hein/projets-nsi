import turtle
import plateau

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

marquage = turtle.Turtle()
marquage.pencolor('cyan')
marquage.pensize(1)

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
    def __init__(self, couleur, deplacementPossibles, caseActuelle):
        self.couleur = couleur                              # str -> camp de la pièce
        self.deplacementsPossibles = deplacementPossibles   # tuple -> les déplacement possibles
        self.CaseActuelle = caseActuelle                    # int -> le numéro de la case


    def MouvementsPossibles(self,mouvements_possibles):
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
        return deplacements_possibles
    
    def MontrerDeplacementsPossibles(self, deplacements_possibles):
        '''Montre au joueur toutes les cases où sa pièce peut se déplacer après avoir effacer les cases déjà marquées (pour une autre pièces par exemple'''
        marquage.clear()
        casesAMarquer = [locals()['pos_' + str(plateau.cases[i])] for i in deplacements_possibles] # liste contenant l'angle bas-gauche des cases à marquer
        coordonneesAMarquer = []
        for cases in casesAMarquer:
            case = (cases[0] + plateau.COTE_CASES * 0.45, cases[1] + plateau.COTE_CASES * 0.45)
            coordonneesAMarquer.append(case)
        for coord in coordonneesAMarquer:
            plateau.carree(coord[0], coord[1], 10, marquage, 'cyan', 0)
    



        
'''
class Piece
    Données :
        Couleur
        DéplacementPossibles
        CaseActuelle
    Actions : 
        MouvementPossibles()
        MontrerDéplacementPossibles()
        Deplacer()
'''