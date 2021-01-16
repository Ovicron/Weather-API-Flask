from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False


from flaskwebsite import routes
from flaskwebsite import models
