from flask import Flask
import pymongo
from config import *
from dbinit import *
from parkingfunctions import *


app = Flask(__name__)

# Connect to database
dbclient = connect_db(connection_string, dbname)
parkingdb = dbclient[dbname]
parkingcol = parkingdb[collection_name]

fetched_parking_status = parkingcol.find_one()
print(fetched_parking_status)

# pprint(fetched_parking_status)


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/park-bike")
def park_motorcycle():
    check_parking = bike_parking("TS07HK2216", "15", fetched_parking_status)
    return check_parking


if __name__ == '__main__':
    app.run(debug=True)
