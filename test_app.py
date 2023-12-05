import unittest
from app import app, db, User

class TestApp(unittest.TestCase):

    def setUp(self):
        # Use an SQLite in-memory database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()

        with app.app_context():  # Set up the application context
            db.create_all()

    def tearDown(self):
        with app.app_context():  # Set up the application context
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User List', response.data)

    def test_add_user(self):
        response = self.app.post('/add_user', data={'username': 'testuser', 'email': 'testuser@example.com'})
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect

        # Check if the user was added to the database
        with app.app_context():  # Set up the application context
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.username, 'testuser')
            self.assertEqual(user.email, 'testuser@example.com')

        # Check if the user is displayed on the home page
        response = self.app.get('/')
        self.assertIn(b'testuser - testuser@example.com', response.data)

if __name__ == '__main__':
    unittest.main()
