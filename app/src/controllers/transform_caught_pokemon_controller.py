import json
import logging

from app.src.DTO.pokemon_dto import PokemonDTO
from app.src.DTO.pokemon_to_transfer_dto import PokemonToTransferDTO
from app.src.entities.pokemon_entitie import PokemonClass


def transform_caught_pokemon(pokemon_to_transfer: PokemonDTO, user_id: int):
    try:
        pokemon = PokemonClass(pokemon_to_transfer)
        pokemon_to_transfer_dto = PokemonToTransferDTO(pokemon, user_id)
    except Exception as ex:
        logging.error(f'error occurred while in transform_caught_pokemon: {ex}')
        raise ex
    return json.dumps(pokemon_to_transfer_dto.__dict__)

