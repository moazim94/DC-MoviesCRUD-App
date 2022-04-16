from application import app, db
from application.forms import DC_MoviesForm, User_ReviewsForm
from application.models import DC_Movies, Users_Reviews
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_DC_Movies = DC_Movies.query.all()
    return render_template('index.html', all_DC_Movies = all_DC_Movies)

@app.route('/view_review/<int:film_id>')
def view_review(film_id):
    all_reviews = Users_Reviews.query.filter_by(DC_Movies_id=film_id).all()
    return render_template('display.html', all_reviews = all_reviews)

@app.route('/add_review/<int:film_id>', methods=['GET','POST'])
def add_review(film_id):
    form = User_ReviewsForm()   
    
    if request.method == "POST":
       
        user_review = Users_Reviews(
        DC_Movies_id = film_id,     
        First_name =  form.First_name.data,
        Last_name = form.Last_name.data,
        Review = form.Review.data,
        Score = form.Score.data,
        
        )
        
        db.session.add(user_review)
        db.session.commit()
        return redirect(url_for('index',film_id = film_id))
    
    return render_template('add_review.html', form = form)


@app.route('/edit_review/<int:id>', methods = ['GET', 'POST'])
def edit_review(id):
    review = Users_Reviews.query.get(id)
    form = User_ReviewsForm()

    if request.method == "POST":
        review.First_name = form.First_name.data
        review.Last_name = form.Last_name.data
        review.Review = form.Review.data
        review.Score = form.Score.data

        db.session.commit()
        return redirect(url_for('index'))
    form.First_name.data = review.First_name
    form.Last_name.data = review.Last_name
    form.Review.data = review.Review
    form.Score.data = review.Score
    
    return render_template('add_review.html', form = form)


@app.route('/delete_review/<int:id>')
def delete_review(id):
    review = Users_Reviews.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('index'))

      