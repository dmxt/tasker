import unittest

from _base import BaseTestCase


class MyTestCase(BaseTestCase):
    def test_load_home_page(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
