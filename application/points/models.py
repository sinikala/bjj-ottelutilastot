from application import db
from sqlalchemy.sql import text

class Point(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    point_type = place=db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False )
    done_by = db.Column(db.Integer, db.ForeignKey('Fighter.id'), nullable= False)


    def __init__(self, point_type, points, done_by):
        self.point_type =point_type
        self.points =points
        self.done_by = done_by