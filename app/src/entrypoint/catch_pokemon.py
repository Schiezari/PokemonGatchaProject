from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required, current_user

from app.src.config.producer_config import ProducerConfig
from app.src.controllers.catch_pokemon_controller import CatchPokemonController
from app.src.controllers.transfer_caught_pokemon_controller import TransferCaughtPokemonController
from app.src.data_provider.call_pokemon_api import CallPokemonAPI
from app.src.data_provider.kafka_data_provider import KafkaDataProvider
from app.src.entities.caught_pokemons import CaughtPokemon

catch_pokemon = Blueprint('catch_pokemon', __name__)


@catch_pokemon.route("/list-pokemon", methods=['GET'])
@login_required
def list_pokemon_by_user():
    page = request.args.get('page', 1, type=int)
    caught_pokemon = CaughtPokemon.query.filter_by(user_id=current_user.user_id).order_by(CaughtPokemon.id).paginate(page=page, per_page=49)
    return render_template('list_pokemon.html', list_pokemon=caught_pokemon)


@catch_pokemon.route("/pokemon-detail/<pokemon_id>", methods=['GET'])
@login_required
def get_pokemon_by_id(pokemon_id):
    caught_pokemon = CaughtPokemon.query.filter_by(id=pokemon_id, user_id=current_user.user_id).first()
    if caught_pokemon:
        return render_template('pokemon_details.html', pokemon=caught_pokemon)


@catch_pokemon.route("/catch-pokemon", methods=['GET'])
@login_required
def catch_pokemon_request():
    return render_template('catch_pokemon.html')


@catch_pokemon.route("/catch-random-pokemon", methods=['GET'])
@login_required
def catch_random_pokemon():
    pokemon_use_case = CatchPokemonController(CallPokemonAPI())
    caught_pokemon = pokemon_use_case.get_random_pokemon(current_user.user_id)
    event_provider = KafkaDataProvider(ProducerConfig())
    transfer_pokemon_to_database = TransferCaughtPokemonController(event_provider)
    pokemon_payload = transfer_pokemon_to_database.transfer_caught_pokemon(caught_pokemon)
    return jsonify(pokemon_payload)


@catch_pokemon.route("/catch-n-pokemon", methods=['GET'])
def catch_n_pokemon():
    quantity = request.args.get("quantity")
    user_id = request.args.get("user_id")
    pokemon_use_case = CatchPokemonController(CallPokemonAPI())
    pokemon_list = pokemon_use_case.get_n_random_pokemon(int(quantity), int(user_id))
    event_provider = KafkaDataProvider(ProducerConfig())
    transfer_pokemon_to_database = TransferCaughtPokemonController(event_provider)
    return ''.join(transfer_pokemon_to_database.transfer_caught_n_pokemon(pokemon_list))
