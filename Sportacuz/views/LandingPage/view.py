import requests
from flask import render_template, request, flash, session, redirect, url_for

from Sportacuz.views.LandingPage import LandingPage


@LandingPage.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = 'http://localhost:5000/api/auth/login'
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        payload = {
            'email': email,
            'password': password,
            'role': role
        }
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            reqjson = r.json()
            session['Authorization'] = reqjson['Authorization']
            session['Role'] = reqjson['Role']
            flash('Login success', 'success')
            if reqjson['Role'] == 'coach':
                return redirect(url_for('Dashboard.dashboard_coach'))
            else:
                return redirect(url_for('Dashboard.dashboard_athlete'))
        else:
            flash('Login failed, please check your email, password and role', 'danger')
            return redirect(url_for('Landingpage.index'))
    return render_template('index.html')
