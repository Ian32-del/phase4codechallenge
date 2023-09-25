from flask import Flask , jsonify , request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import Restaurant, Pizza, RestaurantPizza
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Read data from the JSON seed file
with open('seed.py', 'r') as json_file:
    data = json.load(json_file)



@app.route('/')
def index():
    return '<hi> Welcome </h1>'

@app.route('/restaurants' , methods=['GET'])
def get_restaurants():
    return jsonify(data['restaurants'])

@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = next((r for r in data['restaurants'] if r['id'] == id), None)
    if restaurant:
        return jsonify(restaurant)
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

if __name__ == '__main__':
    app.run(port=5555,debug=True)