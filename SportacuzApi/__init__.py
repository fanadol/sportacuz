from flask import Blueprint
from flask_restplus import Api

from .controllers.coach_controller import api as coach_ns
from .controllers.auth_controller import api as auth_ns
from .controllers.team_controller import api as team_ns
from .controllers.athlete_controller import api as athlete_ns
from .controllers.memo_controller import api as memo_ns

api_blueprint = Blueprint('api', __name__)

authorization = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(api_blueprint,
          doc='/doc/',
          title='SPORTACUZ API',
          description='API for SPORTACUZ',
          authorizations=authorization)

api.add_namespace(coach_ns, path='/coach')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(team_ns, path='/team')
api.add_namespace(athlete_ns, path='/athlete')
api.add_namespace(memo_ns, path='/memo')