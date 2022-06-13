import logging

import requests

from app.src.interfaces.ipokemon_provider import IPokemonProvider


class CallPokemonAPI(IPokemonProvider):
    def __init__(self):
        self.__pokemon_api_url = 'https://pokeapi.co/api/v2/pokemon/'

    def catch_pokemon(self, pokemon_id: int):
        try:
            for _ in range(3):
                response = requests.get(f"{self.__pokemon_api_url}{pokemon_id}")
                if response.status_code == 200:
                    break
                logging.warning(f'error occurred while calling pokemon api: {response.text}')
            return response.json()
        except Exception as ex:
            logging.warning(f'error : {ex}')
            raise ex
