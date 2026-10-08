import json
import os
import tkinter as tk
import requests

from PIL import Image, ImageTk
from io import BytesIO


# 1. LOAD DATA

def open_file():
    folder = os.path.dirname(__file__)
    path = os.path.join(folder, "pokedex.json")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


# 2. SEARCH FUNCTIONS

def search_name(pokemon_data, name):

    for pokemon in pokemon_data:
        if name.lower() == pokemon["name"]["english"].lower():
            return pokemon

    return None


def Search_evolutions(pokemon_data, search):

    evolution_names = []

    for evolution in search:
        evolution_id = int(evolution[0])

        for pokemon in pokemon_data:
            if pokemon["id"] == evolution_id:

                evolution_names.append(
                    pokemon["name"]["english"]
                )

                next_evolution = pokemon.get(
                    "evolution", {}
                ).get("next", [])

                if next_evolution:
                    evolution_names.extend(
                        Search_evolutions(pokemon_data, next_evolution)
                    )

    return evolution_names


# 3. IMAGE FUNCTION

def load_image(url):

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))
    image = image.convert("RGBA")
    image.thumbnail((250, 250))

    return ImageTk.PhotoImage(image)


# 4. CREATE INTERFACE

def create_interface():

    pokemon_data = open_file()

    root = tk.Tk()
    root.title("Pokédex")
    root.config(bg="lightcoral")
    root.geometry("700x850")

    Title = tk.Label(
        root,
        text="Pokédex",
        font=("Arial", 32),
        bg="lightcoral"
    )
    Title.pack(pady=15)

    # Search input
    search = tk.Entry(root, font=("Arial", 20))
    search.pack(pady=10)

    # Pokémon name
    Name = tk.Label(
        root,
        text="Search for a Pokémon",
        font=("Arial", 22)
    )
    Name.pack(pady=10)

    # Pokémon image
    PokemonImage = tk.Label(root)
    PokemonImage.pack(pady=10)

    # Description
    Description = tk.Label(
        root,
        text="Description",
        font=("Arial", 14),
        wraplength=600
    )
    Description.pack(pady=10)

    # Statistics
    Stats = tk.Label(
        root,
        text="Statistics",
        font=("Arial", 14),
        justify="left"
    )
    Stats.pack(pady=10)

    # Evolutions
    Evolutions = tk.Label(
        root,
        text="Evolutions",
        font=("Arial", 14)
    )
    Evolutions.pack(pady=10)


    # 5. EVENT HANDLER

    def search_clicked():

        name = search.get().strip()
        pokemon = search_name(pokemon_data, name)

        if pokemon:

            # Update name
            Name.config(text=pokemon["name"]["english"])

            # Update description
            Description.config(
                text=pokemon.get("description", "")
            )

            # Update statistics
            Stats.config(text=(
                f'HP: {pokemon["base"]["HP"]}\n'
                f'Attack: {pokemon["base"]["Attack"]}\n'
                f'Defense: {pokemon["base"]["Defense"]}\n'
                f'Sp. Attack: {pokemon["base"]["Sp. Attack"]}\n'
                f'Sp. Defense: {pokemon["base"]["Sp. Defense"]}\n'
                f'Speed: {pokemon["base"]["Speed"]}'
            ))

            # Update evolutions
            next_evolution = pokemon.get(
                "evolution", {}
            ).get("next", [])

            if next_evolution:
                names = Search_evolutions(
                    pokemon_data, next_evolution
                )
                Evolutions.config(
                    text="Evolutions: " + ", ".join(names)
                )
            else:
                Evolutions.config(text="No further evolutions")

            # Update Pokémon image
            image_url = pokemon["image"]["hires"]

            try:
                photo = load_image(image_url)

                PokemonImage.config(image=photo, text="")
                PokemonImage.image = photo

            except (requests.RequestException, OSError, ValueError):
                PokemonImage.config(
                    image="",
                    text="Image could not be loaded"
                )
                PokemonImage.image = None

        else:
            Name.config(text="Pokémon not found")
            Description.config(text="")
            Stats.config(text="")
            Evolutions.config(text="")
            PokemonImage.config(image="", text="")
            PokemonImage.image = None


    # Search button
    button = tk.Button(
        root,
        text="Search Pokémon",
        command=search_clicked,
        font=("Arial", 20),
        bg="pink"
    )
    button.pack(pady=10)

    root.mainloop()


# START
create_interface()