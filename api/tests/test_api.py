import random
import requests
import unittest

class TestApi(unittest.TestCase):

    def setUp(self):
        # API Base URL
        self.base_url = 'http://127.0.0.1:8888/'
        # Random Facebook ID for test
        self.facebook_id = 123
        # JSON Data to POST
        self.post_data = { 'facebookId': self.facebook_id }

    def test_list(self):
        response = requests.get(self.base_url + 'person')
        self.assertEqual(200, response.status_code)

    def test_list_with_limit(self):
        response = requests.get(self.base_url + 'person/?limit={0}'.format(random.randint(1,10)))
        self.assertEqual(200, response.status_code)

    def test_list_with_string_limit(self):
        response = requests.get(self.base_url + 'person/?limit={0}'.format('teste'))
        self.assertEqual(500, response.status_code)

    def test_post(self):
        response = requests.post(self.base_url + 'person/', self.post_data)
        self.assertEqual(201, response.status_code)

    def test_post_with_arg_in_url(self):
        response = requests.post(self.base_url + 'person/{0}'.format(int(self.facebook_id)), self.post_data)
        self.assertEqual(201, response.status_code)

    def test_post_with_string_arg(self):
        response = requests.post(self.base_url + 'person/', { 'facebookId': 'teste' })
        self.assertEqual(500, response.status_code)

    def test_post_with_string_arg_in_url(self):
        response = requests.post(self.base_url + 'person/{0}'.format('teste'), self.post_data)
        self.assertEqual(404, response.status_code)

    def test_post_without_facebook_id(self):
        response = requests.post(self.base_url + 'person/', { 'facebookId': None })
        self.assertEqual(500, response.status_code)

    def test_delete(self):
        response = requests.delete(self.base_url + 'person/{0}'.format(int(self.facebook_id)))
        self.assertEqual(204, response.status_code)

    def test_delete_without_facebook_id(self):
        response = requests.delete(self.base_url + 'person/')
        self.assertEqual(500, response.status_code)

    def test_delete_with_string_arg(self):
        response = requests.delete(self.base_url + 'person/{0}'.format('teste'))
        self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()