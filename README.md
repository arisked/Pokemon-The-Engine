# Pokémon Battle Engine
This project implements a Pokémon battle engine in Python, simulating battles between Pokémon based on Generation I Pokémons and moves with some additional features.

# Features
- Turn-based battle system
- Pokémon with stats, levels, and types
- Move system with various effects
- Status conditions (e.g., sleep, paralysis, burn)
- Stat stage changes
- Type effectiveness calculations
- Critical hit system
- Random elements for realistic battle outcomes

# Main Components
## pokemon_models.py
Contains the core classes:

Pokemon: Represents a Pokémon with its stats, moves, and battle-related attributes.
Move: Represents a Pokémon move with its properties and effects.

## pokemon_loader.py
Handles loading Pokémon and move data from an Excel file:

load_pokemon_data: Loads basic Pokémon data.
load_move_data: Loads move data.
link_pokemon_moves: Associates moves with Pokémon.
load_pokemon_list: Combines the above functions to create a list of battle-ready Pokémon.

## battle_engine.py
Implements the battle logic:

execute_turn: Handles the logic for a single turn in the battle.
execute_move: Applies the effects of a move.
Various effect handlers for different move types and status conditions.
Damage calculation and type effectiveness logic.

# Usage
To run a sample battle:

1. Ensure you have the required dependencies installed (pandas, openpyxl, etc).
2. Edit def main() on main.py to specify the current pokemon.xlsx location.
```
def main():
    pokemons = load_pokemon_list(---pokemon.xlsx location---)
...
```
3. Run the main.py.

# Future Improvements
- Add support for more complex battle mechanics (e.g., weather effects, abilities, Pokémon nature, etc).

# License and Copyright
The software is licensed under the MIT license. See the LICENSE file for full copyright and license text. The short version is that you can do what you like with the code, as long as you say where you got it.

This repository includes data extracted from the Pokémon series of video games. All of it is the intellectual property of Nintendo, Creatures, inc., and GAME FREAK, inc. and is protected by various copyrights and trademarks. The author believes that the use of this intellectual property for a fan reference is covered by fair use — the use is inherently educational, and the software would be severely impaired without the copyrighted material.

That said, any use of this library and its included data is at your own legal risk.
