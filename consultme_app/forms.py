from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, IntegerField, DateField, RadioField, TextAreaField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from consultme_app.models import Users


class PatientRegistrationForm(FlaskForm):
    username = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    name = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Full Name"})
    # gender = RadioField('Gender',choice=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    gender = StringField('Gender',validators=[DataRequired()])
    email = StringField('',validators=[DataRequired(),Email()], render_kw={"placeholder": "Email"})
    phone = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Phone"})
    birthdate = DateField('',validators=[DataRequired()], format='%d/%m/%Y',render_kw={"placeholder": "Date of Birth"})
    age = IntegerField('',validators=[DataRequired()],render_kw={"placeholder": "Age"})
    med_history = TextAreaField('',validators=[DataRequired()],render_kw={"placeholder": "Past Medical history"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('',validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
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
    username = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    name = StringField('',validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Full Name"})
    # gender = RadioField('Gender',choice=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    gender = StringField('Gender',validators=[DataRequired()])
    specialist = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Specialist"})
    reg_no = IntegerField('',validators=[DataRequired()], render_kw={"placeholder": "Registration Number"})
    year_reg = DateField('',validators=[DataRequired()], format='%d/%m/%Y', render_kw={"placeholder": "Year of registration"})
    experience = StringField('',validators=[DataRequired(),Length(min=1 , max=20)],render_kw={"placeholder" : "Experience"})
    email = StringField('',validators=[DataRequired(),Email()], render_kw={"placeholder": "Email"})
    phone = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Phone"})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('',validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
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
    username = StringField('',validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField('',validators=[DataRequired()],render_kw={"placeholder": "Email-id"})
    password = PasswordField('', validators=[DataRequired()],render_kw={"placeholder": "Password"})
    # remember = BooleanField('Remember me')
<<<<<<< HEAD
    
    submit = SubmitField('Login')


class ChatForm(FlaskForm):
    username = StringField('',validators=[DataRequired()])
    msg_sent = StringField('',validators=[Length(min=1,max=100)])
    msg_received = StringField('',validators=[Length(min=1,max=100)])
    specialist = StringField('',validators=[DataRequired()])
    experience = StringField('',validators=[DataRequired()])
    chat = SubmitField('Chat')
    send = SubmitField('Send')
    


    
=======
    submit = SubmitField('Login')

class ChatForm(FlaskForm):
    message = TextAreaField('',validators=[DataRequired()],render_kw={"placeholder": "Please enter your message here"})
    submit = SubmitField('Send')
    
>>>>>>> 81c7d278cb67a12bc093632e5e71429c9ba8d3be
