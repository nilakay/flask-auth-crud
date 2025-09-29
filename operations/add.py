from flask import Blueprint, request, redirect, render_template
from utils.utils import read_yaml, convert_password
from methods import CRUDMethods
from flask_jwt_extended import jwt_required

add_blueprint = Blueprint('add', __name__)
config = read_yaml('config/config.yaml')

@add_blueprint.route('/add', methods=['GET'])
@jwt_required()
def add():
    return render_template('add.html')

@add_blueprint.route('/add', methods=['POST'])
@jwt_required()
def post():
    record_type = request.form.get('type')
    crud_methods = CRUDMethods(record_type)
    data = extract_data(record_type)
    if data:
        crud_methods.add_element(data)
        return redirect('/list?type=' + record_type)
    else:
        return "Invalid record type or data", 400
    
def extract_data(record_type):
    if record_type in config:
        record_info = config[record_type]['dict']
        record_info.pop('id', None)
        data = {key: request.form.get(key) for key in record_info.keys()}
        for key in record_info.keys():
            if key == "password":
                data["password"] = convert_password(data["password"])
        return data
    return None