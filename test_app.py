import unittest
from app import app, db, init_db

class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up the application context
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        # Create the database and initialize it
        db.create_all()
        init_db()

    def tearDown(self):
        # Remove the application context after the test is done
        self.app_context.pop()
        # Clean up the database
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get('/')
        # Your test assertions for the home page

    def test_add_user(self):
        response = self.app.post('/add_user', data={'username': 'testuser', 'email': 'testuser@example.com'})
        # Your test assertions for adding a user

if __name__ == '__main__':
    unittest.main()
