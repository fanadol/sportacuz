from SportacuzApi.models.athlete import Athlete
from SportacuzApi.models.coach import Coach
from SportacuzApi.services.blacklist_service import save_token
from SportacuzApi.models.token import encode_auth_token, decode_auth_token


class Auth:
    @staticmethod
    def login_user(data):
        try:
            role = data['role']
            if role == 'coach':
                obj = Coach()
            else:
                obj = Athlete()
            user = obj.query.filter_by(email=data['email']).first()
            if user and user.check_password(data['password']):
                auth_token = encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in',
                        'Authorization': auth_token.decode(),
                        'Role': role
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Email or Password doesnt match'
                }
                return response_object, 401
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'something went wrong, try again.'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data
        else:
            auth_token = ""
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return save_token(auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'messsage': 'please provide a valid token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization')
        role = new_request.headers.get('Role')
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                if role == 'coach':
                    obj = Coach()
                else:
                    obj = Athlete()
                user = obj.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_pid': user.public_id,
                        'email': user.email,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid Auth token.'
            }
            return response_object, 401
