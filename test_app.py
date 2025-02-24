import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Welcome to the Calculator API'

def test_add_route(client):
    response = client.get('/add/5/3')
    assert response.status_code == 200
    assert response.json['result'] == 8

def test_divide_by_zero(client):
    response = client.get('/divide/10/0')
    assert response.status_code == 400
    assert 'error' in response.json

def test_multiply_route(client):
    response = client.get('/multiply/4/5')
    assert response.status_code == 200
    assert response.json['result'] == 20 