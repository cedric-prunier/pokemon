import random
from pokemon import Pokemon
import time


class Combat:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def est_vivant(self, pokemon: Pokemon) -> bool:
        return pokemon.points_de_vie > 0

    def nom_vainqueur(self) -> str:
        if not self.est_vivant(self.pokemon1):
            return self.pokemon2._nom
        elif not self.est_vivant(self.pokemon2):
            return self.pokemon1._nom
        else:
            return ""

    def attaque_reussie(self) -> bool:
        return random.choice([0, 1]) == 1

    def calculer_degats(self, attaquant: Pokemon, defenseur: Pokemon) -> int:
        multiplicateur = attaquant.type_attaque[defenseur.type]
        degats = attaquant.puissance_attaque * multiplicateur
        return degats

    def enlever_points_de_vie(self, attaquant: Pokemon, defenseur: Pokemon) -> int:
        degats = self.calculer_degats(attaquant, defenseur)
        degats_reduits = degats - defenseur.defense
        if degats_reduits > 0:
            defenseur.points_de_vie -= degats_reduits
        else:
            degats_reduits = 0
        return degats_reduits

    def lancer_combat(self) -> str:
        print("Le combat commence !")
        print(
            f"{self.pokemon1._nom} ({self.pokemon1.points_de_vie} PV) vs {self.pokemon2._nom} ({self.pokemon2.points_de_vie} PV)"
        )

        while self.est_vivant(self.pokemon1) and self.est_vivant(self.pokemon2):
            if self.attaque_reussie():
                degats = self.enlever_points_de_vie(self.pokemon1, self.pokemon2)
                print(
                    f"{self.pokemon1._nom} a réussi son attaque et infligé {degats} points de dégâts à {self.pokemon2._nom}."
                )
                time.sleep(2)  # Délai de 1 seconde
            else:
                print(f"{self.pokemon1._nom} a raté son attaque.")
                time.sleep(2)

            if self.est_vivant(self.pokemon2):
                if self.attaque_reussie():
                    degats = self.enlever_points_de_vie(self.pokemon2, self.pokemon1)
                    print(
                        f"{self.pokemon2._nom} a réussi son attaque et infligé {degats} points de dégâts à {self.pokemon1._nom}."
                    )
                    time.sleep(2)  # Délai de 1 seconde
                else:
                    print(f"{self.pokemon2._nom} a raté son attaque.")
                    time.sleep(2)

            print(
                f"{self.pokemon1._nom} ({self.pokemon1.points_de_vie} PV) vs {self.pokemon2._nom} ({self.pokemon2.points_de_vie} PV)"
            )

        vainqueur = self.nom_vainqueur()

        return vainqueur
