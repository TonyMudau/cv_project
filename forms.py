from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, RadioField, DateField
from wtforms.fields.core import SelectField
from wtforms.validators import  DataRequired, Length

# This page contains the forms that will be used in the app

class PersonalDetails(FlaskForm):
##Personal Details
    name =StringField ('Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField ('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    #nationality = StringField('Nationality', validators=[DataRequired(), Length(min=2, max=20)])
    street = StringField('Street number and name', validators=[DataRequired(), Length(min=2, max=20)])
    suburb = StringField('suburb', validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('city', validators=[DataRequired(), Length(min=2, max=20)])
    province = StringField('province', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField('email Address', validators=[DataRequired(), Length(min=2, max=20)])
    cell_num = StringField('cell_num ', validators=[DataRequired(), Length(min=2, max=11)])
    date_of_birth = StringField('date_of_birth', validators=[DataRequired(), Length(min=2, max=20)])
    #There is no class made for radio inputs under languages 
##About Me
    learning1 = StringField('learning1', validators=[Length(min=4, max=25)])
    learning2 = StringField('learning2', validators=[Length(min=4, max=25)])
    learning3 = StringField('learning3', validators=[Length(min=4, max=25)])

    contribute1 = StringField('contribute1', validators=[Length(min=4, max=25)])
    contribute2 = StringField('contribute2', validators=[Length(min=4, max=25)])
    
##Education 
    #High_school
    start_HS_year = DateField('Start_HS', format='%Y')
    finish_HS_year = DateField('finish_HS', format='%Y')
    school_name = StringField('HS_name', validators=[DataRequired(), Length(min=2, max=20)])
    #Uni/college
    start_college_year = DateField('Start_college', format='%Y')
    finish_college_year = DateField('finish_college', format='%Y')
    college_name = StringField('college_name', validators=[Length(min=2, max=20)])
    qualification = StringField('qualification', validators=[Length(min=2, max=20)])
##Online Certificates
    cert_name =  StringField('cert_name', validators=[Length(min=2, max=20)])
    site = StringField('cert_site', validators=[Length(min=2, max=20)])
    cert_date = DateField('Start_college', format='%Y - %M')
    cert_id = StringField('college_name', validators=[DataRequired(), Length(min=2, max=20)])
##Skills 
    #Make computer skills checkbox
    #Make interpersonal skills checkbox
    #Make some skills checkbox
    other_skill1 =  StringField('other_skill1', validators=[DataRequired(), Length(min=2, max=20)])
    other_skill2 =  StringField('other_skill2', validators=[DataRequired(), Length(min=2, max=20)])
    other_skill3 =  StringField('other_skill3', validators=[DataRequired(), Length(min=2, max=20)])
    #other_skill4 =  StringField('other_skill3', validators=[DataRequired(), Length(min=2, max=20)])
##Work Experience 
    job1_title =  StringField('job1_title', validators=[DataRequired(), Length(min=2, max=20)])
    job1_started = DateField('job1_started', format='%Y - %M')
    job1_finished = DateField('job1_finished', format='%Y - %M')
##learning


##Volunteering 

##Refernces 

    ref1_name =StringField ('ref1_name', validators=[DataRequired(), Length(min=2, max=20)])
    ref1_lastname = StringField ('ref1_lastname', validators=[DataRequired(), Length(min=2, max=20)])
    ref1_email = StringField('ref1_email', validators=[DataRequired(), Length(min=2, max=20)])
    ref1_number = StringField('ref1_number', validators=[DataRequired(), Length(min=2, max=11)])
   


    submit = SubmitField('Submit')