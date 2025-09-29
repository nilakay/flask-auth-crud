from flask import Blueprint, request, redirect, render_template
from methods import CRUDMethods
from flask_jwt_extended import jwt_required

delete_blueprint = Blueprint('delete', __name__)

@delete_blueprint.route('/delete', methods=['DELETE', 'GET'])
@jwt_required()
def delete_record():
    print(request.method)
    if request.method=="GET":
        redirect('delete.html')
    else:
        element_type = request.get_json()["typee"]
        record_id = request.get_json()["recordId"]
        crud_methods = CRUDMethods(element_type)
        crud_methods.delete(record_id)
    return render_template('delete.html')