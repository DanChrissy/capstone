from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sup3r$3cretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:capstone@localhost/capstone_records'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models

