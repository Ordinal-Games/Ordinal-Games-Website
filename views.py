from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route('/home')
@views.route('/')
def home():
    return render_template("index.html")

@views.route('/about')
@views.route('/team')
def team():
    return render_template("team.html")

@views.route('/software')
@views.route('/game')
@views.route('/games')
def games():
    return render_template("games.html")

@views.route('/contact')
@views.route('/contacts')
@views.route('/contact-us')
def contact():
    return render_template("contact.html")