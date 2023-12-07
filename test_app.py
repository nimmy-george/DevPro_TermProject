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
        # Clean up the database
        db.session.remove()
        db.drop_all()
        # Remove the application context after the test is done
        self.app_context.pop()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>User List</h1>', response.data)

    def test_add_user(self):
        response = self.app.post('/add_user', data={'username': 'testuser', 'email': 'testuser@example.com'})
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect

        # Check if the user was added to the database
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')

        # Check if the user is displayed on the home page
        response = self.app.get('/')
        self.assertIn(b'testuser - testuser@example.com', response.data)


if __name__ == '__main__':
    unittest.main()
