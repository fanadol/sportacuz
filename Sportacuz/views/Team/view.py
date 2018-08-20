import requests
from flask import render_template, session

from . import Team


@Team.route('/<public_id>/manage')
def team_manage(public_id):
    url = 'http://localhost:5000/api/team/{}'.format(public_id)
    header = {
        'Authorization': session.get('Authorization'),
        'Role': session.get('Role')
    }
    r = requests.get(url, headers=header)
    team_json = r.json()
    return render_template('team_manage.html', team=team_json)