# main.py
from combat import Combat
from pokedex import Pokedex
from normal import Normal
from feu import Feu
from eau import Eau
from terre import Terre
import json
import random
import os


def charger_pokemon_liste():
    fichier_pokedex = "pokedex.json"

    if not os.path.exists(fichier_pokedex):
        with open(fichier_pokedex, "w") as fichier:
            json.dump({}, fichier)

    with open("pokedex.json", "r") as fichier:
        pokedex_data = json.load(fichier)
        return pokedex_data


def creer_pokemon_objet(pokemon_data):
    type_pokemon = pokemon_data["type"]
    if type_pokemon.lower() == "normal":
        return Normal(
            pokemon_data["nom"],
            pokemon_data["niveau"],
            pokemon_data["puissance_attaque"],
            pokemon_data["defense"],
        )
    elif type_pokemon.lower() == "feu":
        return Feu(
            pokemon_data["nom"],
            pokemon_data["niveau"],
            pokemon_data["puissance_attaque"],
            pokemon_data["defense"],
        )
    elif type_pokemon.lower() == "eau":
        return Eau(
            pokemon_data["nom"],
            pokemon_data["niveau"],
            pokemon_data["puissance_attaque"],
            pokemon_data["defense"],
        )
    elif type_pokemon.lower() == "terre":
        return Terre(
            pokemon_data["nom"],
            pokemon_data["niveau"],
            pokemon_data["puissance_attaque"],
            pokemon_data["defense"],
        )
    else:
        return None


def lancer_partie():
    pokemon_liste = charger_pokemon_liste()
    if not pokemon_liste:
        print(
            "Aucun Pokémon disponible pour jouer. Ajoutez des Pokémon à votre fichier pokedex.json."
        )
        return

    print("Liste des Pokémon disponibles :")
    for nom_pokemon, pokemon_data in pokemon_liste.items():
        print(f"{pokemon_data['nom']} ({pokemon_data['type']})")

    pokemon_joueur_data = None
    while not pokemon_joueur_data:
        nom_pokemon_joueur = input(
            "Veuillez choisir un Pokémon parmi la liste : "
        ).lower()

        for nom_pokemon, pokemon_data in pokemon_liste.items():
            if pokemon_data["nom"].lower() == nom_pokemon_joueur:
                pokemon_joueur_data = pokemon_data
                break

        if not pokemon_joueur_data:
            print("Le Pokémon choisi est introuvable. Veuillez réessayer.")

    pokemon_adversaire_data = random.choice(list(pokemon_liste.values()))

    pokemon_joueur = creer_pokemon_objet(pokemon_joueur_data)
    pokemon_adversaire = creer_pokemon_objet(pokemon_adversaire_data)

    if not pokemon_joueur or not pokemon_adversaire:
        print(
            "Erreur lors de la création des objets Pokémon. Veuillez vérifier les données des Pokémon."
        )
        return

    combat = Combat(pokemon_joueur, pokemon_adversaire)
    vainqueur = combat.lancer_combat()

    if vainqueur:
        print(f"{vainqueur} a remporté le combat!")
    else:
        print("Le combat est terminé sans vainqueur.")


def ajouter_pokemon(pokedex):
    print("Veuillez entrer les informations du Pokémon à ajouter :")
    nom = input("Nom : ")
    type_pokemon = input("Type (Normal, Feu, Eau, Terre) : ")
    niveau = int(input("Niveau : "))
    puissance_attaque = int(input("Puissance d'attaque : "))
    defense = 0

    if type_pokemon.lower() == "normal":
        pokemon = Normal(nom, niveau, puissance_attaque, defense)
    elif type_pokemon.lower() == "feu":
        pokemon = Feu(nom, niveau, puissance_attaque, defense)
    elif type_pokemon.lower() == "eau":
        pokemon = Eau(nom, niveau, puissance_attaque, defense)
    elif type_pokemon.lower() == "terre":
        pokemon = Terre(nom, niveau, puissance_attaque, defense)
    else:
        print("Type de Pokémon invalide.")
        return

    pokedex.ajouter_pokemon(pokemon)


def menu(pokedex):
    while True:
        print("Menu principal :")
        print("1. Lancer une partie")
        print("2. Ajouter un Pokémon")
        print("3. Accéder à son Pokédex")
        print("4. Quitter")
        choix = input("Veuillez choisir une option (1-4) : ")

        if choix == "1":
            lancer_partie()

        elif choix == "2":
            ajouter_pokemon(pokedex)

        elif choix == "3":
            pokedex.afficher_pokedex()

        elif choix == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez choisir une option entre 1 et 4.")


if __name__ == "__main__":
    pokedex = Pokedex()
    menu(pokedex)
