import os
import unittest
from unittest.mock import patch, Mock
from app import app, fetch_movies

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_search_status_code(self):
        response = self.app.post('/search', data=dict(movieQuery="test"))
        self.assertEqual(response.status_code, 200)

    @patch('app.requests.get')
    def test_fetch_movies(self, mock_get):
        mock_get.return_value.json.return_value = {'results': 'test'}
        result = fetch_movies("test")
        self.assertEqual(result, 'test')

if __name__ == '__main__':
    unittest.main()