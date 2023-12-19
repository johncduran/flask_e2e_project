from flask import Flask, render_template
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

load_dotenv()
app = Flask(__name__) 

print('Here is the', os.getenv("DB_PASSWORD"))
print('Here is the', os.getenv("DB_URL"))


#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Final897@34.30.218.222/john"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy instance
db = SQLAlchemy(app)

class FitnessEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Float)  # This assumes 'weight' should be a FLOAT
    blood_pressure = db.Column(db.String(20))
    workout = db.Column(db.String(255))
    contact_number = db.Column(db.Float)
### Part 2 - initial sqlalchemy-engine to connect to db:

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL,
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )    


## Test connection

inspector = inspect(engine)
inspector.get_table_names()

# Configure SQLAlchemy for Azure MySQL database
#DATABASE_URL = os.getenv("DB_URL")

#engine = create_engine(DATABASE_URL,
                         #connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         #)

## Test connection

##inspector = inspect(engine)
#inspector.get_table_names()

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Base = declarative_base()

#Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/chart-data')
def chart_data():
    entries = FitnessEntry.query.all()
    data = {'date': [entry.date.strftime('%Y-%m-%d') for entry in entries],
            'weight': [entry.weight for entry in entries]}
    return jsonify(data)    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
