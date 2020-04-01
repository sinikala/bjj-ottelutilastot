from application import db

class Match(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date, default=db.func.current_date())
    place=db.Column(db.String(144), nullable=False)

    #fighter1=db.Column(db.String(144), nullable=False)
    #fighter2=db.Column(db.String(144), nullable=False)
    fighter1_id=db.Column(db.Integer, nullable=False )
    fighter2_id=db.Column(db.Integer, nullable=False)
    winner_id=db.Column(db.Integer)
    winning_category= db.Column(db.String(144))
    comment=db.Column(db.String(244))
    creator_id= db.Column(db.Integer, db.ForeignKey('account.id'), nullable= False)

   

    def __init__(self, place, winning_category, fighter1_id, fighter2_id, comment, creator_id):
        self.place = place
        self.winning_category= winning_category
        self.winner_id=1
        self.fighter1_id=fighter1_id
        self.fighter2_id=fighter2_id
        #self.winner_id=winner_id
        self.comment=comment
        self.creator_id=creator_id

        #fighter1_id, fighter2_id, winner_id, winning_category, comment, adder_id