# main.property

import copy
from pokemon_loader import load_pokemon_list
from battle_engine import execute_turn

def list_pokemon(pokemons):
    print("Available Pokémon:")
    for i, pokemon in enumerate(pokemons, 1):
        print(f"{i}. {pokemon.name}")
    choice = int(input("Choose a Pokémon by number: ")) - 1
    print()
    return copy.deepcopy(pokemons[choice])

def list_moves(pokemon):
    print(f"Available moves for {pokemon.name}:")
    for i, move in enumerate(pokemon.moves, 1):
        print(f"{i}. {move.name}")
    choice = int(input("Choose a move by number: ")) - 1
    print()
    return pokemon.moves[choice]

def main():
    pokemons = load_pokemon_list(---pokemon.xlsx location---)

    # List and choose Pokémon
    pokemon1 = list_pokemon(pokemons)
    pokemon2 = list_pokemon(pokemons)

    print(f"Battle between {pokemon1.name} and {pokemon2.name} begins!\n")

    turn_count = 0

    while pokemon1.battle_stats['hp'] > 0 and pokemon2.battle_stats['hp'] > 0:
        if turn_count > 1000:
            break
        
        # List and choose moves
        pokemon1.selected_move = list_moves(pokemon1)
        pokemon2.selected_move = list_moves(pokemon2)
        
        log, turn_count = execute_turn(pokemon1, pokemon2, turn_count)
        print(log)

    winner = pokemon1 if pokemon1.battle_stats['hp'] > 0 else pokemon2
    print(f"{winner.name} wins the battle!\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Handle the exception (e.g., log it, print a message, etc.)
        print(f"An error occurred: {e}")