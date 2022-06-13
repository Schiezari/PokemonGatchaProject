class PokemonDTO:
    def __init__(self, payload: dict):
        self.pokemon_name = payload['name']
        self.pokemon_id = payload['id']
        self.pokemon_height = payload['height']
        self.pokemon_weight = payload['weight']
        self.pokemon_abilities = [ability['ability']['name'] for ability in payload['abilities']]
        self.pokemon_types = [types['type']['name'] for types in payload['types']]
        self.pokemon_exp = payload['base_experience']
