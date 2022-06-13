from app.src.interfaces.ievent_provider import IEventProvider


class TransferCaughtPokemonController:
    def __init__(self, event_provider: IEventProvider):
        self.__event_provider = event_provider

    def transfer_caught_pokemon(self, pokemon: str):
        return self.__event_provider.send(message=pokemon)

    def transfer_caught_n_pokemon(self, pokemon_list: list):
        response = []
        for pokemon in pokemon_list:
            response.append(self.transfer_caught_pokemon(pokemon))
        return ''.join(response)
