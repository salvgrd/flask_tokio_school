import json
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

with open('./dbconfig.json') as f:
  dbconfig = json.load(f)

for key, value in dbconfig.items():
    app.config[key] = value

mysql = MySQL(app)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/products')
def get_products():
    # Add pagination
    c = mysql.connection.cursor()
    c.execute('SELECT * FROM products')
    products = c.fetchall()
    return jsonify(products)

@app.route('/products/add', methods = ['POST'])
def add_product():
    connection = mysql.connection
    query = 'INSERT INTO products VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    c = connection.cursor()

    data = [ None ]
    for key in request.form:
        data.append(request.form[key])

    c.execute(query, data)
    connection.commit()

    return jsonify({ "message": f"Product '{request.form['name']}' created successfully" })

@app.route('/providers')
def get_providers():
    c = mysql.connection.cursor()
    c.execute('SELECT * FROM providers')
    providers = c.fetchall()
    return jsonify(providers)

@app.route('/users/<user_id>')
def get_user(user_id):
    c = mysql.connection.cursor()
    c.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    user = c.fetchone()
    return jsonify(user)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)