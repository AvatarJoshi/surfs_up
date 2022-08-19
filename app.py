# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create the Flask engine to permit access to / query the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into our classes
Base = automap_base()

# Reflect the database
Base.prepare(engine, reflect=True)

# Create variables for our classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Create a new instance of the Flask App
app = Flask(__name__)

# Set Flask route starting point
@app.route('/') # '/' is the highest level hierarchy
def welcome(): # Notice we are using /api/v1.0/ followed by route. This is to indicate this is version 1 of our app
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        http://127.0.0.1:5000//api/v1.0/precipitation
        http://127.0.0.1:5000//api/v1.0/stations
        http://127.0.0.1:5000//api/v1.0/tobs
        http://127.0.0.1:5000//api/v1.0/temp/start/end
        ''')

# Set Flask route for precipitation data
@app.route('/api/v1.0/precipitation')

def precipitation():
    # Query to get the date and precipitation for the previous year.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    # Create dictionary with date as key and precipitation as value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Set Flask route for stations data
@app.route('/api/v1.0/stations')

def stations():
    # Query all stations in the database
    results = session.query(Station.station).all()
    # Unravel data into 1-dimensional array and convert the array into a list
    stations = list(np.ravel(results))
    return(jsonify(stations=stations))

# Set Flask route for temperature observations
@app.route('/api/v1.0/tobs')

def temp_monthly():
    # Calculate the date 1 year from last date in database. 
    # Query the primary station for all the temperature observations from the previous year.
    prev_year = dt.date(2017, 8 ,23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date >= prev_year).all()
    
    # Unravel data into 1-dimensional array and convert the array into a list
    temps = list(np.ravel(results))
    return(jsonify(temps=temps))

# Set Flask route for min,avg,max temp
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Query to get min avg and max temperatures
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    # 
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all() # The * indicates there will be multiple results for query
        temps = list(np.ravel(results))
        return(jsonify(temps=temps))

    results = session.query(*sel).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))
    return(jsonify(temps))