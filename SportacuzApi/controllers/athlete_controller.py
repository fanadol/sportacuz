from flask import request
from flask_restplus import Resource

from SportacuzApi.services.athlete_service import save_an_athlete, get_all_athletes, get_an_athlete
from SportacuzApi.utils.dto import AthleteDTO
from SportacuzApi.utils.decorator import token_required

api = AthleteDTO.api
_athlete = AthleteDTO.athlete


@api.route('/')
class AthleteList(Resource):
    @api.doc('list of registered athlete', security='apikey')
    @api.marshal_list_with(_athlete)
    @token_required
    def get(self):
        return get_all_athletes()

    @api.doc('register an athlete')
    @api.expect(_athlete)
    def post(self):
        data = request.get_json()
        return save_an_athlete(data)


@api.route('/<public_id>')
class Athlete(Resource):
    @api.doc('get an athlete', security='apikey')
    @api.marshal_with(_athlete)
    @token_required
    def get(self, public_id):
        return get_an_athlete(public_id)
