import pieces
import creation

class Jeu:
    def __init__(self) -> None:
        self.tour = creation.jouer_blanc

    def changeTour(self):
        self.tour = bool(self.tour * False)