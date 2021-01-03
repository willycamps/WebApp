from flask import Flask
from flask_cors import CORS
from flask_restful import Api,reqparse
from views import Club
from flask import jsonify, request


from db import Db

from sqlalchemy import text as sql_text


app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Club, '/clubs',methods=['POST', 'GET'])


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

