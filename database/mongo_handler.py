from pymongo import MongoClient
import os


client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

def save_to_collection(collection_name, data):
    if isinstance(data, list):
        db[collection_name].insert_many(data)
    else:
        db[collection_name].insert_one(data)