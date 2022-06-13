import logging
import random

from app.src.DTO.pokemon_dto import PokemonDTO
from app.src.controllers.transform_caught_pokemon_controller import transform_caught_pokemon
from app.src.interfaces.ipokemon_provider import IPokemonProvider


class CatchPokemonController:
    def __init__(self, pokemon_provider: IPokemonProvider):
        self.__pokemon_provider = pokemon_provider

    def get_random_pokemon(self, user_id: int):
        try:
            caught_pokemon = self.__pokemon_provider.catch_pokemon(random.randint(1, 898))
            pokemon_dto = PokemonDTO(caught_pokemon)
            pokemon_json = transform_caught_pokemon(pokemon_dto, user_id)
        except Exception as ex:
            logging.error(f'error occurred while transforming json into pokemonDTO in get_random_pokemon: {ex}')
            raise ex
        return pokemon_json

    def get_n_random_pokemon(self, quantity: int, user_id: int):
        pokemon_list = []
        logging.info("starting to request from pokemon api")
        for _ in range(quantity):
            pokemon_list.append(self.get_random_pokemon(user_id))
        logging.info("pokemon api calls ended")
        return pokemon_list
