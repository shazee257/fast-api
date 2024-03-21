from fastapi import Depends
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


class Database:
    _client = None

    @classmethod
    def get_database(cls):
        if cls._client is None:
            print("db instantiated now!")
            cls._client = MongoClient(os.environ.get("MONGODB_URL"))["fastapi"]
        return cls._client


def get_db(db: MongoClient = Depends(Database.get_database)):
    return db
