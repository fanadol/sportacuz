from Sportacuz import db
from SportacuzApi.models.blacklist import BlacklistToken


def save_token(token):
    blacklist_token = BlacklistToken(token)
    # insert the token
    try:
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 401
