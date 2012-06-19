import requests
from frontend.test import * 

def test_create(credentials):
    username, password, cookies = credentials
    r = requests.get('http://localhost:5000/upload/create', cookies=cookies)
    assert '404'  not in r.text
