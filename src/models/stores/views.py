from flask import Blueprint

store_blueprint = Blueprint('stores', __name__)

@store_blueprint.route('/')
def index():
    return "To jest index sklepów"

@store_blueprint.route('/store/<string:name>')
def store_page():
    pass

