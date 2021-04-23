from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, template_folder='./templates/')
app.config['SECRET_KEY'] = '96e592be6947f9b29b1cd0f615a33610'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}:{port}/{database}'.format(user='root', password='root', server='localhost', port='3307', database='consult_me')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/consult_me'.format(user='root', password='root', server='localhost', port='5432', database='consult_me')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
USE_SESSION_FOR_NEXT = True
from consultme_app import routes