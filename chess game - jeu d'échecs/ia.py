import pieces

### Fonctions d'évaluation de plusieurs même pièces

def eval_piece(*args) -> list:
    '''Calcul la pièce ayant le plus de valeur parmis plusieurs pièces du même type
    Un pion qui peut manger un reine aura plus de valeur qu'un pion qui peut manger un autre pion
    '''
    ### Commentaire à supprimer -> Faire le calcul des coup à l'avance dans la class de l'ia en appelant plusieurs fois la fonction 