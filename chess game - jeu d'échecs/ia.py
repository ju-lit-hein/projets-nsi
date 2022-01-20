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

def minimax(depth, score):
    assert type(score) == dict, "score n'est pas un dictionnaire"
    if depth:
        for dpd in score:

### voir si c'est pas mieux d'utiliser une liste [key, value, ...]
