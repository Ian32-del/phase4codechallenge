from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    return '<hi> Welcome </h1>'

if __name__ == '__main__':
    app.run(port=5555,debug=True)