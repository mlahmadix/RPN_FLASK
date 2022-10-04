import operator
import uuid
from flask import Flask
from flask_restplus import Resource, fields, Namespace

app = Flask(__name__)
api = Namespace('rpn', description='RPN Api')

stack = api.model('Stack', {
    'value': fields.Float(required=True, description='a stack value'),
})

STACKS = {}
OPS = {'"+"': operator.add,
       '"-"': operator.sub,
       '"*"': operator.mul,
       '"/"': operator.truediv
       }


@api.route('/rpn/stack/<stack_id>')
@api.response(404, 'Stack not found')
class Stack(Resource):
    @api.doc('get a stack', responses={200: 'Success'})
    def get(self, stack_id):
        """Get a stack"""
        if stack_id not in STACKS:
            api.abort(404, message="stack not found")
        else:
            return STACKS.get(stack_id, [])

    @api.doc('Delete a stack', responses={204: 'Success'})
    def delete(self, stack_id):
        """Delete a stack"""
        if stack_id not in STACKS:
            api.abort(404, message="stack not found")
        else:
            del STACKS[stack_id]
        return '', 204

    @api.doc('Push a new value to a stuck', responses={200: 'Success'})
    @api.expect(stack)
    def post(self, stack_id):
        """Push  to a stack"""
        if stack_id not in STACKS:
            api.abort(404)
        else:
            STACKS[stack_id].append(api.payload.get("value"))
        return STACKS[stack_id]


@api.route('/rpn/stack')
class StackList(Resource):
    @api.doc('get all stacks', responses={200: 'Success'})
    def get(self):
        """List the available stacks"""
        return STACKS

    @api.doc('Create a new stack', responses={201: 'Created'})
    def post(self):
        """Create a new stack"""
        stack_id = str(uuid.uuid1())
        STACKS[stack_id] = []
        return {stack_id: STACKS[stack_id]}, 201


@api.route('/rpn/op')
class OpList(Resource):
    @api.doc('List all operators', responses={200: 'Success'})
    def get(self):
        """List operators"""
        return {"operators": list(OPS.keys())}


@api.route('/rpn/op/<path:op>/stack/<stack_id>')
@api.param("op", enum=list(OPS.keys()))
@api.response(404, 'not found')
@api.response(400, 'user error')
class ApplyOperator(Resource):
    @api.doc('Apply an operator to a stack', responses={200: 'Success'})
    def post(self, op, stack_id):
        """Apply an operator to a stack"""
        if op not in OPS or stack_id not in STACKS:
            api.abort(404,
                      message='not found, please check operator or stack_id')
        elif len(STACKS[stack_id]) < 2:
            api.abort(400, message="stack contain less than two values")
        else:
            el1 = STACKS[stack_id].pop()
            el2 = STACKS[stack_id].pop()
            STACKS[stack_id].append(OPS[op](el2, el1))
        return STACKS[stack_id]
