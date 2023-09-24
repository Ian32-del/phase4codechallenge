from app import db


restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'))
)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    pizzas = db.relationship('Pizza', secondary=restaurant_pizza, back_populates='restaurants')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    restaurants = db.relationship('Restaurant', secondary=restaurant_pizza, back_populates='pizzas')
