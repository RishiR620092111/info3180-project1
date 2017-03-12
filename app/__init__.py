from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Ce2U9zj5NVu9Cl4H"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:pass@localhost/proj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views