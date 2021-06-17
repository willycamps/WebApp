from flask import Flask
from flask_cors import CORS
from flask_restful import Api
#from app import app as application
#from flask.ext.sqlalchemy import SQLAlchemy

from views import Club

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dbuser:dbpassword@db/users_db'
#db = SQLAlchemy(app)

CORS(app)
api = Api(app)
##
## Actually setup the Api resource routing here
##

api.add_resource(Club, '/clubs',methods=['POST', 'GET'])


@app.route('/')
def index():
    return '<h1> Hello World ! </h1>'

if __name__ == '__main__':
    #db.create_all()
    app.run(debug = True, host = '0.0.0.0')