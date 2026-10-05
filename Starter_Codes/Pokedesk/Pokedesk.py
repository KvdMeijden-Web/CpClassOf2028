import json
import os

def open_file():
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, "pokedex.json")
    with open(path, "r", encoding="utf-8") as file:
        pokemon_data = json.load(file)
        return pokemon_data



def search_type(pokemon_data):
    search_type = input("Enter Pokémon type: ").capitalize()
    print("\nPokémon with type ="+ search_type+":")
    for pokemon in pokemon_data:
        if search_type in pokemon["type"]:
            print(pokemon["name"]["english"])
           

pokedesk = open_file()
search_type(pokedesk)