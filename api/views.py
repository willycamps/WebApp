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
        query = "SELECT club.id, club.club, club.club_country, SUM(club_match.points) as club_points FROM club INNER JOIN club_match ON club.id = club_match.idclub GROUP BY club.id, club.club, club.club_country ORDER BY SUM(club_match.points) DESC "
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        clubs = self.db.clean_select_results(rows, keys)

        return {
         'clubs': clubs
        }

    def post(self):
        """
        Add the matches to the db 
        Expect a JSON payload with the following format
        {
            "id1":1,
            "point1":0,
            "id2":2,
            "point2":3
        }
        """
        
        data = request.get_json()
        cursor = self.db._connection.cursor()
        args = [data["id1"],data["point1"],data["id2"],data["point2"]]
        
        try:
            result_args = cursor.callproc('matchClubs', args)
            results = list(cursor.fetchall())
            cursor.close()
            self.db._connection.commit()
            return True
        except Exception as e:
            return {'error': str(e)}
        finally:
            cursor.close()

