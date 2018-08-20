from Sportacuz import db, flask_bcrypt

from SportacuzApi.models.team import Team


class Athlete(db.Model):
    """
    Athlete model in the database
    """

    __tablename__ = "athlete"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    public_id = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    password_hash = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20)),
    jersey_number = db.Column(db.Integer)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "Coach {}".format(self.username)
