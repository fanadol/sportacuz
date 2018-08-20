from flask import request
from flask_restplus import Resource

from SportacuzApi.utils.dto import TeamDTO
from SportacuzApi.services.team_service import get_a_team, get_all_team, save_new_team, get_owned_team
from SportacuzApi.utils.decorator import token_required

api = TeamDTO.api
_team = TeamDTO.team


@api.route('/')
class TeamList(Resource):
    @api.doc('list of created teams', security='apikey')
    @api.marshal_list_with(_team)
    @token_required
    def get(self):
        return get_all_team()

    @api.response(201, 'team successfully created')
    @api.response(409, 'failed to create team')
    @api.doc('create a new team', security='apikey')
    @api.expect(_team)
    @token_required
    def post(self):
        token = request.headers.get('Authorization')
        data = request.get_json()
        return save_new_team(data, token)


@api.route('/<public_id>')
class Team(Resource):
    @api.response(404, 'team not found')
    @api.marshal_with(_team)
    @token_required
    def get(self, public_id):
        team = get_a_team(public_id)
        if not team:
            api.abort(404)
        return team


@api.route('/owned')
class TeamOwned(Resource):
    @api.doc('List of created teams by a coach', security='apikey')
    @api.marshal_list_with(_team)
    @token_required
    def get(self):
        token = request.headers.get('Authorization')
        return get_owned_team(token)
