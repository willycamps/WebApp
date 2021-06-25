
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import time
import datetime

app = Flask(__name__) 

app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://dbuser:dbpassword@172.23.0.3:3306/clubs_db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

class Users(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50))  
    name = db.Column(db.String(50))
    password = db.Column(db.String(150))
    admin = db.Column(db.Boolean)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expires_in=600):
      return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
        except:
            return
        return Users.query.get(data['id'])

class Club(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    club = db.Column(db.String(50))  
    club_country = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.date)
    updated = db.Column(db.DateTime)
    
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(50))  
    date = db.Column(db.DateTime)




