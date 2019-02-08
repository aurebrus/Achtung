from flask import Blueprint

alert_blueprint = Blueprint('alerts', __name__)

@alert_blueprint.route('/new', methods = ['POST'])
def create_alert():
    pass


@alert_blueprint.route('deactivate/<string:alert_id>')
def deactivate_alert():
    pass

