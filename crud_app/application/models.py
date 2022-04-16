from application import db
from datetime import datetime

class DC_Movies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Movie_name = db.Column(db.String(50), nullable=False)
    Critics_score = db.Column(db.String(30), nullable=False)
    Release_date = db.Column(db.String(30), nullable=False)
    users_reviews = db.relationship('Users_Reviews', backref = 'users_reviewsbr')
    
class Users_Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(30), nullable=False)
    Last_name = db.Column(db.String(30), nullable=False)
    Score = db.Column(db.String(30), nullable=False)
    Review = db.Column(db.String(400), nullable=False)
    DC_Movies_id = db.Column(db.Integer, db.ForeignKey('DC__movies.id'))
     
     