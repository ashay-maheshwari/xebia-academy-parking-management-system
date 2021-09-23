from flask import Flask
import pymongo
from config import *
from dbinit import *
from parkingfunctions import *

print(add(5,6))

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
    levels = list(fetched_parking_status.keys())
    parking_found = 0

    # Remove _id key from the list
    levels.remove("_id")

    for level in levels:

        # Look for a spot in Motorcycle section first
        motorcycle_spots = list(parking_slots[level]["Motorcycle spots"].keys())
        for row in motorcycle_spots:
            if len(parking_slots[level]["Motorcycle spots"][row]) == 0:
                print("No parking found")
            else:
                parking_found = 1
                return "Parking found in motorcycle spot"

        # Look for a parking in compact spot
        compact_spots = list(parking_slots[level]["compact spots"].keys())
        for row in compact_spots:
            if len(parking_slots[level]["compact spots"][row]) == 0:
                print("No parking found")
            else:
                parking_found = 1
                return "Parking found in compact spot"

        # Look for a parking in large spot
        large_spots = list(parking_slots[level]["large spots"].keys())
        for row in large_spots:
            if parking_slots[level]["large spots"][row] == []:
                print("No parking found")
            else:
                parking_found = 1
                return "Parking found in a large spot"


if __name__ == '__main__':
    app.run(debug=True)
