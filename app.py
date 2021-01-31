import json
from flask import Flask, jsonify
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
    keys =  [i[0] for i in c.description]
    products = []
    for p in c.fetchall():
        product = {
            keys[0]: p[0],
            keys[1]: p[1],
            keys[2]: p[2],
            keys[3]: p[3],
            keys[4]: p[4],
            keys[5]: p[5],
            keys[6]: p[6],
            keys[7]: p[7]
        }
        products.append(product)
    return jsonify(products)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)