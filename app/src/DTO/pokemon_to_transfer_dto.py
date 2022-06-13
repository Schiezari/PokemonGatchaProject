import random
from app.src.entities.pokemon_entitie import PokemonClass


class PokemonToTransferDTO:
    def __init__(self, pokemon_to_transfer: PokemonClass, user_id: int):
        self.id = pokemon_to_transfer.id
        self.user_id = user_id
        self.name = pokemon_to_transfer.name
        self.exp = pokemon_to_transfer.exp
        self.types = [pokemon_type.name for pokemon_type in pokemon_to_transfer.types]
        self.ability = pokemon_to_transfer.abilities[random.randint(0, len(pokemon_to_transfer.abilities) - 1)].name
        self.height = pokemon_to_transfer.height
        self.weight = pokemon_to_transfer.weight
