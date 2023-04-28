from pokemon import Pokemon


class Terre(Pokemon):
    def __init__(self, nom, niveau, puissance_attaque, defense):
        super().__init__(nom, niveau, puissance_attaque, defense, "Terre")
        self.type = "Terre"
        self.type_attaque = {"Normal": 1, "Feu": 0.5, "Eau": 2, "Terre": 1}
