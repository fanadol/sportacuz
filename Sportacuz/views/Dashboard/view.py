from . import Dashboard
from Sportacuz.config import Config

import requests
import datetime
import time
import os
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


@Dashboard.route('/coh', methods=["GET", "POST"])
def dashboard_coach():
    url = 'http://localhost:5000/api/team/owned'
    header = {
        'Authorization': session.get('Authorization'),
        'Role': session.get('Role')
    }
    r = requests.get(url, headers=header)
    return render_template('dashboard_coach.html', teams=r.json())


@Dashboard.route('/ath', methods=["GET", "POST"])
def dashboard_athlete():
    return render_template('dashboard_athlete.html')


@Dashboard.route('/new-team', methods=["GET", "POST"])
def create_team():
    if request.method == "POST":
        url = 'http://localhost:5000/api/team/'
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('Please provide a logo')
            return redirect(url_for('Dashboard.create_team'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(url_for('Dashboard.create_team'))
        if file and allowed_file(file.filename):
            timestr = time.strftime("%Y%m%d-%H%M%S")
            sf = secure_filename(file.filename)
            name = sf.rsplit('.', 1)[0]
            extension = sf.rsplit('.')[1]
            pattern = name + "_" + timestr
            filename = pattern + "." + extension
            name = request.form.get('name')
            payload = {
                'name': name,
                'logo': filename
            }
            header = {
                'Authorization': session.get('Authorization'),
                'Role': session.get('Role')
            }
            r = requests.post(url, json=payload, headers=header)
            print(os.path.dirname(os.path.abspath(__file__)))
            if r.status_code == 201:
                file.save(os.path.join(Config.UPLOAD_FOLDER, "static", "uploads", filename))
                flash('Team successfully created', 'success')
                return redirect(url_for('Dashboard.dashboard_coach'))
            else:
                flash('Something went wrong, try again', 'danger')
                return redirect(url_for('Dashboard.create_team'))
    return render_template('create_team.html')
