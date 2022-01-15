import pieces
import creation

class Jeu:
    def __init__(self) -> None:
        self.tour = creation.jouer_blanc

    def set_tour(self) -> None:
        self.tour = not self.tour

    