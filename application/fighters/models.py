from application import db
from sqlalchemy.sql import text


class Fighter(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50), nullable=False)
    born= db.Column(db.Integer())
    belt =db.Column(db.String(50), nullable=False)
    club =db.Column(db.String(144))
    weight = db.Column(db.Float)
    creator_id= db.Column(db.Integer, db.ForeignKey('account.id'), nullable= False)

    

    def __init__(self, name, born, belt, club, weight, creator_id):
        self.name= name
        self.born=born
        self.belt=belt
        self.club=club
        self.weight=weight
        self.creator_id=creator_id


    @staticmethod
    def get_match_history(fighter_id):
        stmt = text("SELECT COALESCE((SELECT COUNT(*) FROM Match"
                    " WHERE (fighter1_id = :id OR fighter2_id = :id)),0)").params(id=fighter_id)
        
        res= db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])

        stmt = text("SELECT COALESCE((SELECT COUNT(*) FROM Match"
                    " WHERE winner_id = :id),0)").params(id=fighter_id)
        
        res= db.engine.execute(stmt)
        for row in res:
            response.append(row[0])

        print("res", response)
        return response
    

    @staticmethod
    def find_fighter_names(fighter_id, fighters):
        if not isinstance(fighter_id, int):
            fighter_id= int(fighter_id)

        for fighter in fighters:
            if fighter.id==fighter_id:
                return fighter.name
        
        return '<POISTETTU>'

    @staticmethod
    def filter_fighters(belt, club, clubs):

        club_filter=''
        for c in clubs:
            if int(c[0])==int(club):
                club_filter=c[1]

        if belt == '-1':
            stmt= text("SELECT * FROM Fighter"
                  + " WHERE Fighter.club=:searchword").params(searchword=club_filter)

        elif club == '-1':
            
            stmt= text("SELECT * FROM Fighter"
                   + " WHERE Fighter.belt=:searchword").params(searchword=belt)
        else:
            stmt= text("SELECT * FROM Fighter"
                   + " WHERE Fighter.club=:club"
                   + " AND Fighter.belt=:belt").params(club=club_filter, belt=belt)
        
        
        res= db.engine.execute(stmt)
        response=[]
        for row in res:
            response.append({"id":row[0], "name":row[1], "born":row[2], "belt":row[3], 
                "club":row[4], "weight":row[5]})

        return response


    @staticmethod
    def get_clubs():
        
        query = db.session().query(Fighter.club.distinct().label("club"))
        clubs_in_db = [row.club for row in query.all()]
        clubs_in_db.sort()
        club_choices=[('-1', 'Valitse seura')]
        for club in enumerate(clubs_in_db):
            club_choices.append(club)
        
        return club_choices
