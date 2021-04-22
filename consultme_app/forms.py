from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, IntegerField, DateField, RadioField, TextAreaField ,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from consultme_app.models import Users
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PatientRegistrationForm(FlaskForm):
    username = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    name = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Full Name"})
    gender = StringField('Gender',validators=[DataRequired()])
    email = StringField('',validators=[DataRequired(),Email()], render_kw={"placeholder": "Email"})
    phone = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Phone"})
    birthdate = DateField('',validators=[DataRequired()], format='%d/%m/%Y',render_kw={"placeholder": "Date of Birth(dd/mm/yyyy)"})
    age = IntegerField('',validators=[DataRequired()],render_kw={"placeholder": "Age"})
    med_history = TextAreaField('',validators=[DataRequired()],render_kw={"placeholder": "Past Medical history"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('',validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')


class DoctorRegistrationForm(FlaskForm):
    username = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    name = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Full Name"})
    gender = StringField('Gender',validators=[DataRequired()])
    specialist = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Specialist"})
    reg_no = IntegerField('',validators=[DataRequired()], render_kw={"placeholder": "Registration Number"})
    year_reg = DateField('',validators=[DataRequired()], format='%d/%m/%Y', render_kw={"placeholder": "Year of registration (dd/mm/yyyy)"})
    experience = StringField('',validators=[DataRequired(),Length(min=1 , max=20)],render_kw={"placeholder" : "Experience (in years)"})
    email = StringField('',validators=[DataRequired(),Email()], render_kw={"placeholder": "Email"})
    phone = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Phone"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('',validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')
	
class LoginForm(FlaskForm):
    username = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField('',validators=[DataRequired()],render_kw={"placeholder": "Email-id"})
    password = PasswordField('', validators=[DataRequired()],render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

class ChatForm(FlaskForm):
    message = StringField('',validators=[DataRequired(),Length(min=1,max=250)],render_kw={"placeholder": "Please enter your message here"})
    submit = SubmitField('Send')
    
class PredictForm(FlaskForm):
    feedback_input = StringField('Provide Rating to our Prediction :',validators=[DataRequired()])
    feedback = SubmitField('Submit')

class ConsultRate(FlaskForm):
    rate_input = StringField("Provide Rating to doctor's Consultation :",validators=[DataRequired()])
    rate = SubmitField('Submit')