import requests

valid_pages = ['/login', '/register']

def test_loads():
    for page in valid_pages:
        r = requests.get('http://127.0.0.1:5000' + page)
        assert 'Not Found' not in r.text
        assert 'Error' not in r.text

def test_register_login():
    username ='123456789123456789testtest'
    r = requests.post('http://127.0.0.1:5000/login', data={'Username':username, 'Password':'pass', 'Method':'Register'})
    assert 'Invalid' not in r.text
    assert 'I am' in r.text

    r = requests.post('http://127.0.0.1:5000/login', data = {'Username':username, 'Password':'pass', 'Method':'Login'})
    assert 'Invalid' not in r.text
    assert 'I am' in r.text

    import frontend.db
    item = frontend.db.get_item('Users', username)
    frontend.db.delete_item('Users', username, item)
    
