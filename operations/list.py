from flask import Blueprint, request, redirect, render_template
from methods import CRUDMethods

list_blueprint = Blueprint('list', __name__)

@list_blueprint.route('/list', methods=['GET'])
def list_elements():
    element_type = request.args.get('type')
    if element_type not in ['users', 'item']:
        return redirect('/choose_type')
    element_type = request.args.get('type')
    crud_methods = CRUDMethods(element_type)
    elements = crud_methods.get_all_elements()
    return render_template('list.html', elements=elements, choice=element_type)
