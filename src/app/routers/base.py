from flask import Blueprint, request
from flask_restx import Api, namespace, Namespace, Resource

router = Blueprint('configurations', __name__, 'templates')
@router.get('/')
def get_hello():
    return '<h1>Helllo, my friend</h1>'

ns = Namespace('admin')
# @ns.route('/')
# class K(Resource):
#     @ns.param('param', {'sf': 'int',
#                         'op': 12})
#     def post(self, param: dict):
#         id = request.get_json()['id']
#         return '<h1>Helllo, my friend</h1>'


