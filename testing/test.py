import requests
import json

localhost = 'http://localhost:8000'

test_case = {"steam_id": "21938123", "permission": "Hecate", "request_origin" : localhost}
resp = requests.post(localhost + '/permissions/add', data=json.dumps(test_case), headers={'Content-Type' : 'application/json'})
print(resp.text)

test_case = {"include_hex" : True, "request_origin" : localhost, "bomboclart" : False}
resp = requests.post(localhost + '/permissions/list', data=json.dumps(test_case), headers={'Content-Type' : 'application/json'})
print(resp.text)