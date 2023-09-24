from flask import Flask
from flask_sqlachemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza restaurant.db'
db = SQLAlchemy(app)

restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'))
)


class Restaurant(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    pizzas = db.relationship('Pizza', secondary=restaurant_pizza, back_populates='restaurant')

