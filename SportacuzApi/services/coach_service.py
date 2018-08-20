import uuid
import datetime

from Sportacuz import db
from SportacuzApi.models.coach import Coach


def save_new_coach(data):
    try:
        coach_email = Coach.query.filter_by(email=data['email']).first()
        if not coach_email:
            new_coach = Coach(
                email=data['email'],
                username=data['username'],
                public_id=str(uuid.uuid4()),
                password=data['password'],
                registered_on=datetime.datetime.utcnow()
            )
            save_to_db(new_coach)
            response_object = {
                'status': 'success',
                'message': 'coach successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'email already used'
            }
            return response_object, 409
    except Exception as e:
        return e


def save_to_db(data):
    db.session.add(data)
    db.session.commit()


def get_all_coach():
    return Coach.query.all()


def get_a_coach(public_id):
    return Coach.query.filter_by(public_id=public_id).first()
