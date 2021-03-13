from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('users', description='user related operations')
    user = api.model('users', {
        'access_email': fields.String(required=True, description='user email address'),
        'name': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
    })