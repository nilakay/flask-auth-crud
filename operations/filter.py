
from flask import Blueprint, request, render_template, jsonify
from methods import CRUDMethods
from flask_jwt_extended import jwt_required

filter_blueprint = Blueprint('filter', __name__)

@filter_blueprint.route('/filter', methods=['GET', 'POST'])
@jwt_required()
def filter_records():
    if request.method == 'GET':
        return render_template('filter.html')
    else:
        data = request.get_json()
        element_type = data.get('type')
        key = data.get('key')
        value = data.get('value')

        if not all([element_type, key, value]):
            return jsonify({"error": "Missing required fields"}), 400

        crud_methods = CRUDMethods(element_type)
        results = crud_methods.filter(key, value)
        return jsonify(results), 200