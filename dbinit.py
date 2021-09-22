import pymongo
from parkingslots import *
from config import *
print(parking_slots)

def connect_db(connection_uri, database):
    """
    :param connection_uri: srv connection uri of the mongodb database
    :param database: database name to connect with. If database does not exists, it creates one with the given name
    :return: database client object

    """
    try:
        client = pymongo.MongoClient(connection_uri)
        database_list = client.list_database_names()
        if database in database_list:
            print("Database exists")
            return client
        else:
            db = client[database]
            print(db)
            print("Database created")
            return client
    except:
        return "connection failed"

def init_collection(dbclient, databasename, collection_name, data_dict):
    """

    :param dbclient: client object for database
    :param databasename: name of the database to be used
    :param collection_name: name of the collection. If does not exists, will be created
    :param data_dict: data to be inserted
    :return: status of the insert operation
    """

    parkingdb = dbclient[databasename]
    collection_list = parkingdb.list_collection_names()
    if collection_name in collection_list:
        print("Collection already exists")
        return None
    else:
        parkingcol = parkingdb[collection_name]
        records = parkingcol.insert_one(data_dict)
        return records

#connection_string = "mongodb+srv://parkingadmin:parkingadmin@cluster0.uvrnm.mongodb.net/ParkingManagementSystem?retryWrites=true&w=majority"
#dbname = "ParkingManagementSystem"
#collection_name = "parkingslots"


#Connect to database
dbclient = connect_db(connection_string, dbname)

#Create collection and insert records
init_data = init_collection(dbclient, dbname, collection_name, parking_slots)
print(init_data)
