from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

# Create a Flask application instance
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance with the Flask app
db = SQLAlchemy(app)

# Define the database model for the Item
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True)

    # Method to convert Item instances to dictionary format
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
    
# This function runs before the first request to ensure that the database tables are created
@app.before_first_request
def create_tables():
    db.create_all()

# Add a route for testing
@app.route('/')
def index():
    return "Is this thing on?"

if __name__ == '__main__':
    app.run(debug=True)