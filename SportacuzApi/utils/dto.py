from flask_restplus import Namespace, fields


class CoachDTO:
    api = Namespace('coach', description='coach namespace')
    coach = api.model('coach_DTO_model', {
        'email': fields.String(required=True, description='coach email address'),
        'username': fields.String(required=True, description='coach username'),
        'password': fields.String(required=True, description='coach password')
    })


class AthleteDTO:
    api = Namespace('athlete', description='athlete namespace')
    athlete = api.model('athlete_DTO_model', {
        'email': fields.String(required=True, description='athlete email'),
        'username': fields.String(required=True, description='athlete username'),
        'password': fields.String(required=True, description='athlete password'),
        'invite_code': fields.String(required=True, description='invite code for join a team'),
        'registered_on': fields.String(description='athlete date registration'),
        'jersey_number': fields.String(description='athlete jersey number')
    })


class TeamDTO:
    api = Namespace('team', description='team namespace')
    team = api.model('team_DTO_model', {
        'name': fields.String(required=True, description='team name'),
        'logo': fields.String(required=True, description='team logo'),
        'public_id': fields.String(description='team identifier'),
        'invite_code': fields.String(description='team invite code'),
        'created_at': fields.String(description='team date creation'),
        'squad': fields.Nested(AthleteDTO.athlete)
    })


class AuthDTO:
    api = Namespace('Auth', description='authentication namespace')
    auth = api.model('auth_DTO_model', {
        'email': fields.String(required=True, description='user email'),
        'password': fields.String(required=True, description='user password'),
        'role': fields.String(required=True, description='user role coach or athlete')
    })


class MemoDTO:
    api = Namespace('Memo', description='memo namespace')
    memo = api.model('memo_DTO_model', {
        'type': fields.String(required=True, description='type of the memo'),
        'duration': fields.String(required=True, description='duration of the event'),
        'date': fields.String(required=True, description='date of the event'),
        'location': fields.String(required=True, description='location of the event'),
        'coach': fields.String(description='who make the memo and become the coach'),
        'team': fields.String(required=True, description='team where the memo made')
    })
