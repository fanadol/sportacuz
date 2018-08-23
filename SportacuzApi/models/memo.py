from Sportacuz import db

from SportacuzApi.models.coach import Coach
from SportacuzApi.models.team import Team


class Memo(db.Model):
    __tablename__ = 'memo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    coach = db.Column(db.Integer, db.ForeignKey('coach.id'))
    team = db.Column(db.Integer, db.ForeignKey('team.id'))
