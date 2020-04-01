from application import db


class Fighter(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    belt =db.Column(db.String(50), nullable=False)
    club =db.Column(db.String(144))
    weight = db.Column(db.Float)
    creator_id= db.Column(db.Integer, db.ForeignKey('account.id'), nullable= False)

    

    def __init__(self, name, belt, club, weight, creator_id):
        self.name= name
        self.belt=belt
        self.club=club
        self.weight=weight
        self.creator_id=creator_id


