import datetime
import uuid

from Sportacuz import db
from SportacuzApi.models.athlete import Athlete
from SportacuzApi.models.team import Team


def save_an_athlete(data):
    email = Athlete.query.filter_by(email=data['email']).first()
    if not email:
        team = Team.query.filter_by(invite_code=data['invite_code']).first()
        if team:
            new_athlete = Athlete(
                email=data['email'],
                username=data['username'],
                registered_on=datetime.datetime.utcnow(),
                public_id=str(uuid.uuid4()),
                password=data['password'],
                # pass an object here for foreign key
                team=team
            )
            save_to_db(new_athlete)
            response_object = {
                'status': 'success',
                'message': 'Athlete successfully registered'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'provide a valid invite code'
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'email already used. please use another email.'
        }
        return response_object, 409


def save_to_db(data):
    db.session.add(data)
    db.session.commit()


def get_an_athlete(public_id):
    return Athlete.query.filter_by(public_id=public_id).first()


def get_all_athletes():
    return Athlete.query.all()
