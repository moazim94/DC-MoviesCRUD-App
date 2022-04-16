from application import db
from application.models import DC_Movies


db.drop_all()
db.create_all()

movie_1 = DC_Movies(Movie_name = 'Batman Begins', Critics_score = '84', Release_date = '2005')
movie_2 = DC_Movies(Movie_name = 'The Dark Knight', Critics_score = '94', Release_date = '2008')
movie_3 = DC_Movies(Movie_name = 'The Dark Knight Rises', Critics_score = '87', Release_date = '2012')

movie_4 = DC_Movies(Movie_name = 'Man of Steel', Critics_score = '56', Release_date = '2013')
movie_5 = DC_Movies(Movie_name = 'Batman v Superman: Dawn of Justice', Critics_score = '29', Release_date = '2016')
movie_6 = DC_Movies(Movie_name = 'Suicide Squad', Critics_score = '26', Release_date = '2016')
movie_7 = DC_Movies(Movie_name = 'Wonder Woman', Critics_score = '93', Release_date = '2017')
movie_8 = DC_Movies(Movie_name = 'Justice League', Critics_score = '39', Release_date = '2017')

movie_9 = DC_Movies(Movie_name = 'Aquaman', Critics_score = '65', Release_date = '2018')
movie_10 = DC_Movies(Movie_name = 'Shazam', Critics_score = '90', Release_date = '2019')
movie_11 = DC_Movies(Movie_name = 'Birds of Prey', Critics_score = '79', Release_date = '2019')
movie_12 = DC_Movies(Movie_name = 'Wonder Woman: 1984', Critics_score = '58', Release_date = '2020')

movie_13 = DC_Movies(Movie_name = 'Justice League: Snyder Cut', Critics_score = '71', Release_date = '2021')
movie_14 = DC_Movies(Movie_name = 'The Suicide Squad', Critics_score = '90', Release_date = '2021')

db.session.add(movie_1)
db.session.add(movie_2)
db.session.add(movie_3) 
db.session.add(movie_4)
db.session.add(movie_5)
db.session.add(movie_6)
db.session.add(movie_7)
db.session.add(movie_8)
db.session.add(movie_9)
db.session.add(movie_10)
db.session.add(movie_11)
db.session.add(movie_12)
db.session.add(movie_13)
db.session.add(movie_14)

db.session.commit()
