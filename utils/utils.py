import bcrypt, yaml, logging
from datetime import datetime

def read_yaml(file_name):
    try:
        with open(file_name, "r") as f:
                config = yaml.safe_load(f)
        return config
    except Exception as e:
         print("Error found while reading YAML file\n", e)
         
def convert_password(password):
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt(rounds=15)
    password = bcrypt.hashpw(password, salt)
    return password.decode('utf-8')

def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False 
    return logger

def get_logger(name="general"):
    logger = name + '_logger'
    return setup_logger(logger, '/Users/nilakay/Desktop/flask2_checkpoint4/logs/' + name + '.log')

def get_error_logger(name="error"):
    logger = name + '_logger'
    return setup_logger(logger, '/Users/nilakay/Desktop/flask2_checkpoint4/logs/' + name + '.log', level=logging.ERROR)

def log_user_addition(username, email, age):
    today = datetime.now().strftime('%Y-%m-%d')
    log_file_path = f'/Users/nilakay/Desktop/flask2_checkpoint4/logs/users_added_{today}.log'
    user_add_logger = setup_logger('user_addition', log_file_path)
    user_add_logger.info(f'User added: Username={username}, Email={email}, Age={age}')
