import os
from pymongo import MongoClient

os.environ["MONGO_URI"] = "mongodb://localhost:27017/"


class Connections:
    def __init__(self):
        self.mongo_client = MongoClient()

    def delete(self):
        self.mongo_client.close()
        print("obj main destroy")
