from pprint import pprint

import apple

def test_working():
    r =apple.request('iron maiden')
    assert r
    assert 'error' not in r
    pprint(r)
