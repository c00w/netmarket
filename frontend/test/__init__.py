import requests


def make_login(callback, username=False):
    username = username if username else'123456789123456789testtest'
    r = requests.post('http://127.0.0.1:5000/login', data={'Username':username, 'Password':'pass', 'Method':'Register'})
    assert 'Invalid' not in r.text
    assert 'I am' in r.text

    callback(username, 'pass', r.cookies)

    r = requests.post('http://127.0.0.1:5000/login', data = {'Username':username, 'Password':'pass', 'Method':'Login'})
    assert 'Invalid' not in r.text
    assert 'I am' in r.text

    import frontend.db
    item = frontend.db.get_item('Users', username)
    frontend.db.delete_item('Users', username, item)
    
