from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired, Length

# This page contains the forms that will be used in the app

class PersonalDetails(FlaskForm):
    name =StringField ('Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField ('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    #nationality = StringField('Nationality', validators=[DataRequired(), Length(min=2, max=20)])
    street = StringField('Street number and name', validators=[DataRequired(), Length(min=2, max=20)])
    suburb = StringField('suburb', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('city', validators=[DataRequired(), Length(min=2, max=20)])
    province = StringField('province', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField('email Address', validators=[DataRequired(), Length(min=2, max=20)])
    cell_num = StringField('cell_num ', validators=[DataRequired(), Length(min=2, max=20)])
    date_of_birth = StringField('date_of_birth', validators=[DataRequired(), Length(min=2, max=20)])



    submit = SubmitField('Submit')