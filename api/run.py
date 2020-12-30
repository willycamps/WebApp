from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from views import Club
from flask import jsonify, request

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Club, '/clubs')

#incomes = [
#  { 'description': 'salary', 'amount': 5000 }
#]


#@app.route('/incomes')
#def get_incomes():
#  return jsonify(incomes)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

#if __name__ == "__main__":
    #app.run()
