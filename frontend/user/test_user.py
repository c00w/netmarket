import requests

valid_pages = ['/login', '/register']

def test_loads():
    for page in valid_pages:
        r = requests.get('http://127.0.0.1:5000' + page)
        assert 'Not Found' not in r.text
        assert 'Error' not in r.text
