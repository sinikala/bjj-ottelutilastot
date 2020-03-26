from application import db


class Fighter(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    belt =db.Column(db.String(50), nullable=False)
    club =db.Column(db.String(144))
    weight = db.Column(db.Float)

    def __init__(self, name, belt, club, weight):
        self.name= name
        self.belt=belt
        self.club=club
        self.weight=weight


