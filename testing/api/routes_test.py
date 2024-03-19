from unittest import TestCase
from unittest.mock import patch
import requests
import json

localhost = 'http://localhost:8000'

class Routes(TestCase):

    @patch('requests.post')
    def test_add_permission(self, mock_post):
        test_case = {"steam_id": "21938123", "permission": "Hecate"}
        resp = requests.post(localhost + '/permissions/add', data=json.dumps(test_case), headers={'Content-Type' : 'application/json'})
        mock_post.assert_called_with(localhost + '/permissions/add', data=json.dumps(test_case), headers={'Content-Type' : 'application/json'})

Routes().test_add_permission()