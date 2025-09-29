from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required

choose_type_blueprint = Blueprint('choose_type', __name__)

@choose_type_blueprint.route('/choose_type')
@jwt_required
def choose_type():
    return render_template('/choose_type.html')