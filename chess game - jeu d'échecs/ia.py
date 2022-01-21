from pieces import *
### Fonctions d'évaluation de plusieurs même pièces

def eval_piece(*args) -> dict:
    '''Calcul la pièce ayant le plus de valeur parmis plusieurs pièces du même type
    Un pion qui peut manger un reine aura plus de valeur qu'un pion qui peut manger un autre pion
    '''
    liste_pieces = [Cavalier, Fou, Pion, Reine, Roi, Tour]
    for i in args:
        assert type(i) in liste_pieces
    ### Commentaire à supprimer -> Faire le calcul des coup à l'avance dans la class de l'ia en appelant plusieurs fois la fonction
    coups_possibles = {}
    for piece in args:
        coups_possibles[piece] = piece.mouvementPossibles()

    note_pieces = {}
    return note_pieces # note_pieces est le dictionnaire contenant {objet piece : score}


class IA():
    def __init__(self) -> None:
        pass

    ### faire un algo minmax() qui prend en argument la liste retournée par eval_piece()

# l'algorithme minimax utilisera le principe de récursivité

def minimax(data={}, miniormaxi=-1):
    '''
    
    miniormaxi : True si on cherche le et False si on cherche le
    '''
    assert type(data) == dict, "L'argument doit être un dictionnaire"
    if len(data) % 2 == 0:
        depth = len(data) // 2
    else:
        depth = len(data) // 2 + 1
    if miniormaxi == -1:                                                # valeur de 1- par défaut pour pouvoir définir True ou False selon depth qui n'est pas encore définie lorsqu'on appelle la focntion
        miniormaxi = bool(depth % 2)
    if depth != 0:
        erkjvherk = {}
        for element in range(depth):
            try:
                pass
            except:
                pass

### comparer deux par deux les élément et ajouter le mini ou maxi dans le dico erkvherk                






### voir si c'est pas mieux d'utiliser une liste [key, value, ...]
a = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10}