from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>please login</p>" 

@auth.route('/sign-up')
def sign_up():
    return "<p>please sign up</p>"

@auth.route('/logout')
def logout():
    return "<h1>please log out</h1>" 
