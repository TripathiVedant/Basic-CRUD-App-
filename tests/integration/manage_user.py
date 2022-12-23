from fastapi.testclient import TestClient
from index import app
import json
import string
import random

client = TestClient(app)
class User:
    def __init__(self, email=None, id=None):
        self.email = email
        self.id = id

    def create_user(self):
        self.email='test'+''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 10))+'@testUser.com'
        payload= {
            "email":self.email,
            "password":"password@123",
            "username": "TestUser"
        }
        response = client.post('/user/', data=json.dumps(payload))
        response_data = response.json()
        if response.status_code==201:
            self.id=response_data[0].get('id')
        return response.status_code == 201
    
    def delete_user(self):
        response=client.delete("/user/{id}".format(id=self.id))
        response_data = response.json()
        return response.status_code == 200
