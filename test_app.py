from app import app, db, User
import unittest

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_home_page(self) -> None:
        response = self.app.get('/')
        self.assertIn(b'Member List', response.data)

    def test_add_user(self) -> None:
        response = self.app.post('/add_user', data=dict(
            username='testuser',
            email='testuser@example.com'
        ), follow_redirects=True)
        self.assertIn(b'testuser', response.data)

if __name__ == '__main__':
    unittest.main()
