from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from Sportacuz.config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    from Sportacuz.views.LandingPage import LandingPage as landingpage_bp
    app.register_blueprint(landingpage_bp, url_prefix='/')

    from Sportacuz.views.Auth import Auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from Sportacuz.views.Dashboard import Dashboard as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    from Sportacuz.views.Team import Team as team_bp
    app.register_blueprint(team_bp, url_prefix='/team')

    from SportacuzApi import api_blueprint as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
