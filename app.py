from flask import Flask
import pymongo

app = Flask(__name__)

parking_slots = {
"Level-0": {
    "Motorcycle spots" : {
        "row1": ["M1", "M2", "M3", "M4", "M5", "M6"],
        "row2": ["M7", "M8", "M9", "M10", "M11", "M12"]
},
    "compact spots" : {
        "row1" : ["C1", "C2", "C3", "C4", "C5", "C6"],
        "row2" : ["C7", "C8", "C9", "C10", "C11", "C12"]
},
    "large spots": {
        "row1" : ["L1", "L2", "L3", "L4", "L5", "L6"],
        "row2" : ["L7", "L8", "L9", "L10", "L11", "L12"]
}
},
"Level-1" : {
     "Motorcycle spots" : {
        "row1": ["M1", "M2", "M3", "M4", "M5", "M6"],
        "row2": ["M7", "M8", "M9", "M10", "M11", "M12"]
},
    "compact spots" : {
        "row1" : ["C1", "C2", "C3", "C4", "C5", "C6"],
        "row2" : ["C7", "C8", "C9", "C10", "C11", "C12"]
},
    "large spots": {
        "row1" : ["L1", "L2", "L3", "L4", "L5", "L6"],
        "row2" : ["L7", "L8", "L9", "L10", "L11", "L12"]
}
},
"Level-2": {
     "Motorcycle spots" : {
        "row1": ["M1", "M2", "M3", "M4", "M5", "M6"],
        "row2": ["M7", "M8", "M9", "M10", "M11", "M12"]
},
    "compact spots" : {
        "row1" : ["C1", "C2", "C3", "C4", "C5", "C6"],
        "row2" : ["C7", "C8", "C9", "C10", "C11", "C12"]
},
    "large spots": {
        "row1" : ["L1", "L2", "L3", "L4", "L5", "L6"],
        "row2" : ["L7", "L8", "L9", "L10", "L11", "L12"]
}
},
"Level-3": {
     "Motorcycle spots" : {
        "row1":["M1", "M2", "M3", "M4", "M5", "M6"],
        "row2":["M7", "M8", "M9", "M10", "M11", "M12"]
},
    "compact spots" : {
        "row1" : ["C1", "C2", "C3", "C4", "C5", "C6"],
        "row2" : ["C7", "C8", "C9", "C10", "C11", "C12"]
},
    "large spots": {
        "row1" : ["L1", "L2", "L3", "L4", "L5", "L6"],
        "row2" : ["L7", "L8", "L9", "L10", "L11", "L12"]
}
}
}




connection_string = "mongodb+srv://parkingadmin:parkingadmin@cluster0.uvrnm.mongodb.net/ParkingManagementSystem?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)
db = ""
if "ParkingManagementSystem" in client.list_database_names():
    print("database exists")
    db = client["ParkingManagementSystem"]


@app.route("/hello")
def hello():
    return "Hello"


if __name__ == '__main__':
    app.run(debug = True)