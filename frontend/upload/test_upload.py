import requests

def test_create():
    r = requests.get('http://localhost:5000/upload/create')
    assert '404'  not in r.text

def test_upload():
    r = requests.get("http://localhost:5000/upload/create")
    assert '404' not in r.text
