from flask import Blueprint, render_template
from apps.app import db
from apps.crud.models import User

crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static')

user = User(username="john", email="hzdkv@example.com", password="123456")
@crud.route('/sql')
def sql():
    db.session.add(user)
    db.session.commit()
    #User.query.all()
    return "Please confirm db history"


@crud.route('/')
def index():
    return render_template('index.html')
