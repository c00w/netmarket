import requests
import upload.test
import search.test

def test_load():
    r = requests.get('http://localhost:5000/')
    assert '404' not in r.text
    assert 'Error' not in r.text
def test_site_up():
    r = requests.get('http://localhost:5000/non/existant/')
    assert '404' in r.text
