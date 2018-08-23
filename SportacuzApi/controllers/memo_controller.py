from flask import request
from flask_restplus import Resource

from SportacuzApi.services.memo_service import get_a_memo, save_a_memo
from SportacuzApi.utils.dto import MemoDTO
from SportacuzApi.utils.decorator import token_required

api = MemoDTO.api
_memo = MemoDTO.memo


@api.route('/')
class Memo(Resource):
    @api.doc('create new memo', security='apikey')
    @api.expect(_memo)
    @token_required
    def post(self):
        token = request.headers.get('Authorization')
        data = request.get_json()
        return save_a_memo(data, token)


@api.route('/<team_id>')
@api.param('team_id', 'team identifier')
class TeamMemo(Resource):
    @api.doc('list of memo from a team', security='apikey')
    @api.marshal_with(_memo)
    @token_required
    def get(self, public_id):
        return get_a_memo(public_id)
