from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, UniqueConstraint

db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = 'restaurants'  # Custom table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    __table_args__ = (
        CheckConstraint("LENGTH(name) <= 50", name="check_name_length"),
        UniqueConstraint('name', name='unique_restaurant_name')
    )
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', back_populates='restaurants')

class Pizza(db.Model):
    __tablename__ = 'pizzas'  # Custom table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', back_populates='pizzas')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'  # Custom table name
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    price = db.Column(db.Float)

    __table_args__ = (
        CheckConstraint("price >= 1 AND price <= 30 " ,name="check_price_orange"),
    )