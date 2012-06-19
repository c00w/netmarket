import requests
from frontend.test import *
valid_pages = ['/login']

def test_loads():
    for page in valid_pages:
        r = requests.get('http://127.0.0.1:5000' + page)
        assert 'Not Found' not in r.text
        assert 'Error' not in r.text

def test_register_login(credentials):
    username, password, cookies = credentials
    r = requests.post('http://127.0.0.1:5000/login', data = {'Username':username, 'Password':password, 'Method':'Login'})
    assert 'Invalid' not in r.text
    assert 'I am' in r.text

