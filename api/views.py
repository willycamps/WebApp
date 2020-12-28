from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text


class Club(Resource):
    """ The Club View """

    def __init__(self):
        self.db = Db()

    def get(self):
        """ Returns a list of clubs """
        query = "SELECT * FROM club ORDER BY club_points DESC"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        clubs = self.db.clean_select_results(rows, keys)

        return {
         'clubs': clubs
            
        }

    def put(self):
        """
        Update the points of Clubs to the db 
        Expect a JSON payload with the following format
        clubs:[ {
                    'id': 1,
                    'points': "1"
                }
                ]
        """
        data = request.get_json()
        query ="UPDATE club SET club_points = :points WHERE id = :id;"
        
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False
