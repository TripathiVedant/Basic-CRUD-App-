from fastapi.testclient import TestClient
from index import app
import json
import pytest
from tests.integration.manage_user import User

client = TestClient(app)

@pytest.fixture()
def run_around_test():

    #create   
    test_user=User()
    assert test_user.create_user()
    
    # runtest
    yield test_user

    # teardown
    test_user.delete_user()
    test_user = None
    


def _write_data(payload, expected, code):
    response = client.post('/user/', data=json.dumps(payload))
    response_data = response.json()
    assert response.status_code == code
    if response.status_code==201:
        created_user=User(email=response_data[0].get('email'), id=response_data[0].get('id'))
    # if "id" in expected[0]:
    #     del expected[0]["id"]
    if response.status_code==201:
        if "id" in response_data[0]:
            del response_data[0]["id"]
    assert response_data == expected
    if response.status_code==201:
        created_user.delete_user()

def test_write_data_successful():
    payload={
        "email":"test_user_creation@rakuten.com",
        "password":"password@123",
        "username": "Vedant"
    }
    expected=[
        {
            "email": "test_user_creation@rakuten.com",
            "username": "Vedant",
            "password": "password@123"
        }
    ]
    code = 201
    _write_data(payload, expected, code)

def test_write_data_already_exists(run_around_test):
    test_user = run_around_test
    payload={
        "email":test_user.email,
        "password":"password@123",
        "username": "TestUser"
    }
    expected={
        "detail": "Email already Exists!"
    }
    code = 401
    _write_data(payload, expected, code)


def _read_data(payload, expected, code):
    response = client.get('/user/')
    response_data = response.json()
    assert response.status_code == code
    if response.status_code==200:
        assert len(response_data)>0

def test_read_data_success():
    payload={}
    expected={}
    code=200
    _read_data(payload, expected, code)

def _read_user_data(payload, expected, code):
    response = client.get("/user/{id}".format(id=payload['id']))
    response_data = response.json()
    assert response.status_code == code
    assert response_data==expected

def test_read_user_data_success(run_around_test):
    test_user = run_around_test
    payload={
        "id":test_user.id
    }
    expected=[{
        "id":test_user.id,
        "email":test_user.email,
        "username": "TestUser",
        "password":"password@123"
    }]
    code=200
    _read_user_data(payload, expected, code)
def test_read_user_data_not_exists():
    payload={
        "id":12414324346
    }
    expected={
        "detail": "Record do not exists"
    }
    code=404
    _read_user_data(payload, expected, code)

def _update_data(payload, expected, code):
    response = client.put("/user/{id}".format(id=payload['id']), data=json.dumps(payload))
    response_data = response.json()
    assert response.status_code == code
    assert response_data == expected
    
def test_update_data_successful(run_around_test):
    test_user = run_around_test
    payload={
        "id": test_user.id,
        "password":"password@123",
        "username": "Vedant"
    }
    expected=[
        {
            "id":test_user.id,
            "email": test_user.email,
            "username": "Vedant",
            "password": "password@123"
        }
    ]
    code = 200
    _update_data(payload, expected, code)

def test_update_data_not_exists():
    payload={
        "id":1231435346,
        "password":"password@123",
        "username": "TestUser"
    }
    expected={
        "detail": "User do not exists"
    }
    code = 404
    _update_data(payload, expected, code)

def _delete_data(payload, expected, code):
    response = client.delete("/user/{id}".format(id=payload['id']))
    response_data = response.json()
    assert response.status_code == code
    assert response_data==expected

def test_delete_data_successful(run_around_test):
    test_user = run_around_test
    payload={
        "id": test_user.id
    }
    expected=[
        {
            "id":test_user.id,
            "email": test_user.email,
            "username": "TestUser",
            "password": "password@123"
        }
    ]
    code = 200
    _delete_data(payload, expected, code)

def test_delete_data_not_exists():
    payload={
        "id":1231435346
    }
    expected={
        "detail": "User do not exists"
    }
    code = 404
    _delete_data(payload, expected, code)