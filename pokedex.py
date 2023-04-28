import json
from pokemon import Pokemon


class Pokedex:
    def __init__(self):
        self._pokedex_fichier = "pokedex.json"
        self._pokedex_data = self._charger_pokedex()

    def _charger_pokedex(self):
        try:
            with open(self._pokedex_fichier, "r") as fichier:
                return json.load(fichier)
        except FileNotFoundError:
            return {}

    def _sauvegarder_pokedex(self):
        with open(self._pokedex_fichier, "w") as fichier:
            json.dump(self._pokedex_data, fichier, indent=1)

    def ajouter_pokemon(self, pokemon: Pokemon):
        nom = pokemon._nom.lower()
        if nom not in self._pokedex_data:
            self._pokedex_data[nom] = {
                "nom": pokemon._nom,
                "type": pokemon.type_pokemon,
                "niveau": pokemon.niveau,
                "puissance_attaque": pokemon.puissance_attaque,
                "defense": pokemon.defense,
                "points_de_vie": pokemon._points_de_vie,
            }
            self._sauvegarder_pokedex()
            print(f"{pokemon._nom} a été ajouté au Pokédex.")
        else:
            print(f"{pokemon._nom} est déjà dans le Pokédex.")

    def afficher_pokedex(self):
        if not self._pokedex_data:
            print("Votre Pokédex est vide.")
            return

        print("Pokédex :")
        for pokemon_data in self._pokedex_data.values():
            print(
                f"{pokemon_data['nom']} ({pokemon_data['type']}) - Niveau: {pokemon_data['niveau']}, Attaque: {pokemon_data['puissance_attaque']}, "
                f"Defense: {pokemon_data['defense']}, PV: {pokemon_data['points_de_vie']}"
            )
