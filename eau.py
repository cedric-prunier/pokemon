from pokemon import Pokemon


class Eau(Pokemon):
    def __init__(self, nom, niveau, puissance_attaque, defense):
        super().__init__(nom, niveau, puissance_attaque, defense, "Eau")
        self.type = "Eau"
        self.type_attaque = {"Normal": 1, "Feu": 2, "Eau": 1, "Terre": 0.5}
