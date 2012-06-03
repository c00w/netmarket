import requests

def test_request():
    r = requests.get("http://127.0.0.1:5000/files")
    assert '404' not in r.text
    assert 'Error' not in r.text
    assert 'Files' in r.text
