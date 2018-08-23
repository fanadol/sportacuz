from Sportacuz import db

from SportacuzApi.models.coach import Coach

class Team(db.Model):

    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('coach.id'))
    logo = db.Column(db.String(255), nullable=False, unique=True)
    public_id = db.Column(db.String(100), unique=True)
    invite_code = db.Column(db.String(5), unique=True)
    created_at = db.Column(db.DateTime, nullable=False)
    squad = db.relationship('Athlete', backref='team', lazy=True)
    memo = db.relationship('Memo', backref='team', lazy=True)