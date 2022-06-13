from abc import ABC, abstractmethod


class IPokemonProvider(ABC):
    @abstractmethod
    def catch_pokemon(self, pokemon_id: int):
        pass
