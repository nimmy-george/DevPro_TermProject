# tests/test_app.py

import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Store Data in Redis</h1>', response.data)

    def test_store_data_route(self):
        response = self.app.post('/store_data', data={'key': 'test_key', 'value': 'test_value'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data stored successfully', response.data)

    def test_retrieve_data_route(self):
        self.app.post('/store_data', data={'key': 'test_key', 'value': 'test_value'})
        response = self.app.get('/retrieve/test_key')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'test_value', response.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
