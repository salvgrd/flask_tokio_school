import json
from flask import Flask
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
    return 'products!'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)