import requests
from frontend.test import make_login

def test_request():
    def callback(usern, passw, cookies):
        r = requests.get("http://127.0.0.1:5000/files", cookies = cookies)
        assert '404' not in r.text
        assert 'Error' not in r.text
        assert 'Files' in r.text
        # Going to have to mock more of this stuff up.

    make_login(callback)
