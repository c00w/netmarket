import requests
from frontend.test import * 

def test_request(credentials):
    username, password, cookies = credentials
    r = requests.get("http://127.0.0.1:5000/files", cookies = cookies)
    assert '404' not in r.text
    assert 'Error' not in r.text
    assert 'Files' in r.text
