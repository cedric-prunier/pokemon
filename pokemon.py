class Pokemon:
    def __init__(self, nom, niveau, puissance_attaque, defense, type_pokemon):
        self._nom = nom
        self._points_de_vie = 100
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = 0
        self.type_pokemon = type_pokemon

    @property
    def points_de_vie(self):
        return self._points_de_vie

    @points_de_vie.setter
    def points_de_vie(self, value):
        self._points_de_vie = value

    def afficher_information(self):
        return f"{self._nom} ({self.type_pokemon}) - PV: {self._points_de_vie}, Attaque: {self.puissance_attaque}, Defense: {self.defense}"
