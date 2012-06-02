import requests

def test_request():
    r = requests.get("http://127.0.0.1:5000/settings")
    assert '404' not in r.text
    assert 'Error' not in r.text
    assert 'settings' in r.text
