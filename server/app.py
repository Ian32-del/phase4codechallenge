from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



if __name__ == '__main__':
    app.run()