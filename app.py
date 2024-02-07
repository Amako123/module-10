import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#* Running on http://127.0.0.1:5000


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)





@app.route("/")
def welcome():
 return (f"Welcome page <br/>"
f"Routes: <br/>"
f"/api/v1.0/precipitation <br/>"
f"/api/v1.0/stations <br/>"
f"/api/v1.0/tobs <br/>")

           
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
    

@app.route("/api/v1.0/stations")

def station():
    result = session.query(Station.station).all()
    station_list = list(np.ravel(result))
    return jsonify (station_list)



@app.route("/api/v1.0/tobs")

def tobs():
    tobs1 = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281' ).\
        filter(Measurement.date >= '2017,8,23').all()
    
    tobs_list = list(np.ravel(tobss))
    return jsonify (tobs_list)



@app.route ("/api/v1.0/<start>/<end>")

def temps(start,end):
    results = session.query(Measurement).filter(Measurement.date>= start).filter(Measurement.date<=end)
    shown =[] 
    for row in findings:
        shown.append(row.tobs) 
    return (jsonify ({"tempmin": min(found),"tempmax": max(found),"tempavg":np.mean}))
           
            

if __name__ == "__main__":
   app.run(debug=True)
