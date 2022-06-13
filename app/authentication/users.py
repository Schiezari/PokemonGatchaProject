from requests_entry_point import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    nick_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

    def get_id(self):
        return self.user_id
