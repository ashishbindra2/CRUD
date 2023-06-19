import os
from pymongo import MongoClient

os.environ["MONGO_URI"] = "mongodb://localhost:27017/"


class Connections:
    def __init__(self):
        self.mongo_client = MongoClient()

    def delete(self):
        self.mongo_client.close()
        print("obj main destroy")

class Employee(Connections):
    def __init__(self):
        super().__init__()
        self.db = self.mongo_client.employeedb
        self.employee = self.db['employee']

    def add_data(self,data):
        self.employee.insert_one(data)
    
    def add_all_data(self,data):
        self.employee.insert_many( data )
   
    def get_emp_data(self):
        response = self.employee.find()
        return list(response)
    def set_emp_data(self,id,data):
        print(id)
        print(data)
        self.employee.update_one(id, {"$set" : data})
        