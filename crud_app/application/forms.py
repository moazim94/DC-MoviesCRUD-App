from platform import mac_ver
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class DC_MoviesForm(FlaskForm):
    DC_Movies = StringField(
        'DC Movies',
        validators = [DataRequired(), Length(max = 100)]
    )
    Critics_score = StringField(
        'Critic score',
        validators = [DataRequired(), Length(max = 100)]
    )
    Release_date = StringField(
        'Release year',
        validators = [DataRequired(), Length(max = 100)]
    )
    submit = SubmitField('submit')

class User_ReviewsForm(FlaskForm):
     First_name = StringField(
        'First name',
        validators = [DataRequired(), Length(max = 100)]
    )
     Last_name = StringField(
        'Last name',
        validators = [DataRequired(), Length(max = 100)]
    )
     Score = StringField(
        'Score',
        validators = [DataRequired(), Length(max = 100)]
     )
     Review = StringField(
         'Review',
         validators = [DataRequired(), Length(max = 100)]
     )    
     submit = SubmitField('submit')
    