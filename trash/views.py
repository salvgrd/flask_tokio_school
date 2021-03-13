from core import app
from flask import jsonify, request
from models import Users, Sales

@app.route('/')
def index():
    print(Users.get_by_id(1).provider.company)
    return 'Hello world!'

@app.route('/sales/place', methods = ['POST'])
def test():
    placed_sale = Sales.place(request.get_json())
    return placed_sale

@app.route('/users/authenticate', methods = ['POST'])
def log_in():
    response = 'OK!' if Users.log_in(request.get_json()) else 'KO!'
    status = 200 if response else 401
    return jsonify(response), status

@app.route('/users/register', methods = ['POST'])
def register():
    # response = 'OK!' if Users.register(request.get_json()) else 'KO!'
    response = Users.register(request.get_json())
    print(response)
    status = 200
    return jsonify(response), status