from flask import request
from flask_restplus import Resource

from SportacuzApi.utils.dto import CoachDTO
from SportacuzApi.services.coach_service import get_a_coach, get_all_coach, save_new_coach
from SportacuzApi.utils.decorator import token_required

# namespace
api = CoachDTO.api
# model
_coach = CoachDTO.coach


@api.route('/')
class CoachList(Resource):
    @api.doc('list of registered coach', security='apikey')
    @api.marshal_list_with(_coach)
    @token_required
    def get(self):
        return get_all_coach()

    @api.doc('save a new coach')
    @api.response(201, 'coach successfully registered.')
    @api.response(409, 'failed to register coach.')
    @api.expect(_coach)
    def post(self):
        data = request.get_json()
        return save_new_coach(data)


@api.route('/<public_id>')
@api.param('public_id', 'coach identifier')
@api.response(404, 'coach not found')
class Coach(Resource):
    @api.doc('get a single coach based on id', security='apikey')
    @api.marshal_with(_coach)
    @token_required
    def get(self, public_id):
        coach = get_a_coach(public_id)
        if not coach:
            api.abort(404)
        return coach

