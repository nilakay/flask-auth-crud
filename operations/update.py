
from flask import Blueprint, request, render_template
from utils.utils import convert_password
from methods import CRUDMethods
from flask_jwt_extended import jwt_required

update_blueprint = Blueprint('update', __name__)

@update_blueprint.route('/update', methods=['GET', 'POST'])
@jwt_required()
def update_record():
    element_type = request.args.get('type')
    record_id = request.args.get('id')
    if request.method == 'GET':
        return render_template('update.html', type=element_type, id=record_id)
    else:
        record_data = request.get_json()
        record_id = record_data.pop('id', None)
        element_type = record_data.pop('type', None)
        
        if not record_id or not element_type:
            return "Missing record ID or type", 400
        
        if "password" in record_data.keys():
            record_data["password"] = convert_password(record_data["password"])
        crud_methods = CRUDMethods(element_type)
        crud_methods.update(record_id, record_data)
        
        return "Record updated successfully", 200

