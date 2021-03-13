import uuid
import datetime

from app.main import db
from app.main.models import models

Users = models.Users # to refactor

def register_new_user(data):
    user = user = Users.query.filter_by(email=data['access_email']).first()
    if not user:
        new_user = Users(
            name=data['name'], 
            access_email=data['access_email'], 
            password=data['password'], 
            type=data['type']
        )
        response = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'User already exists.'
        }
        return response, 409

def get_all_users(data):
    return Users.query.all()

def get_user_by_email(name):
    return Users.query.filter_by(name=name).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()