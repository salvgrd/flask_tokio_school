from flask import Flask
import os
import json

basedir = os.getcwd()

dbURI = 'mysql://USERNAME:PASSWORD@HOST:PORT/DATABASE'

with open(f"{basedir}\core\dbconfig.json") as f:
  dbconfig = json.load(f)

for key, value in dbconfig.items():
    dbURI = dbURI.replace(key, value)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import views