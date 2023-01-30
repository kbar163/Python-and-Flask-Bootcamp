import os
from data_models import db
from flask import Flask

#Getting the absolute path of the current file
basedir = os.path.abspath(os.path.dirname(__file__))

#Initializing app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

