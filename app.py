from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db_schema import db, FitnessEntry

load_dotenv()
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/test')
def test():
    return render_template('test.html')

# @app.route('/chart-data')
# def chart_data():
#     entries = FitnessEntry.query.all()
#     data = {'date': [entry.date.strftime('%Y-%m-%d') for entry in entries],
#             'weight': [entry.weight for entry in entries]}
#     return jsonify(data)    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port=8080)
