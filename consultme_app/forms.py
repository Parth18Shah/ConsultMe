from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, IntegerField, DateField, RadioField, TextAreaField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from consultme_app.models import Users


class PatientRegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=4, max=20)])
    name = StringField('Full Name',validators=[DataRequired(), Length(min=4, max=20)])
    # gender = RadioField('Gender',choice=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    gender = StringField('Gender',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    phone = StringField('Phone',validators=[DataRequired()])
    birthdate = DateField('Date of Birth',validators=[DataRequired()], format='%d-%m-%Y')
    age = IntegerField('Age',validators=[DataRequired()])
    med_history = TextAreaField('Past medical history',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_username(self,username):
    #     user = Users.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('Username is already taken.Choose Differnt one!')

    # def validate_email(self,email):
    #     user = Users.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('Email already Exists!')

    # def validate_phone(self, phone):
    #     try:
    #         p = phonenumbers.parse(phone.data)
    #         if not phonenumbers.is_valid_number(p):
    #             raise ValueError()
    #     except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
    #         raise ValidationError('Invalid phone number')

class DoctorRegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=4, max=20)])
    name = StringField('Full Name',validators=[DataRequired(), Length(min=4, max=20)])
    # gender = RadioField('Gender',choice=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    gender = StringField('Gender',validators=[DataRequired()])
    specialist = StringField('Specialist',validators=[DataRequired()])
    reg_no = IntegerField('Registration Number',validators=[DataRequired()])
    year_reg = DateField('Year of registration',validators=[DataRequired()], format='%d-%m-%Y')
    email = StringField('Email',validators=[DataRequired(),Email()])
    phone = StringField('Phone',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_username(self,username):
    #     user = Users.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('Username is already taken.Choose Differnt one!')

    # def validate_email(self,email):
    #     user = Users.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('Email already Exists!')

    # def validate_phone(self, phone):
    #     try:
    #         p = phonenumbers.parse(phone.data)
    #         if not phonenumbers.is_valid_number(p):
    #             raise ValueError()
    #     except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
    #         raise ValidationError('Invalid phone number')
	
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember me')
    submit = SubmitField('Login')