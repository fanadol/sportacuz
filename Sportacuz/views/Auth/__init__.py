from flask import Blueprint

Auth = Blueprint('Auth', __name__)

from Sportacuz.views.Auth import view