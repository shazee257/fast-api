from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27017/")["fastapi"]
print("db connected successfully!")
