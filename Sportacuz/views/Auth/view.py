from Sportacuz.views.Auth import Auth

from flask import render_template, request, redirect, flash, url_for, make_response, session
import requests


@Auth.route('/register/role', methods=["GET"])
def register_role():
    return render_template('register_role.html')


@Auth.route('/register/coach', methods=["GET", "POST"])
def register_coach():
    if request.method == "POST":
        url = 'http://localhost:5000/api/coach/'
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        payload = {
            'email': email,
            'password': password,
            'username': username
        }
        resp = requests.post(url, json=payload)
        if resp.status_code == 201:
            flash('Coach successfully registered. Please Login', 'success')
            return redirect(url_for('LandingPage.index'))
        elif resp.status_code == 409:
            flash('Email already used. Try Again.', 'danger')
            return redirect(url_for('Auth.register_coach'))
        else:
            flash('Something went wrong. Try Again.', 'danger')
            return redirect(url_for('Auth.register_coach'))
    return render_template('register_coach.html')


@Auth.route('/register/athlete', methods=["GET", "POST"])
def register_athlete():
    if request.method == "POST":
        url = 'http://localhost:5000/api/athlete/'
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        invite_code = request.form.get('invite_code')
        payload = {
            'email': email,
            'username': username,
            'password': password,
            'invite_code': invite_code
        }
        r = requests.post(url, json=payload)
        print(r.status_code)
        if r.status_code == 201:
            flash('Registration success, please login', 'success')
            return redirect(url_for('LandingPage.index'))
        elif r.status_code == 409:
            flash('Email already used. Please use another email address or input proper invite code.', 'danger')
            return redirect(url_for('Auth.register_athlete'))
        else:
            flash('Something went wrong, please try again.', 'danger')
            return redirect(url_for('Auth.register_athlete'))
    return render_template('register_athlete.html')


@Auth.route('/login', methods=["GET", "POST"])
def login():
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
            return redirect(url_for('Auth.login'))
    return render_template('login.html')


@Auth.route('/logout')
def logout():
    url = 'http://localhost:5000/api/auth/logout'
    token = session.get('Authorization')
    header = {'Authorization': token}
    r = requests.post(url, headers=header)
    if r.status_code == 200:
        session.pop('Authorization', None)
        session.pop('Role', None)
        flash('logout success.', 'success')
        return redirect(url_for('LandingPage.index'))
    else:
        print(r.status_code)
        flash('Something Went Wrong', 'danger')
        return redirect(url_for('LandingPage.index'))