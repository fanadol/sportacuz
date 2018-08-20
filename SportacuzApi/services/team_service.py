import uuid
import datetime
import random
import string

from SportacuzApi.models.team import Team
from SportacuzApi.models.coach import Coach
from SportacuzApi.models.token import decode_auth_token
from Sportacuz import db


def save_new_team(data, token):
    try:
        coach_id = decode_auth_token(token)
        coach = Coach.query.filter_by(id=coach_id).first()
        if coach:
            new_team = Team(
                name=data['name'],
                # pass an object here for foreign key
                coach=coach,
                logo=data['logo'],
                public_id=str(uuid.uuid4()),
                invite_code=''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
                created_at=datetime.datetime.utcnow()
            )
            save_to_db(new_team)
            response_object = {
                'status': 'success',
                'message': 'team successfully created'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'invalid owner id, please login as coach'
            }
            return response_object, 401
    except Exception as e:
        return e


def save_to_db(data):
    db.session.add(data)
    db.session.commit()


def get_all_team():
    return Team.query.all()


def get_a_team(public_id):
    return Team.query.filter_by(public_id=public_id).first()


def get_owned_team(token):
    owner_id = decode_auth_token(token)
    return Team.query.filter_by(owner_id=owner_id).all()
