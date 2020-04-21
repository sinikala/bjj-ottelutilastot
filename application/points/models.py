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