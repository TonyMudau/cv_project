from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired, Length

# This page contains the forms that will be used in the app

class UserDetails(FlaskForm):
    name =StringField ('Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField ('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    nationality = StringField('Nationality', validators=[DataRequired(), Length(min=2, max=20)])
    street = StringField('Street number and name', validators=[DataRequired(), Length(min=2, max=20)])
    suburb = StringField('suburb', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('city', validators=[DataRequired(), Length(min=2, max=20)])
    province = StringField('province', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField('email Address', validators=[DataRequired(), Length(min=2, max=20)])
    cell_num = StringField('cell_num ', validators=[DataRequired(), Length(min=2, max=20)])
    drivers_license = StringField('drivers_license', validators=[DataRequired(), Length(min=2, max=20)])

    # nationality = input('Nationality')
    # street = input('Street number and name')
    # suburb = input('Suburb')
    # city = input('City')
    # province = input('province')
    # email_address = input('email_address')
    # cell_num = input('cell_num ')
    # drivers_license = input('drivers_license')
    # project_link = input('project_link')
    #
    # high_school_name = input('high_school_name')
    # qualification = input('qualification ')
    # work_experience = input('work_experience')
    # skills = input('skills')
    # extra_activities = input('extra_activities')
    # references = input('references')
    # age = input('what is your age?')

    submit = SubmitField('Submit')