import random

from app.src.DTO.pokemon_dto import PokemonDTO


class PokemonClass:
    def __init__(self, pokemon_dto: PokemonDTO):
        self.name = pokemon_dto.pokemon_name
        self.id = pokemon_dto.pokemon_id
        self.exp = pokemon_dto.pokemon_exp
        self.height = pokemon_dto.pokemon_height
        self.weight = pokemon_dto.pokemon_weight
        self.abilities = [Ability(pokemon_ability) for pokemon_ability in pokemon_dto.pokemon_abilities]
        self.types = [Type(pokemon_type) for pokemon_type in pokemon_dto.pokemon_types]


class Ability:
    def __init__(self, ability_name: str):
        self.name = ability_name


class Type:
    def __init__(self, type_name: str):
        self.name = type_name
