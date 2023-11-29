# tests/test_app.py

import pytest
from app.app import app, init_db

@pytest.fixture
def client():
    test_app = app
    test_app.config['TESTING'] = True
    with test_app.test_client() as client:
        # Initialize the database before each test
        init_db()
        yield client

def test_home_route(client):
    response = client.get('/')
    assert b'Member List' in response.data

def test_add_user(client):
    # Assuming you have an add_user route
    response = client.post('/add_user', data={'username': 'Nimmy', 'email': 'c0872805@mylambton.ca'})
    assert response.status_code == 302  # Assuming a redirect after adding a user

    # Verify that the user is added by checking the updated user list
    response = client.get('/')
    assert b'Nimmy' in response.data
    assert b'c0872805@mylambton.ca' in response.data
