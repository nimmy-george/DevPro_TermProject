# tests/test_app.py

from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert b'Member List' in response.data
