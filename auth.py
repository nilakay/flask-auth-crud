from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
from utils.db_utils import get_db_connection
from utils.utils import read_yaml, get_logger, get_error_logger
import bcrypt, copy

auth_logger = get_logger()
auth_error_logger = get_error_logger()
user_activity_logger = get_logger("user_activity")
config = read_yaml('config/config.yaml')
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                email = data.get('email')
                password = data.get('password')
            else:
                email = request.form.get('email')
                password = request.form.get('password')

            user_activity_logger.info(f"Login attempt for email: {email}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(copy.deepcopy(config["auth_query"]), (email,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            access_token = create_access_token(identity=email)
            user_activity_logger.info(f"Successful login for email: {email}")
            return jsonify(access_token=access_token), 200
        else:
            user_activity_logger.warning(f"Invalid login attempt for email: {email}")
            return jsonify({"msg": "Invalid email or password"}), 401
    
    except Exception as e:
        print(email,password)
        auth_error_logger.error(f"Login failed for email: {email}, Error: {e}")
        return jsonify({"msg": "Login failed"}), 500
