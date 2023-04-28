from pokemon import Pokemon


class Feu(Pokemon):
    def __init__(self, nom, niveau, puissance_attaque, defense):
        super().__init__(nom, niveau, puissance_attaque, defense, "Feu")
        self.type = "Feu"
        self.type_attaque = {"Normal": 1, "Feu": 1, "Eau": 0.5, "Terre": 2}
