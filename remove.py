import pymongo

connection_string = "mongodb+srv://parkingadmin:parkingadmin@cluster0.uvrnm.mongodb.net/ParkingManagementSystem?retryWrites=true&w=majority"
dbname = "ParkingManagementSystem"
collection_name = "parkingslots"


client = pymongo.MongoClient(connection_string)
parking_db = client[dbname]
parkingcol = parking_db[collection_name]

myquery = {"Level-0.MotorcycleSpots.row1" : ["M1", "M2", "M3", "M4", "M5", "M6"]}
newvalues = { "$set" : { "Level-0.MotorcycleSpots.row1" : ["M1"]}}

parkingcol.update_one(myquery, newvalues)

for x in parkingcol.find():
    print(x)
