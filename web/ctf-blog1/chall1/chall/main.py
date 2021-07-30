from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template("index.html", user=current_user)


@main.route('/about')
def about():
    return render_template("about.html", user=current_user)


@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@main.route('/part1')
def part1():
    return render_template("part1.html", user=current_user)


@main.route('/part2')
def part2():
    return render_template("part2.html", user=current_user)


@main.route('/part3')
def part3():
    return render_template("part3.html", user=current_user)


@main.route('/part4')
@login_required
def part4():
    return render_template("part4.html", user=current_user)
