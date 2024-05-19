from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Create a Flask application instance
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise the SQLAlchemy database instance with the Flask app
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

# Custom CLI command to create database tables
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database initialised.')

# Route to serve the main web interface
@app.route('/')
def index():
    return render_template('index.html')

# REST API endpoint to get all items
@app.route('/api/items', methods=['GET'])
def get_items():
    items = Item.query.all()  # Query all items from the database
    return jsonify([item.to_dict() for item in items])  # Convert items to dictionary format and return as JSON