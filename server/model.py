from flask_SQLAlchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy


restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id')),
    db.Column('price', db.Float , nullable=False),
    CheckConstraint('price >= 1 AND price <= 30', name='check_price_range')
)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    pizzas = db.relationship('Pizza', secondary=restaurant_pizza, back_populates='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    restaurants = db.relationship('Restaurant', secondary=restaurant_pizza, back_populates='pizzas')
