from flask_login import UserMixin
from datetime import datetime
from consultme_app import db ,login_manager

@login_manager.user_loader
def load_user(id):
	return Users.query.get(id)


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    u_name = db.Column(db.String(20),nullable=False)
    pswd = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)   
    phone = db.Column(db.String(10),nullable=False)
    gender = db.Column(db.String(10))
    specialist = db.Column(db.String(20))
    reg_no = db.Column(db.Integer)
    year_reg = db.Column(db.Date)
    birthdate = db.Column(db.Date)
    age = db.Column(db.Integer)
    med_history = db.Column(db.Text)
    ispatient = db.Column(db.Boolean, nullable=False)
    experience = db.Column(db.Text)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.specialist}','{self.experience}','{self.ispatient}')"

class Chat(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    senderid = db.Column(db.Integer,nullable=False)
    receiverid  = db.Column(db.Integer,nullable=False)
    message = db.Column(db.Text,nullable=False)
    send_time = db.Column(db.DateTime,nullable=False,default=datetime.now())

class PredictDisease(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    userid = db.Column(db.Integer,nullable=False)
    disease_name = db.Column(db.Text,nullable=False)
    symptom1 = db.Column(db.Text,nullable=False,default="0")
    symptom2 = db.Column(db.Text,nullable=False,default="0")
    symptom3 = db.Column(db.Text,nullable=False,default="0")
    symptom4 = db.Column(db.Text,nullable=False,default="0")
    symptom5 = db.Column(db.Text,nullable=False,default="0")
    feedback  = db.Column(db.String,nullable=False,default="True")


# CREATE TABLE users (
#          id SERIAL PRIMARY KEY, 
#          username varchar(20) unique not null,
#          u_name varchar(20) not null,
#          pswd varchar(100) not null,
#          phone varchar(10) not null,
#          email varchar(50) not null unique,
#          gender varchar(10),
#          specialist varchar(20),
#          reg_no INT,
#          year_reg DATE,
#          birthdate DATE,
#          age INT,
#          med_history varchar(100),
#           experience varchar(50),
#          ispatient boolean not null
# );

# ALTER TABLE users
# ADD COLUMN image_file varchar(20);

# CREATE TABLE chat (
#   id int not null auto-increment,
# 	senderid int not null,
#   receiverid int not null,
#   message text not null,
#   send_time datetime not null,
#   primary key(id)
# );

# CREATE TABLE chat (
#   id serial not null ,
# 	senderid int not null,
#   receiverid int not null,
#   message text not null,
#   send_time date not null,
#   primary key(id)
# );

# CREATE TABLE predict_disease (
#   id serial not null ,
# 	userid int not null,
#   disease_name text not null,
#   symptom1 text not null,
#   symptom2 text not null,
#   symptom3 text not null,
#   symptom4 text not null,
#   symptom5 text not null,
#   feedback boolean not null,
#   primary key(id)
# );