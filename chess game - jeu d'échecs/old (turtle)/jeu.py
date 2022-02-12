import pieces
import creation

class Jeu:
    def __init__(self) -> None:
        """
        tour = True si c'est ua joueur de jouer, False si c'est à l'ordinateur
        """
        self.tour = creation.jouer_blanc

    def set_tour(self) -> None:
        self.tour = not self.tour

    