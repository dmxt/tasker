import unittest

from _base import BaseTestCase


class MyTestCase(BaseTestCase):
    def test_load_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Table master</h1>', response.data)

    def test_load_stylesheet(self):
        response = self.client.get('/static/css/main.css')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
