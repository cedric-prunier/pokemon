from pokemon import Pokemon


class Normal(Pokemon):
    def __init__(self, nom, niveau, puissance_attaque, defense):
        super().__init__(nom, niveau, puissance_attaque, defense, "Normal")
        self.type = "Normal"
        self.type_attaque = {"Normal": 1, "Feu": 0.75, "Eau": 0.75, "Terre": 0.75}
