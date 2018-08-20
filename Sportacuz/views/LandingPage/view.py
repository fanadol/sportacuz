from flask import render_template

from Sportacuz.views.LandingPage import LandingPage


@LandingPage.route('/', methods=["GET"])
def index():
    return render_template('index.html')
