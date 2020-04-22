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
            
        #else:
         #   stmt= text("SELECT Fighter.name FROM Fighter"
          #          " WHERE Fighter.id = :id").params(id=fighter_id)
        #
         #   res= db.engine.execute(stmt)
          #  response=[]
           # for row in res:
                #response.append({"name":row[0]})
            #    return row[0]
            #return response

