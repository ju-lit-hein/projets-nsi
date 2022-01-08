from pieces import Cavalier, Fou, Pion, Reine, Roi, Tour
### Fonctions d'évaluation de plusieurs même pièces

def eval_piece(*args) -> list:
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