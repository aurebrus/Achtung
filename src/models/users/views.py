from flask import Blueprint

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login')
def login_user():
    pass

@user_blueprint.route('/register')
def register_user():
    pass

@user_blueprint.route('/alerts')
def user_alert():
    pass

@user_blueprint.route('/alogout')
def logout_user():
    pass