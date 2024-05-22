from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.todo_db

collection_name = db["todo_collection"]
