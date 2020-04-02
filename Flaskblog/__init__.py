from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='dfb8f820b9f89608fc694f97a38b98e5'
app.config['SQLALCHEMY_DATABASE_URI']=r'sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from Flaskblog import routes
