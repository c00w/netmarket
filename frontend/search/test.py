import requests

def test_load():
    r = requests.get("http://localhost:5000/search")
    assert '404' not in r.text
