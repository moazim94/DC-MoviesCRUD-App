from application import app, db
from flask import render_template, url_for, redirect, request
from flask_testing import TestCase
from application.models import DC_Movies, Users_Reviews
from application.forms import User_ReviewsForm, DC_MoviesForm

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:united123@10.70.0.3/flask-db',
           SECRET_KEY='Test_Secret_Key',
           WTF_CSRF_ENABLED = False
        )
        return app

        
    def setUp (self):
        db.create_all()
        movie_1 = DC_Movies(Movie_name = 'Batman Begins', Critics_score = '84', Release_date = '2005')
        movie_2 = DC_Movies(Movie_name = 'The Dark Knight', Critics_score = '94', Release_date = '2008')
        
        review_1 = Users_Reviews(DC_Movies_id = 1, First_name = 'Mohammed', Last_name = 'Azim', Review = 'Good', Score = '70')
        review_2 = Users_Reviews(DC_Movies_id = 1, First_name = 'John', Last_name = 'Doe', Review = 'Bad', Score = '40')

        db.session.add(movie_1)
        db.session.add(movie_2) 
        
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestModels(TestBase): # This is testing your add review function
    def test_add_review(self):
        response = self.client.get(url_for('add_review', film_id = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'First name', response.data)
       
    
    def test_delete_review(self):
        response = self.client.get(url_for('delete_review', id = 1))
        self.assertNotIn(b'First name', response.data)


    def test_add_review_page(self):
        response = self.client.post(
            url_for('add_review', film_id = 1), 
            data = dict(
                First_name = "Mohammed",
                Last_name = "Azim",
                Review = "Good",
                Score = "70"
            ),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_edit_review(self):
        response = self.client.post(
            url_for('edit_review', id = 1), 
            data = dict(
                First_name = "Mohammed",
                Last_name = "Azim",
                Review = "Good",
                Score = "70"
            ),
            follow_redirects=True
        )
        self.assertNotEqual(response.status_code, 200)
        
class TestWebPages(TestBase): #everything here will be testing the get/post requests for the web pages
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_review(self):
        response = self.client.get(url_for('view_review', film_id = 1))
        self.assertEqual(response.status_code, 200)

    

        