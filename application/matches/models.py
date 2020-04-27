from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey, select
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text


matchpoints = db.Table('matchpoints', 
            db.Column('match_id', db.Integer, db.ForeignKey('match.id'), nullable=False),
            db.Column('points_id', db.Integer, db.ForeignKey('points.id'), nullable=False))    

matchfighter = db.Table('matchfighter', 
            db.Column('match_id', db.Integer, db.ForeignKey('match.id'), nullable=False),
            db.Column('fighter_id', db.Integer, db.ForeignKey('fighter.id'), nullable=False))  
       


class Match(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date, default=db.func.current_date())
    place=db.Column(db.String(144), nullable=False)
    winner_id=db.Column(db.Integer)
    winning_category= db.Column(db.String(144))
    comment=db.Column(db.String(244))
    creator_id= db.Column(db.Integer, db.ForeignKey('account.id'), nullable= False)

    points=db.relationship('Points', secondary=matchpoints, backref='match')
    fighters=db.relationship('Fighter', secondary=matchfighter, backref='match')
   

    def __init__(self, date, place, winning_category, winner_id, comment, creator_id):
        self.date=date
        self.place = place
        self.winning_category= winning_category
        self.winner_id=winner_id
        self.comment=comment
        self.creator_id=creator_id


    @staticmethod
    def get_fighters(match_id):
        stmt= text("SELECT id, name, belt FROM Fighter "
                   + "LEFT JOIN matchfighter ON matchfighter.fighter_id = Fighter.id "
                   + "WHERE matchfighter.match_id = :id").params(id=match_id)

        res=db.engine.execute(stmt)
        response=[]

        for row in res:
            response.append({"id":row[0], "name":row[1], "belt":row[2]})

        
        if len(response)==0:
            response. append({"id":'<POISTETTU>', "name":'<POISTETTU>', "belt":'<POISTETTU>'})
            response. append({"id":'<POISTETTU>', "name":'<POISTETTU>', "belt":'<POISTETTU>'})

        elif len(response)==1:
            response. append({"id":'<POISTETTU>', "name":'<POISTETTU>', "belt":'<POISTETTU>'})

        return response


    @staticmethod
    def get_matches_by_fighter(fighters):
       
        fighter_ids=[]
       
        for fighter in fighters:
          fighter_ids.append(fighter.id)

            
        match_ids= db.session().execute(select(
        [matchfighter.c.match_id], 
        matchfighter.c.fighter_id.in_(fighter_ids), distinct=True )).fetchall()
      
        matches=[]

        for id in match_ids:
          matches.append(Match.query.get_or_404(id))

        return matches
       

    @staticmethod
    def filter_matches(belt, club, clubs, winning_category):

        club_filter=''
        for c in clubs:
            if int(c[0])==int(club):
                club_filter=c[1]

        #only category
        if (belt == '-1' and club == '-1'):
            stmt= text("SELECT match.id FROM match"
                  + " WHERE match.winning_category=:category").params(category=winning_category)


        #only belt
        elif (winning_category == '-1' and club == '-1'):
             stmt= text("SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE fighter.belt=:belt").params(belt=belt)


        # only club
        elif (winning_category == '-1' and belt == '-1'):
             stmt= text("SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE fighter.club=:club").params(club=club_filter)


        # win + belt
        elif club == '-1':
             stmt= text("SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE match.winning_category=:category"
                  + " AND fighter.belt=:belt").params(category=winning_category, belt=belt)


        #win + club
        elif belt == '-1':
             stmt= text("SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE match.winning_category=:category"
                  + " AND fighter.club=:club").params(category=winning_category, club=club_filter)


        # club + belt
        elif winning_category == '-1':
             stmt= text("SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE fighter.club=:club"
                  + " AND fighter.belt=:belt").params(club=club_filter, belt=belt)


        #all
        else:
            stmt= text("SELECT DISTINCT match.id FROM match"
                  + " JOIN matchfighter ON matchfighter.match_id = match.id"
                  + " JOIN fighter ON fighter.id = matchfighter.fighter_id"
                  + " WHERE match.winning_category=:category"
                  + " AND fighter.club=:club"
                  + " AND fighter.belt=:belt").params(category=winning_category, club=club_filter, belt=belt)
        
        
        res= db.engine.execute(stmt)
        matches=[]

        for row in res:
          matches.append(Match.query.get_or_404(row[0]))

        return matches
