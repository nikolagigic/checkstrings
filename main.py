from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from helpers import check_strings

app = Flask(__name__)
CORS(app)
api = Api(app)
parser = reqparse.RequestParser()

class ParserArguments():
    def post(self):
        parser.add_argument('string1', type=str)
        parser.add_argument('string2', type=str)
        self.args = parser.parse_args()

class CheckStringsAPI(Resource, ParserArguments):
    def post(self):
        super().post()
        string1 = self.args.get('string1', '')
        string2 = self.args.get('string2', '')

        if not string1 or not string2:
            return "Both arguments must be satisfied."

        return check_strings(string1, string2)
        
        
api.add_resource(CheckStringsAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)