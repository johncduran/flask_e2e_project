"""

pip install sqlalchemy mysql-connector-python

"""

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Create SQLAlchemy instance
db = SQLAlchemy()

class FitnessEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Float)
    blood_pressure = db.Column(db.String(20))
    workout = db.Column(db.String(255))