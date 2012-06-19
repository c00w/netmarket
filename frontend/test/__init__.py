import requests

from frontend.configuration import USER_BUCKET_NAME

def pytest_funcarg__credentials(request):
    def setup():
        username = '123456789123456789testtest'
        r = requests.post('http://127.0.0.1:5000/login', data={'Username':username, 'Password':'pass', 'Method':'Register'})
        assert 'Invalid' not in r.text
        assert 'I am' in r.text
        return username, 'pass', r.cookies

    def teardown(item):
        username, password, cookies = item
        import frontend.db
        item = frontend.db.get_item(USER_BUCKET_NAME, username)
        frontend.db.delete_item(USER_BUCKET_NAME, username, item)
       
    return request.cached_setup(setup, teardown, 'session')
 
def make_login(callback, username=False):
    username = username if username else'123456789123456789testtest'
    r = requests.post('http://127.0.0.1:5000/login', data={'Username':username, 'Password':'pass', 'Method':'Register'})
    assert 'Invalid' not in r.text
    assert 'I am' in r.text

    callback(username, 'pass', r.cookies)

    import frontend.db
    item = frontend.db.get_item(USER_BUCKET_NAME, username)
    frontend.db.delete_item(USER_BUCKET_NAME, username, item)
    
