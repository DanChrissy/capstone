from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sup3r$3cretkey'

app.config.from_object(__name__)
from app import views
