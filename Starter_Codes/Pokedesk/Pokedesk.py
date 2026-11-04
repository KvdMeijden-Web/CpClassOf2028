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
           
def search_name(pokemon_data):
    search_name = input("Enter Pokémon name: ").capitalize()
    print("\nSearching"+search_name+":")
    for pokemon in pokemon_data:
            if search_name in pokemon["name"]["english"]:
                print(f'----{pokemon["name"]["english"]}----')
                print(f'{pokemon["description"]}')
                print(f'HP: {pokemon["base"]["HP"]}')
                print(f'Attack: {pokemon["base"]["Attack"]}')
                print(f'Defense: {pokemon["base"]["Defense"]}')
                print(f'Sp. Attack: {pokemon["base"]["Sp. Attack"]}')
                print(f'Sp. Defense: {pokemon["base"]["Sp. Defense"]}')
                print(f'Speed: {pokemon["base"]["Speed"]}')
                id = pokemon["evolution"]["next"]
                Search_evolutions(pokemon_data,id)
def Search_evolutions(pokemon_data,search):
    evolve =[]
    for evolution in search:
       result = int(evolution[0])
       evolve.append(result)
       
    for pokemon in pokemon_data:
        if pokemon["id"] in evolve:
            print(pokemon["name"]["english"])
        
            if "evolution" in pokemon and "next" in pokemon["evolution"]:
                next_evolution = pokemon["evolution"]["next"]

                Search_evolutions(
                    pokemon_data,
                    next_evolution
                )
pokedesk = open_file()
search_name(pokedesk)