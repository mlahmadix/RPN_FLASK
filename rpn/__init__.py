from flask_restplus import Api
from .namespace import api as ns


api = Api(
    title='Rpn Api',
    version='1.0',
    description='Rpn Api',
)

api.add_namespace(ns)
