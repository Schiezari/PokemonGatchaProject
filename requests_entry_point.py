import urllib
from datetime import timedelta

from flask import Flask, session
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(filename)s:%(lineno)s - %(funcName)s %(message)s',
                    filename=r'C:\Users\leoem\Logs\pokemon_api\log_pokemon.log')
db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'askdfsakbasdfhoahsdsdf'
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=localhost;DATABASE=MyPokemons;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.needs_refresh_message = u"Session timedout, please re-login"
login_manager.needs_refresh_message_category = "info"
login_manager.init_app(app)
from app.authentication.users import Users


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return Users.query.get(int(user_id))


from app.src.entrypoint.catch_pokemon import catch_pokemon

app.register_blueprint(catch_pokemon)
from app.authentication.main import main

app.register_blueprint(main)
from app.authentication.auth import auth

app.register_blueprint(auth)


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
