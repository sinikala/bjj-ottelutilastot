from application import db
from sqlalchemy.sql import text

class Points(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    points=db.Column(db.Integer, nullable=False)
    penalties = db.Column(db.Integer, nullable=False )
    advantage = db.Column(db.Integer, nullable=False )
    fighter_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable= False)



    def __init__(self, points, penalties, advantage, fighter_id):
        self.points =points
        self.penalties =penalties
        self.advantage=advantage
        self.fighter_id = fighter_id


    @staticmethod
    def get_points(match_id):
        stmt= text("SELECT id, points, penalties, advantage, fighter_id FROM Points "
                   + "LEFT JOIN matchpoints ON matchpoints.points_id = Points.id "
                   + "WHERE matchpoints.match_id = :id").params(id=match_id)

        res=db.engine.execute(stmt)

        response=[]
        for row in res:
            response. append({"id":row[0], "points":row[1], "penalties":row[2], "advantage":row[3], "fighter_id":row[4]})

        
        return response