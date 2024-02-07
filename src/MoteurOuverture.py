from .Lecteur import Lecteur
from .Porte import Porte

class MoteurOuverture:
    def __init__(self, porte: Porte):
        self._porte = porte

    def interroger(self, lecteur: Lecteur):
        if lecteur.badge_detecte:
            self._porte.ouvrir()