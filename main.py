import argparse
import requests


def get_pokemon_info(pokemon_name: str) -> None:
    """Fetch and print information for a given Pokémon name or ID."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.strip().lower()}"
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"Error fetching '{pokemon_name}': {e}")
        return

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        print(f"Name: {data['name'].title()}")
        print(f"Height: {data['height']} decimetres")
        print(f"Weight: {data['weight']} hectograms")
        print(f"Types: {data['types']}")
    elif response.status_code == 404:
        print(f"Error: Pokémon '{pokemon_name}' not found.")
    else:
        print(f"Error: Received status code {response.status_code}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch and display Pokémon information."
    )
    parser.add_argument(
        "pokemon",
        nargs="+",
        help="Name(s) or ID(s) of the Pokémon to look up",
    )
    args = parser.parse_args()

    for i, name in enumerate(args.pokemon):
        if i > 0:
            print()
        get_pokemon_info(name)


if __name__ == "__main__":
    main()

