import pytest
from app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Initialize the test database
    with app.app_context():
        init_db()

    yield client

def test_home_route(client):
    response = client.get('/')
    assert b'Member List' in response.data

def test_add_user(client):
    response = client.post('/add_user', data={'username': 'Nimmy', 'email': 'c0872805@mylambton.ca'})
    assert response.status_code == 302  # Assuming a redirect after adding a user
    
    # Verify that the user is added by checking the updated user list
    response = client.get('/')
    assert b'Nimmy' in response.data
