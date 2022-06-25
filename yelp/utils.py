from pymongo import MongoClient
def get_db(db_name, host):
    client =MongoClient(host)
    db_handle = client[db_name]
    return db_handle, client
def get_collection(db_handle,collection_name):
    return db_handle[collection_name]