from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

print("os >", os.environ.get("MONGODB_URL"))

db = MongoClient(os.environ.get("MONGODB_URL"))["fastapi"]
print("db connected successfully!")
