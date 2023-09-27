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
# this is a default route so when the URL is runed this is seen rather than an error

@app.route('/restaurants' , methods=['GET'])
# the route specifies that it should only handle GET request
def get_restaurants():   
    return jsonify(data['restaurants'])
# the code returns a json response using jsonify with data from the restaurants 
# this code retrieves the list of restaurantsfrom data
@app.route('/restaurant/<int:id>', methods=['GET'])
# the id is converted into an interger
def get_restaurant(id):
    restaurant = next((r for r in data['restaurants'] if r['id'] == id), None)
    # the code tries to find a specific restaurant based on the id given in the URL
    # the r is used to iterate over the list of restaurants 
    if restaurant:
        return jsonify(restaurant)
    # if the matching is found it is assigned to the variable restaurant
    # it is then returned as a JSON response
    else:
        return jsonify({'error': 'Restaurant not found'}), 404
    # if no matching it brings an error
    
@app.route('/restaurants/<int:id>' , methods=['DELETE'])
def delete_restaurant(id):
    global data
    # the code begins declaring data as a global variable that stores info about restaurant
    restaurant = next((r for r in data['restaurants'] if r['id'] == id ), None)
    # this is used to iterate over the list of restaurants data 
    # the next function is used to find the first restaurant that matches the provided id
    if restaurant:
        # if it found it is assingned to the variable restaurant
        data['restaurants'].remove(restaurant)
        # if it found it is removed from the data restaurant
        return '' , 204
    else :
        return jsonify({'error': 'Restaurant not found'}), 404
@app.route('/pizzas' , methods=['GET'])
def get_pizzas():
    return jsonify(data['pizzas'])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():

    restaurant_pizza_data = request.get_json()
# the .get_json is used to extract the json data from the HTTP requests body
# the restaurant_pizza_data contains the json data that was extracted
    pizza_id = restaurant_pizza_data.get("pizza_id")
    restaurant_id = restaurant_pizza_data.get("restaurant_id")
    # this lines are extracting specific pieces of data from the restaurant_pizza_data

    if not pizza_id or not restaurant_id:
       return jsonify({"errors":["Missing pizza_id or restaurant_id"]}) ,400
# this conditional statement checks whether they are missing if either of them is missing it evalutes false 
    pizza = next ((p for p in data['pizzas'] if p['id'] == pizza_id) , None)
    restaurant = next((r for r in data['restaurant'] if r['id'] == restaurant_id) , None)
#  this lines intend to find a specific pizza and restaurant bassed on the id
# next returns the next item fromthe iterable
# it iterates through the data loking for items with matching id if a match is found it returns None
    if not pizza or not restaurant:
        return jsonify({"errors":["Pizza or restaurant not found"]}),404
    # this checks if both pizza and restaurant are missing to evealute False
    price = restaurant_pizza_data.get("price")
# here the code is extracting the price fromthe restaurant_pizza_data
    if not price or not (1 <= price <= 30):
        return jsonify({"errors":["Price must be between 1 and 30"]}) , 400
    # this checks if the price is missing or evalutes to false
    response_data = {
        "id": pizza_id,
        "name": pizza["name"],
        "ingredients": pizza["ingredients"]
    }

    return jsonify(response_data),201
if __name__ == '__main__':
    app.run(port=5555,debug=True)