import requests
from frontend.test import make_login

def test_create():
    def body(user, passw, cookie):
        r = requests.get('http://localhost:5000/upload/create', cookies=cookie)
        assert '404'  not in r.text
    make_login(body)
