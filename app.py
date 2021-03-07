from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, dbURI, Products, Users, Sales

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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

# @app.route('/products')
# def get_products():
#     # Add pagination
#     c = mysql.connection.cursor()
#     c.execute('SELECT * FROM products')
#     products = c.fetchall()
#     return jsonify(products)

# @app.route('/products/add', methods = ['POST'])
# def add_product():
#     connection = mysql.connection
#     query = 'INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
#     c = connection.cursor()

#     data = [ None ]
#     for key in request.form:
#         data.append(request.form[key])

#     c.execute(query, data)
#     connection.commit()

#     return jsonify({ "message": f"Product '{request.form['name']}' created successfully" })

# @app.route('/providers')
# def get_providers():
#     c = mysql.connection.cursor()
#     c.execute('SELECT * FROM providers')
#     providers = c.fetchall()
#     return jsonify(providers)

# @app.route('/users/<user_id>')
# def get_user(user_id):
#     c = mysql.connection.cursor()
#     c.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
#     user = c.fetchone()
#     return jsonify(user)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)