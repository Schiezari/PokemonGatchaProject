from requests_entry_point import db


class CaughtPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(50), unique=True)
    exp = db.Column(db.Integer)
    first_type = db.Column(db.String(50))
    second_type = db.Column(db.String(50))
    ability = db.Column(db.String(50))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)


