from flask import jsonify
from .services import Enviroment

def index():
    return 'Hello, World!'

def health(enviroment: Enviroment):
    return jsonify({'env': enviroment.get_env()})