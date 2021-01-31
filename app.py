from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/products')
def get_products():
    return 'products!'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)