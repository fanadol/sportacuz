from flask import request
from flask_restplus import Resource

from SportacuzApi.services.auth_service import Auth
from SportacuzApi.utils.dto import AuthDTO

api = AuthDTO.api
_auth = AuthDTO.auth


@api.route('/login')
class UserLogin(Resource):
    @api.doc('user authentication for coach and athlete')
    @api.expect(_auth)
    def post(self):
        data = request.get_json()
        return Auth.login_user(data)


@api.route('/logout')
class UserLogout(Resource):
    @api.doc('user logout for coach and athlete')
    def post(self):
        data = request.headers.get('Authorization')
        return Auth.logout_user(data)
