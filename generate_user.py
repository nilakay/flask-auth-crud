from faker import Faker
from utils.utils import convert_password
from methods import CRUDMethods
from utils.utils import log_user_addition  

def generate_user():
    fake = Faker()
    user_dict = {"username": fake.user_name(),"email": fake.email(),
        "age": fake.random_int(min=18, max=80),"password": fake.password()}
    user_dict["password"] = convert_password(user_dict["password"])
    return user_dict

def add_user(**kwargs):
    ti = kwargs['ti']
    user_dict = ti.xcom_pull(task_ids='generate_user')
    crud_methods = CRUDMethods("users")
    crud_methods.add_element(user_dict)
    log_user_addition(user_dict['username'], user_dict['email'], user_dict['age'])