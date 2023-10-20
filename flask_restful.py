from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Example(Resource):
    def get(self):
        # Handle GET request
        return {'message': 'GET request received'}

    def post(self):
        # Handle POST request
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=str, required=True)
        args = parser.parse_args()
        # Process the data here
        result = {'message': 'POST request received', 'data': args['data']}
        return result, 201

api.add_resource(Example, '/api')

if __name__ == '__main__':
    app.run(debug=True)