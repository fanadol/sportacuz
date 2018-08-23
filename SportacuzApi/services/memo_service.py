from Sportacuz import db
from SportacuzApi.models.memo import Memo
from SportacuzApi.models.team import Team
from SportacuzApi.models.coach import Coach
from SportacuzApi.models.token import decode_auth_token


def save_a_memo(data, token):
    try:
        coach_id = decode_auth_token(token)
        team = Team.query.filter_by(public_id=data['team']).first()
        coach = Coach.query.filter_by(id=coach_id).first()
        new_memo = Memo(
            type = data['type'],
            duration = data['duration'],
            date = data['date'],
            location = data['location'],
            coach = coach,
            team = team
        )
        save_to_db(new_memo)
        response_object = {
            'status': 'success',
            'message': 'memo successfully created'
        }
        return response_object, 201
    except Exception as e:
        return e


def save_to_db(data):
    db.session.add(data)
    db.session.commit()


def get_a_memo(team_id):
    return Memo.query.filter_by(team=team_id).all()