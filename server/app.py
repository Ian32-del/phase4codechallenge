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
    
@app.route('/restaurants/<int:id>' , methods=['DELETE'])
def delete_restaurant(id):
    global data
    restaurant = next((r for r in data['restaurants'] if r['id'] == id ), None)
    if restaurant:
        data['restaurants'].remove(restaurant)
        return '' , 204
    else :
        return jsonify({'error': 'Restaurant not found'}), 404
@app.route('/pizzas' , methods=['GET'])
def get_pizzas():
    return jsonify(data['pizzas'])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():

    restaurant_pizza_data = request.get_json()

    pizza_id = restaurant_pizza_data.get("pizza_id")
    restaurant_id = restaurant_pizza_data.get("restaurant_id")

    if not pizza_id or not restaurant_id:
       return jsonify({"errors":["Missing pizza_id or restaurant_id"]}) ,400

    pizza = next ((p for p in data['pizzas'] if p['id'] == pizza_id) , None)
    restaurant = next((r for r in data['restaurant'] if r['id'] == restaurant_id) , None)

    if not pizza or not restaurant:
        return jsonify({"errors":["Pizza or restaurant not found"]}),404
    
    price = restaurant_pizza_data.get("price")

    if not price or not (1 <= price <= 30):
        return jsonify({"errors":["Price must be between 1 and 30"]}) , 400
    
    response_data = {
        "id": pizza_id,
        "name": pizza["name"],
        "ingredients": pizza["ingredients"]
    }

    return jsonify(response_data),201
if __name__ == '__main__':
    app.run(port=5555,debug=True)