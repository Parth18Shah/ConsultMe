from flask_login import UserMixin
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

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.String(30))
    username = db.Column(db.String(20),unique=True,nullable=False)
    content = db.Column(db.String(500), default='')
    ispatient = db.Column(db.Boolean, nullable=False)



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

# CREATE TABLE message (
#          id SERIAL PRIMARY KEY, 
#          username varchar(20) unique not null,
#          content varchar(500) not null,
#           ispatient boolean not null
# );