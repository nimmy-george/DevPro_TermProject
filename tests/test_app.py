# tests/test_app.py

import pytest
from flask import Flask
from your_app_module.app import init_db, create_app

@pytest.fixture
def app():
    test_app = create_app()
    test_app.config['TESTING'] = True
    return test_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def database(app):
    init_db()
    yield
    # Clean up the test database after each test
    with app.app_context():
        conn = app.database.connect()
        conn.execute('DROP TABLE IF EXISTS users')
        conn.close()

def test_home_route(client, database):
    response = client.get('/')
    assert b'Member List' in response.data

def test_add_user(client, database):
    # Assuming you have an add_user route
    response = client.post('/add_user', data={'username': 'Nimmy', 'email': 'c0872805@mylambton.ca'})
    assert response.status_code == 302  # Assuming a redirect after adding a user

    # Verify that the user is added by checking the updated user list
    response = client.get('/')
    assert b'Nimmy' in response.data
    assert b'c0872805@mylambton.ca' in response.data
