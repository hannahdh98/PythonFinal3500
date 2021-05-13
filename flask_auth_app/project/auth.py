from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db

auth = Blueprint('auth', __name__)


# route to login
@auth.route('/login')
def login():
    return render_template('login.html')


# route login and post user information to database
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the password is wrong or if the user's login details arent right then it will reload the page.
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


# signup page
@auth.route('/signup')
def signup():
    return render_template('signup.html')


# This will redirect to the signup page
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    # This will redirect to the signup page
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    # This will create new user and hash password
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    #This will add a new user to database
    db.session.add(new_user)
    db.session.commit()

    #This will validate and add the user to the database
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
