from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta
from utils.utils import read_yaml
from auth import auth_blueprint
from operations.index import index_blueprint
from operations.add import add_blueprint
from operations.choose_type import choose_type_blueprint
from operations.update import update_blueprint
from operations.delete import delete_blueprint
from operations.filter import filter_blueprint
from operations.list import list_blueprint
import os

config = read_yaml('config/config.yaml')

app = Flask(__name__)
expires_at_midnight = datetime.combine(datetime.utcnow().date() + timedelta(days=1), datetime.min.time())
app.config['JWT_SECRET_KEY'] = config["jwt_secret_key"]
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=20)
jwt = JWTManager(app)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
print(root)
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)

app.register_blueprint(auth_blueprint, url_prefix='/') 
app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(add_blueprint, url_prefix='/')
app.register_blueprint(choose_type_blueprint, url_prefix='/')
app.register_blueprint(update_blueprint, url_prefix='/')
app.register_blueprint(delete_blueprint, url_prefix='/')
app.register_blueprint(filter_blueprint, url_prefix='/')
app.register_blueprint(list_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
