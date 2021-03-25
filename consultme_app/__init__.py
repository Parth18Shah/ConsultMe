from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO


app = Flask(__name__, template_folder='./templates/')
socketio = SocketIO(app)
app.config['SECRET_KEY'] = '96e582be6947f9b29b1cd0f615a33600'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/consult_me'.format(user='root', password='root', server='localhost', port='5432', database='consult_me')
# for postgres example statement for the above line: 'postgresql://postgres:root@localhost/consult_me'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
USE_SESSION_FOR_NEXT = True
from consultme_app import routes